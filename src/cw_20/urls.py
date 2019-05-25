from django.urls import path
from .views import *

urlpatterns = [
    path('home/', to_home_page, name='home_url'),
    path('add/', create_customer, name='create_customer_url'),
    path('remove/<int: customer_id>/', remove_customer, name='remove_customer_url'),
    # path('edit/<int: customer_id>', edit_customer, name='edit_customer_url'),
]

