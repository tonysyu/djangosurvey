from .models import Choice, Question, UserResponse


def create_question_choices(text, choices=()):
    """Create question with choices, and insert it into the database.
    """
    question = Question.objects.create(question_text=text)
    return [Choice.objects.create(choice_text=choice_text, question=question)
            for choice_text in choices]


def create_user_response(user, choice):
    return UserResponse.objects.create(user=user, choice=choice,
                                       question=choice.question)


def get_question_choices(text, choices=()):
    """Create question with choices.
    """
    question = Question(question_text=text)
    return (question, [Choice(choice_text=choice_text, question=question)
                       for choice_text in choices])


def get_user_response(user, choice):
    return UserResponse(user=user, choice=choice, question=choice.question)
