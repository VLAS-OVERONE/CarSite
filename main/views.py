from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Vehicle
from .forms import VehicleForm, LoginForm





def index(request):
    return render(request, 'main/index.html')


def cars(request):
    vehicles = Vehicle.objects.order_by('id')[:10] # Можно 'title'
    return render(request, 'main/cars.html', {'title': 'АВТО', 'description': vehicles})


def create(request):
    error = ''
    if request.method == 'POST':
        form  = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/adt")
        else:
            error = 'Проверьте заполненные данные'

    form = VehicleForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def Str2(request):
    return render(request, 'main/Str2.html')


def Str3(request):
    return render(request, 'main/Str3.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Несуществующий аккаунт. Попробуйте снова', status=403)
            else:
                return redirect("/signup")
    else:
        form = LoginForm()
    return render(request, 'main/signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')