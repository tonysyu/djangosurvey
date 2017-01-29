import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


DEFAULT_STRING_LENGTH = 200
RECENT_TIME_DELTA = datetime.timedelta(days=1)


class Question(models.Model):

    question_text = models.CharField(max_length=DEFAULT_STRING_LENGTH)
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        recent_past = now - RECENT_TIME_DELTA
        return recent_past <= self.publish_date <= now

    was_published_recently.admin_order_field = 'publish_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


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
