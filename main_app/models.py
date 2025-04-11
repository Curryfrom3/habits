from django.db import models

class Habit(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()

    def __str__(self):
        return self.name
