from django.contrib import admin
from django.urls import path
from .views import length_vowels_and_consonants, split_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment/', length_vowels_and_consonants),
    path('comment/split/', split_comment),
]
