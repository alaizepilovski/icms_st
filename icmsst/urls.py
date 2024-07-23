from django.urls import path, include
from icmsst import views

urlpatterns = [
    path('icms_st', views.home, name="it_home"),
]
