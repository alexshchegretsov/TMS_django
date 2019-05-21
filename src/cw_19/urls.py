from django.urls import path
from .views import *

urlpatterns = [
    path('task_5/',print_string, name='comment_add'),
]
