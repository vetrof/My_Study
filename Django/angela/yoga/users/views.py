from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from users.form import LoginForm, UserRegistrationForm
from users.models import User


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы, успешно зарегистрированы!'





