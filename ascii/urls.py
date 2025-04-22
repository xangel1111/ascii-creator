from django.urls import path
from ascii import views

urlpatterns = [
    path('', views.ascii_show, name='ascii_show'),
]
