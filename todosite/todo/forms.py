from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'due_time', 'completed', 'user']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', "password2"]

class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
