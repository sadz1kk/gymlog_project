from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('addworkout/', views.add_workout, name='add_workout'),
    path('workoutdetail/<int:pk>', views.workout_detail, name='workout_detail'),
    path('deleteworkout/<int:pk>', views.delete_workout, name='delete_workout'),
    path('addexercise/<int:pk>', views.add_exercise, name='add_exercise'),
    path('deleteexercise/<int:pk>/', views.delete_exercise, name='delete_exercise'),
]