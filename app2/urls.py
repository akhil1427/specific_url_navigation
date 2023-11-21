from app2.views import *
from django.urls import path

app_name='akhil'

urlpatterns=[

    path('media/',media,name='media')
]