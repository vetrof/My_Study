from django.contrib.auth.forms import UserChangeForm
from django import forms

from users.models import User


class CabinetForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4", 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control py-4", 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')