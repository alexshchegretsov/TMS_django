from django.shortcuts import render
from django.http import HttpResponse
from .forms import WriteNewPost


def validator(request):
    if request.method == 'GET':
        context = {'form': WriteNewPost()}
        return render(request, 'cw_19/task_5.html', context)
    elif request.method == 'POST':
        form = WriteNewPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            age = data.get('age')
            comment = data.get('comment')
            print(f'{first_name}|{last_name}|{age}|{comment}')
            context = {'form': WriteNewPost()}
            return render(request, 'cw_19/task_5.html', context)
        else:
            errors = form.errors
            return HttpResponse(errors)
    return HttpResponse('Invalid method')
