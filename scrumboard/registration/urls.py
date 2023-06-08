from .views import *
from django.urls import path

urlpatterns = [
    path('', index),
    path('reg/', reg),
    path('auth/', auth),

]
