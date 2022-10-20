from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.conf import settings

from . import forms


# Create your views here.
def register_page(request):
    form = forms.RegisterForm()

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    return render(request, 'custom_auth/register.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


class LoginPageView(View):
    template = 'custom_auth/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour {user.username}! Vous êtes connecté.'
        message = 'Identifiants invalides'
        return render(request, self.template, context={'form': form, 'message': message})
