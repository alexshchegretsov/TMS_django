from django.urls import path, include
from .views import *

urlpatterns = [
    path('tickets/', flight_tickets_handler,name='tickets_url' ),

]
