from django.db import models

# Create your models here.
class Question(models.Model):
  question_text = models.TextField(max_length=200)
  pub_date = models.DateTimeField("Created date time")

  def __str__(self):
    return self.question_text

class Choice(models.Model):
  def __str__(self):
    return self.choice_text
  question = models.ForeignKey(Question,on_delete=models.CASCADE)
  choice_text = models.TextField(max_length=200)
  votes = models.IntegerField(default=0)


