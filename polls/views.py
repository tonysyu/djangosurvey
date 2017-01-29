from random import randint

from django import urls
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


class IndexView(generic.DetailView):

    model = Question
    template_name = 'polls/index.html'

    def get_object(self):
        question_id = self._random_question_id()
        if question_id is None:
            return None
        return get_object_or_404(Question, pk=question_id)

    def _random_question_id(self):
        """Return a random question.

        Adapted from http://stackoverflow.com/a/6405601/260303
        """
        questions = Question.objects.filter(publish_date__lte=timezone.now())
        if not questions:
            return None
        random_index = randint(0, len(questions) - 1)
        return questions[random_index].id


class ResultsView(generic.DetailView):

    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        redirect_url = urls.reverse('polls:results', args=(question.id,))
        return HttpResponseRedirect(redirect_url)
