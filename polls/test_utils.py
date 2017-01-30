import pytest
from django.contrib.auth.models import User

from .testing_utils import get_question_choices, get_user_response
from .utils import summarize_user_responses


def test_summarize_one_user_response(default_user):
    question, (a, b, c) = get_question_choices('Question', 'ABC')
    response = get_user_response(default_user, a)

    assert (summarize_user_responses([a, b, c], [response])
            == {'Question': {'A': 1, 'B': 0, 'C': 0}})


def test_summarize_choose_a_twice(default_user):
    question, (a, b, c) = get_question_choices('Question', 'ABC')
    responses = [get_user_response(default_user, a) for i in range(2)]

    assert (summarize_user_responses([a, b, c], responses)
            == {'Question': {'A': 2, 'B': 0, 'C': 0}})


def test_summarize_choose_each_once(default_user):
    question, choices = get_question_choices('Question', 'ABC')
    responses = [get_user_response(default_user, each) for each in choices]

    assert (summarize_user_responses(choices, responses)
            == {'Question': {'A': 1, 'B': 1, 'C': 1}})


def test_summarize_two_questions(default_user):
    question_1, (a, b, c) = get_question_choices('Question 1', 'ABC')
    question_2, (x, y, z) = get_question_choices('Question 2', 'XYZ')
    responses = [get_user_response(default_user, c),
                 get_user_response(default_user, z)]

    assert (summarize_user_responses([a, b, c, x, y, z], responses)
            == {'Question 1': {'A': 0, 'B': 0, 'C': 1},
                'Question 2': {'X': 0, 'Y': 0, 'Z': 1}})


@pytest.fixture
def default_user():
    return User(username='default_user')
