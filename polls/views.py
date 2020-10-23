from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from . import models
# Create your views here.
class index(generic.ListView):
  template_name = 'polls/index.html'
  def get_queryset(self):
    return models.Question.objects.order_by('-pub_date')[:5]

class detail(generic.DetailView):
  model = models.Question
  template_name = 'polls/detail.html'

class results(generic.DetailView):
  model = models.Question
  pk_url_kwarg = 'question_id'
  template_name = 'polls/results.html'

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