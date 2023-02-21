from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register/register_user.html', {'failed_signup': True, 'register_user': form})
    else:
        form = RegisterForm()
    return render(request, 'register/register_user.html', {'register_user': form})


@login_required(login_url='/register/login_user')
def home(request):
    return render(request, 'register/home.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                logout(request)
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'register/login_user.html', {'failed_login': True, 'login_user': form})
    else:
        form = AuthenticationForm()
    return render(request, 'register/login_user.html', {'login_user': form})


@login_required(login_url='/register/login_user')
def logout_user(request):
    logout(request)
    return redirect('login_user')
