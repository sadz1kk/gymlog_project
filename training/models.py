from django.db import models

# Create your models here.

class Workout(models.Model):
    workoutname = models.CharField(max_length=100)

    date = models.DateField()

    duration = models.IntegerField(help_text="In Minutes")

class Exercise(models.Model):
    name = models.CharField(max_length=100)

    weight = models.DecimalField(max_digits=5, decimal_places=2)

    sets = models.IntegerField()

    reps = models.IntegerField()

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')



def __str__(self):
        return f"{self.name} - {self.date}"