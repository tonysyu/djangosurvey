from django import urls
from django.test import TestCase

from .models import Question


class QuestionViewTests(TestCase):

    def test_index_view_with_a_question(self):
        create_question("One question.")
        response = self._get_polls_response()
        assert (repr(response.context['question'])
                == '<Question: One question.>')

    def test_index_view_with_two_questions(self):
        create_question("Question 1.")
        create_question("Question 2.")
        response = self._get_polls_response()
        assert response.context['question'] in Question.objects.all()

    def test_index_view_with_no_questions(self):
        response = self.client.get(urls.reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        response = self._get_polls_response()
        assert b"No polls are available." in response.content

    def _get_polls_response(self):
        return self.client.get(urls.reverse('polls:index'))


def create_question(text):
    """Create question and insert it into the database."""
    return Question.objects.create(question_text=text)
