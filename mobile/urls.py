from django.urls import path
from mobile.views import *
app_name='14plus'
urlpatterns=[
    path('iphone/',iphone,name='iphone'),
]