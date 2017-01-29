from django.db import models
from django.contrib.auth.models import User


DEFAULT_STRING_LENGTH = 200


class Question(models.Model):

    question_text = models.CharField(max_length=DEFAULT_STRING_LENGTH)

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=DEFAULT_STRING_LENGTH)

    def __str__(self):
        return self.choice_text


class UserResponse(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return '{}|{}'.format(self.user.username, self.choice.choice_text)
