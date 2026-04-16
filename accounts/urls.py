from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(next_page="/"), name="login"),
    path('logut/', auth_views.LogoutView.as_view(next_page="/"), name="logout")
]
