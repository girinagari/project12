from django.urls import path
from app1.views import *

app_name='brahmi'
urlpatterns=[ 
    path('gajala/',gajala,name='gajala'),
]