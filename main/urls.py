from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('adt', views.cars),
    path('registr', views.registr),
    path('create', views.create),
    path('Str2', views.Str2),
    path('Str3', views.Str3),
]
