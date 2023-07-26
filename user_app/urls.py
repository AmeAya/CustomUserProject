from django.urls import path
from.views import *

urlpatterns = [
    path('registration', registrationView, name='registration_url'),
]
