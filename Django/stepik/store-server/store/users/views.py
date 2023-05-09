from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User, EmailVerification


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!!!!!!!!!!'
    title = 'Store - Регистрация'
    # def get_context_data(self, **kwargs):
    #     context = super(UserRegistrationView, self).get_context_data()
        # context['title'] = 'Store - Регистрация'
        # return context

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Регистрация успешна!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)


# class UserProfileView(TitleMixin, UpdateView):
#     model = User
#     form_class = UserProfileForm
#     template_name = 'users/profile.html'
#     title = 'Store - Личный кабинет'
#
#     def get_success_url(self):
#         return reverse_lazy('users:profile', args=(self.object.id,))


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
    # корзину передаем через контекст менеджер глобально
    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileView , self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.object)
    #     return context
# @login_required()
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     context = {'title': 'Store - Профиль',
#                'form': form,
#                'baskets': Basket.objects.filter(user=request.user),
#                }
#
#     return render(request, 'users/profile.html', context)


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