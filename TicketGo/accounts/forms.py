from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логін',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Обов'язково вкажіть діючу адресу електронної пошти.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
