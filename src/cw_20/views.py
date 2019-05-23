from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'cw_20/home_page.html')
