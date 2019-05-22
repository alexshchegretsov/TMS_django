from django.urls import path
from .views import *

urlpatterns = [
    path('task_5/',validator, name='comment'),
]
