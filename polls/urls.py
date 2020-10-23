from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
  path('', views.index.as_view(), name='index'),
  #Using pk as generic view expects it by default
  path('<int:pk>', views.detail.as_view(), name='detail'),
  #We can change default pk using pk_url_kwarg in generic view
  path('<int:question_id>/results', views.results.as_view(), name='results'),
  path('<int:pk>/vote', views.vote, name='vote')
]