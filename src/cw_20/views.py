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


def edit_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'GET':
        context = {
            'customer_id': customer_id,
            'form': CreateCustomerForm(
                initial={
                    'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'profession': customer.profession,
                    'age': customer.age,
                }
            )
        }
        return render(request, 'cw_20/edit.html', context)
    elif request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Customer.objects.filter(id=customer_id).update(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                profession=data.get('profession'),
                age=data.get('age'),
            )
            return redirect('home_url')
        else:
            return HttpResponse(form.errors)
    return HttpResponse('INVALID REQUEST METHOD')
