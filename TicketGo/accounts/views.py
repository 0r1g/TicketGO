from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import LoginForm, CustomUserCreationForm


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    extra_context = {'title': 'Авторизація'}


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
