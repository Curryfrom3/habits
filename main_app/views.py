#views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Habit

# Home view
def home(request):
    return render(request, 'home.html')

# Index view - shows only the current user's habits
@login_required
def habits_index(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/index.html', {'habits': habits})

# Detail view - shows one habit
@login_required
def habits_detail(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    return render(request, 'habits/detail.html', {'habit': habit})

# Create view
class HabitCreate(LoginRequiredMixin, CreateView):
    model = Habit
    fields = ['name', 'description', 'start_date']
    template_name = 'habits/habit_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'habit_id': self.object.id})

# Update view
class HabitUpdate(LoginRequiredMixin, UpdateView):
    model = Habit
    fields = ['name', 'description', 'start_date']
    template_name = 'habits/habit_form.html'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse('detail', kwargs={'habit_id': self.object.id})

# Delete view
class HabitDelete(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'habits/habit_confirm_delete.html'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse('index')

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('index')  # Redirect to habits index
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})