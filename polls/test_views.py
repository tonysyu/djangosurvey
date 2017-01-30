from django import urls
from django.test import TestCase

from .models import Question
from .testing_utils import create_question_choices, create_user_response


class QuestionViewTests(TestCase):

    def test_index_view_with_a_question(self):
        create_question_choices("One question.")
        response = self._get_polls_response()
        assert (repr(response.context['question'])
                == '<Question: One question.>')

    def test_index_view_with_two_questions(self):
        create_question_choices("Question 1.")
        create_question_choices("Question 2.")
        response = self._get_polls_response()
        assert response.context['question'] in Question.objects.all()

    def test_index_view_with_no_questions(self):
        response = self.client.get(urls.reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self._assert_text_in_response(b"No questions defined.")

    def test_index_view_with_all_questions_answered(self):
        user = self._get_user()
        question, (a, b, c) = create_question_choices("Question.", 'ABC')
        create_user_response(user, a)
        self._assert_text_in_response(b"You've answered all questions.")

    def _assert_text_in_response(self, text):
        response = self._get_polls_response()
        assert text in response.content

    def _get_polls_response(self):
        return self.client.get(urls.reverse('polls:index'))

    def _get_user(self):
        response = self._get_polls_response()
        return response.context['user']
