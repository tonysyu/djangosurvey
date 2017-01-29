from random import randint

from django.utils import timezone

from .models import Question


def random_question():
    """Return a random question.

    Adapted from http://stackoverflow.com/a/6405601/260303
    """
    questions = Question.objects.filter(publish_date__lte=timezone.now())
    if not questions:
        return None
    random_index = randint(0, len(questions) - 1)
    return questions[random_index]
