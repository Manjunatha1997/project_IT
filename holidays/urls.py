from django.urls import path, include
from holidays.views import *


urlpatterns = [
    path('', holidays),
    path('email/', email),
]