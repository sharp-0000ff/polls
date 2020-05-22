from django.shortcuts import render, get_object_or_404
from . import models
from django.http import HttpResponse, Http404

# Create your views here.


def index(request):
    question_list = models.Question.objects.order_by('-publish_date')[:5]
    context = {'question_list': question_list, }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question, })


def results(request, question_id):
    return HttpResponse('Вы смотрите на результаты вопроса {}'.format(question_id))


def vote(request, question_id):
    return HttpResponse('Вы голосуете по вопросу {}'.format(question_id))

