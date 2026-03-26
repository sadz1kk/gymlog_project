from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from .models import Exercise
from .forms import ExerciseForm
from .forms import WorkoutForm

# Create your views here.

def exercise_list(request):
    workout = Workout.objects.all()
    return render(request, 'training/list.html', {'workout': workout})

def add_workout(request):
        if request.method == 'POST':
          form = WorkoutForm(request.POST)
          if form.is_valid():
                form.save()
                return redirect('exercise_list')
        else:
               form = WorkoutForm()
        return render(request, 'training/add_workout.html', {'form': form})

def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    # Pobieramy wszystkie ćwiczenia przypisane do tego konkretnego treningu
    # Jeśli w modelu Exercise masz related_name='exercises'
    exercises = workout.exercises.all() 
    
    return render(request, 'training/workout_detail.html', {
        'workout': workout,
        'exercises': exercises
    })

def delete_workout(request,pk):
     workout = Workout.objects.get(id=pk)
     workout.delete()
     return redirect('exercise_list')
     
def add_exercise(request, pk):
    workout = Workout.objects.get(id=pk)
    
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            return redirect('workout_detail', pk)
    else:
        # Tego fragmentu prawdopodobnie Ci brakuje!
        form = ExerciseForm()

    # Ta linia MUSI być wysunięta do lewej (na poziomie pierwszego if)
    return render(request, 'training/add_exercise.html', {'form': form, 'workout': workout})

def delete_exercise(request, pk):
    # Używamy get_object_or_404, żeby zamiast błędu Pythona pokazać ładne 404
    exercise = get_object_or_404(Exercise, id=pk)
    
    # Pobieramy ID treningu, zanim usuniemy ćwiczenie
    workout_id = exercise.workout.id 
    
    exercise.delete()
    
    # WRACAMY DO SZCZEGÓŁÓW TRENINGU (to jest nazwa z urls.py)
    return redirect('workout_detail', pk=workout_id)

   