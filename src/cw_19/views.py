from django.shortcuts import render
from django.http import HttpResponse


def print_string(request):
    if request.method == 'GET':
        return render(request, 'cw_19/task_5.html')
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        print(f'{first_name}|{last_name}|{age}|{comment}')
        return render(request, 'cw_19/task_5.html')
    return HttpResponse('Invalid method')
