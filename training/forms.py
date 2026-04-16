from django import forms
from .models import Exercise
from .models import Workout

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100, label = 'Name')
    email = forms.CharField(label = 'E-mail')
    subject = forms.CharField(max_length = 200, label='Message subject')
    content = forms.CharField(
        widget = forms.Textarea,
        label = 'Messege content'
    )
   

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

