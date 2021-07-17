from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('adt', views.cars),
    path('create', views.create),
    path('Str2', views.Str2),
    path('Str3', views.Str3),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout_view, name='logout'),
]
