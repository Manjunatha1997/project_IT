
from django.urls import path, include
from contact.views import *


urlpatterns = [
    path('us/', contact_us),
]