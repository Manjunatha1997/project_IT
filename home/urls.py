from django.urls import path, include
from home.views import *


urlpatterns = [
    path('', home),
    #path('project_data/<str:name>/', project_data),

]