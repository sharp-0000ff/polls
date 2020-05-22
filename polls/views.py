from django.shortcuts import render, get_object_or_404
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        return models.Question.objects.order_by('-publish_date')[:5]


class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'polls/detail.html'


class DeleteView(generic.DeleteView):
    model = models.Question
    template_name_suffix = '_delete'
    success_url = reverse_lazy('polls:index')


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Вы не сделали выбор!', })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
