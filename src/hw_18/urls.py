from django.contrib import admin
from django.urls import path
from .views import (
    three_fields_handler,
    string_list_view,
    clean_file
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_2/', three_fields_handler),
    path('task_3/', string_list_view),
    path('task_4/', clean_file),
]
