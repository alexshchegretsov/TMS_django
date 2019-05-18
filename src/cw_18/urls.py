from django.contrib import admin
from django.urls import path
from .views import length_vowels_and_consonants

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment/', length_vowels_and_consonants),
]
