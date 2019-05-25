from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.http import HttpResponse


def to_home(request):
    return render(request, 'hw_20/home.html', context={'cars': Car.objects.all()})


def create_car(request):
    if request.method == 'GET':
        return render(request, 'hw_20/create.html', context={'form': CarForm()})
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Car.objects.create(
                brand=data.get('brand'),
                model=data.get('model'),
                color=data.get('color'),
                weight=data.get('weight'),
                owner_full_name=data.get('owner_full_name'),
                year_issue=data.get('year_issue'),
            )
            return redirect('home_url')
        else:
            return HttpResponse(f'{form.errors}')
    return HttpResponse('INVALID REQUEST METHOD')

def edit_car(request, car_id):
    pass


def delete_car(request, car_id):
    Car.objects.get(id=car_id).delete()
    return redirect('home_url')
