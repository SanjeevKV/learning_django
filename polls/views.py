from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello World! You are at the poll index.")