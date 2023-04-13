from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class SignUpForm(UserCreationForm):

    name = forms.CharField(label='имя', max_length=50, required=True)
    username = forms.CharField(label='имя пользователя', max_length=50, required=True)
    email = forms.EmailField(label='электронная почта', required=True)
    phone_number = forms.RegexField(label='номер телефона', regex=r'^\+?1?\d{9,15}$')
    public_key = forms.CharField(max_length=500, widget=forms.HiddenInput(), required=False)
    password1 = forms.CharField(
        label='пароль',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='повторите пароль',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'phone_number')
