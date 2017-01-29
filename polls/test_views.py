import datetime

from django import urls
from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(publish_date=time_from_now(hours=-1))
        assert recent_question.was_published_recently()

    def test_was_published_recently_with_old_question(self):
        old_question = Question(publish_date=time_from_now(days=-30))
        assert not old_question.was_published_recently()

    def test_was_published_recently_with_future_question(self):
        future_question = Question(publish_date=time_from_now(days=30))
        assert not future_question.was_published_recently()


class QuestionViewTests(TestCase):

    def test_index_view_with_a_past_question(self):
        create_question("Past question.", time_from_now(days=-30))
        response = self._get_polls_response()
        assert (repr(response.context['question'])
                == '<Question: Past question.>')

    def test_index_view_with_two_past_questions(self):
        create_question("Older question.", time_from_now(days=-30))
        create_question("Recent question.", time_from_now(days=-5))
        response = self._get_polls_response()
        assert response.context['question'] in Question.objects.all()

    def test_index_view_with_no_questions(self):
        response = self.client.get(urls.reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        response = self._get_polls_response()
        self._assert_no_question(response)

    def test_index_view_with_a_future_question(self):
        create_question("Future question.", time_from_now(days=30))
        response = self._get_polls_response()
        self._assert_no_question(response)

    def test_index_view_with_future_and_past_question(self):
        create_question("Past question.", time_from_now(days=-30))
        create_question("Future question.", time_from_now(days=30))
        response = self._get_polls_response()
        assert (repr(response.context['question'])
                == '<Question: Past question.>')

    def _assert_no_question(self, response):
        assert b"No polls are available." in response.content

    def _get_polls_response(self):
        return self.client.get(urls.reverse('polls:index'))


def create_question(text, publish_date=None):
    """Create question and insert it into the database."""
    publish_date = publish_date if publish_date is not None else timezone.now()
    return Question.objects.create(question_text=text,
                                   publish_date=publish_date)


def time_from_now(**kwargs):
    """Return current time plus timedelta defined by keyword-arguments.

    Allowed keyword-arguments are the same as those for datetime.timedelta
    (hours, days, etc.). Negative deltas will a give time in the past.
    """
    return timezone.now() + datetime.timedelta(**kwargs)
