from django.shortcuts import render, redirect
from .forms import CreateCustomerForm
from .models import Customer
from django.http import HttpResponse


# Create your views here.
def to_home_page(request):
    return render(request, 'cw_20/home_page.html', context={'customers': Customer.objects.all()})


def create_customer(request):
    if request.method == 'GET':
        return render(request, 'cw_20/add.html', context={'form': CreateCustomerForm()})
    elif request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # create new object
            Customer.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                profession=data.get('profession'),
                age=data.get('age'),
            )
            return redirect('home_url')
        else:
            return HttpResponse(form.errors)

    return HttpResponse('INVALID REQUEST METHOD')


def remove_customer(request, customer_id):
    Customer.objects.get(id=customer_id).delete()
    return redirect('home_url')


