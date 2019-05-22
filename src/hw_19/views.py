from django.shortcuts import render
from django.http import HttpResponse
from .forms import TicketHandler


def flight_tickets_handler(request):
    if request.method == 'GET':
        context = {'form': TicketHandler()}
        return render(request, 'hw_19/flight_tickets_form.html', context)

    elif request.method == 'POST':
        form = TicketHandler(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            from_where = data['from_where']
            to_where = data['to_where']
            date = data['date']
            people_amount = data['how_many_people']
            cost = people_amount * 100 if people_amount == 1 else people_amount * 100 * 2
            return render(request, 'hw_19/cost.html', context={
                'cost': cost,
                'date': date,
                'from_where': from_where,
                'to_where': to_where,
            })
        else:
            return HttpResponse(form.errors)

    return HttpResponse('INVALID REQUEST METHOD')
