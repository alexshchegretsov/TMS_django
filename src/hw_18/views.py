from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def three_fields_handler(request):
    if request.method == 'GET':
        return render(request,'hw_18/task_2.html')
    if request.method == 'POST':
        data = request.POST

        with open('file.txt','a') as file:
            for v in data.values():
                file.write(f'{v.title()} ')
            file.write('\n')
        file = open('file.txt').readlines()

        return render(request,'hw_18/form_task_2.html',context={'data_list': file})