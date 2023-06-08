from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', reg),
    #path('registration/', reg),

]
