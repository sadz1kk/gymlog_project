from django import forms
from .models import Exercise
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workoutname', 'duration', 'date'] 

        labels = {
            'workoutname': 'Name of workout',
            'duration': 'Duration (min)',
            'date': 'Date',
        }

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'weight', 'sets', 'reps' ]