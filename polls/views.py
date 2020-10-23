from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import models
# Create your views here.
def index(request):
  question_list = models.Question.objects.order_by('-pub_date')[:5]
  #return HttpResponse(', '.join(question.question_text for question in question_list))
  #question_list = []
  return render(request, 'polls/index.html', context = {'question_list': question_list})

def detail(request, question_id):
  question = get_object_or_404(models.Question, pk = question_id)
  return render(request, 'polls/detail.html', context={'question': question})

def results(request, question_id):
  question = get_object_or_404(models.Question, id = question_id)
  return render(request, 'polls/results.html', context={'question': question})

def vote(request, pk):
  question = get_object_or_404(models.Question, id = pk)
  try:
    selected_choice = question.choice_set.get(id = request.POST['choice'])
  except (KeyError, models.Choice.DoesNotExist):
    error_text = "You didn't select a choice"
    return render(request, 'polls/detail.html', context={'question': question, 'error_text':error_text})

  selected_choice.votes += 1
  selected_choice.save()
  return HttpResponseRedirect(reverse('polls:results',args=(pk,)))