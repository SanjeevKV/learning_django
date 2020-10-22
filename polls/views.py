from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . import models
# Create your views here.
def index(request):
  question_list = models.Question.objects.order_by('-pub_date')[:5]
  #return HttpResponse(', '.join(question.question_text for question in question_list))
  #question_list = []
  return render(request, 'polls/index.html', context = {'question_list': question_list})

def detail(request, question_id):
  question = get_object_or_404(models.Question, pk = question_id)
  return render(request, 'polls/detail.html', context={'question': question, 'choices': question.choice_set.all()})

def results(request, question_id):
  return HttpResponse('Requesting results of question {qid}'.format(qid = question_id))