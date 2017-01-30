from .models import Choice, Question, UserResponse


def create_question_choices(text, choices=()):
    """Create question with choices, and insert it into the database.
    """
    question = Question.objects.create(question_text=text)
    choices = get_choices(question, choices)
    for each in choices:
        each.save(force_insert=True)
    return (question, choices)


def create_user_response(user, choice):
    user_response = get_user_response(user, choice)
    user_response.save(force_insert=True)
    return user_response


def get_question_choices(text, choices=()):
    """Create question with choices.
    """
    question = Question(question_text=text)
    return (question, get_choices(question, choices))


def get_choices(question, choices=()):
    return [Choice(choice_text=choice_text, question=question)
            for choice_text in choices]


def get_user_response(user, choice):
    return UserResponse(user=user, choice=choice, question=choice.question)
