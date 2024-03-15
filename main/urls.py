from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('logout', views.logout, name = 'logout'),
    path('emptasks', views.emptasks, name = 'emptasks'),
]