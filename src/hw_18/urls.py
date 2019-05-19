from django.contrib import admin
from django.urls import path
from .views import three_fields_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_2/', three_fields_handler),
]
