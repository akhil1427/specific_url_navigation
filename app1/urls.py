from app1.views import *
from django.urls import path

app_name='sai'

urlpatterns=[

    path('praveen/',praveen,name='praveen'),
]