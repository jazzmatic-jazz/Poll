from django.db import models
from django.utils import timezone
import datetime
from users.models import CustomUser

class Question(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True)
    question = models.CharField(max_length=200)
    pub_quest = models.DateTimeField('Date Published', auto_now_add=True)

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_quest >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
    