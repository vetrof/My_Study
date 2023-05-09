from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Логин"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Пароль"
    }))


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите фамилию"}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': "например: ivan86"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите адрес эл. почты"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': "Подтвердите пароль"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        # expiration = now() + timedelta(hours=48)
        # record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        # record.send_verification_email()
        return user
