from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    start_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'habit_id': self.id})

    def __str__(self):
        return self.name
