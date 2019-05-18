from django.shortcuts import render
from django.http import HttpResponse

def length_vowels_and_consonants(request):
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
