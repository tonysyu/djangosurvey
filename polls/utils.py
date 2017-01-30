from itertools import groupby
from random import randint

from .models import Choice, Question, UserResponse


def random_question():
    """Return a random question.

    Adapted from http://stackoverflow.com/a/6405601/260303
    """
    questions = Question.objects.all()
    if not questions:
        return None
    random_index = randint(0, len(questions) - 1)
    return questions[random_index]


def summarize_survey_results():
    """Return summary of survey results (a.k.a. UserResponses).
    """
    return summarize_user_responses(Choice.objects.all(),
                                    UserResponse.objects.all())


def summarize_user_responses(choices, user_responses):
    """Return summary of UserResponse objects.
    """
    results = _init_question_results(choices)
    for response in user_responses:
        question = response.question.question_text
        choice = response.choice.choice_text
        results[question][choice] += 1
    return results


def _init_question_results(choices):
    """Return dict of questions with dicts of choice counts initialized to 0.
    """
    choice_by_question = groupby(choices, lambda c: c.question.question_text)
    return {question_text: {choice.choice_text: 0 for choice in choice_list}
            for question_text, choice_list in choice_by_question}
