from django.urls import path, include
from timer.views import *


urlpatterns = [
    path('select_dates/', select_dates, name='date'),
    #path('timesheet/', timesheet),
    path('approve_timesheet/', approve_timesheet),
    path('submit/', submit),
]