import os
from django.shortcuts import render

# task 2
def three_fields_handler(request):
    if request.method == 'GET':
        return render(request, 'hw_18/task_2.html')
    if request.method == 'POST':
        data = request.POST

        with open('file.txt', 'a') as file:
            for v in data.values():
                file.write(f'{v.title()} ')
            file.write('\n')
        file = open('file.txt').readlines()

        return render(request, 'hw_18/form_task_2.html', context={'data_list': file})


# task 3
def string_list_view(request):
    if request.method == 'GET':
        file_list = open('file.txt').readlines()
        return render(request,'hw_18/task_3.html',context={'file_list': file_list})

# task 4
def clean_file(request):
    if request.method == 'GET':
        os.remove(os.path.abspath('file.txt'))
        return render(request,'hw_18/task_2.html')
