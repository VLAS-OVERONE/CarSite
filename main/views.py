from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm


def index(request):
    return render(request, 'main/index.html')


def cars(request):
    vehicles = Vehicle.objects.order_by('title')[:10]
    return render(request, 'main/cars.html', {'title': 'АВТО', 'description': vehicles})


def registr(request):
    return render(request, 'main/registr.html')


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