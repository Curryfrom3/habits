 # main_app/urls.py
from django.urls import path
from . import views
from .views import HabitUpdate, HabitDelete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth routes
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Habit routes
    path('habits/', views.habits_index, name='index'),
    path('habits/<int:habit_id>/', views.habits_detail, name='detail'),
    path('habits/create/', views.HabitCreate.as_view(), name='habit_create'),
    path('habits/<int:pk>/update/', HabitUpdate.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', HabitDelete.as_view(), name='habit_delete'),
]
