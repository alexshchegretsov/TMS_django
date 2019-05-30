from django.urls import path
from .views import (
    to_home,
    create_car,
    delete_car,
    edit_car,
)

urlpatterns = [
    path('', to_home, name='home_url'),
    path('create/', create_car, name='create_car_url'),
    path('edit/<int:car_id>/', edit_car, name='edit_car_url'),
    path('delete/<int:car_id>/', delete_car, name='delete_car_url'),

]
