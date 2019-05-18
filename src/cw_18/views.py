from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse


def length_vowels_and_consonants(request):
    if request.method == 'GET':
        return render(request,'cw_18/comment_1.html')
    if request.method == 'POST':
        comment = request.POST.get('comm')
        vowels = 0
        consonants = 0
        n = '<br>'
        for char in comment:
            if char.isalpha():
                if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                    vowels += 1
                else:
                    consonants += 1
        return HttpResponse(f'length comment: {len(comment)}{n}vowels: {vowels}{n}consonants: {consonants}')


def split_comment(request):
    if request.method == 'GET':
        return render(request,'cw_18/split_comment.html')
    if request.method == 'POST':
        author = request.POST.get('first_name')
        list_comment = request.POST.get('comm').split('\r\n')
        modified_list_comment = [f'{line} (c){author}' for line in list_comment]
        return HttpResponse('<br>'.join(modified_list_comment))
