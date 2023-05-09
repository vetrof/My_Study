from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User, EmailVerification


# class UserLoginView(LoginView):
#     template_name = 'users/login.html'
#     form_class = UserLoginForm
#     # title = 'Store - Авторизация'


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


# class UserRegistrationView(SuccessMessageMixin, CreateView):
#     model = User
#     form_class = UserRegistrationForm
#     template_name = 'users/registration.html'
#     success_url = reverse_lazy('users:login')
#     success_message = 'Вы успешно зарегестрированы!'
#     title = 'Store - Регистрация'


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/registration.html', context)


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_summ = 0
    total_quantity = 0
    for i in baskets:
        total_summ += i.summ()
        total_quantity += i.quantity

    context = {'title': 'Store - Профиль',
               'form': form,
               'baskets': Basket.objects.filter(user=request.user),
               'total_sum': total_summ,
               'total_quantity': total_quantity,
               }

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):

        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)

        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))