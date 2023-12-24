from django.urls import path

from . import views

urlpatterns = [
    path("userLogin/", views.userLoginProcess, name="userLogin"),
    path("userReg/", views.userRegProcessing, name="userReg"),
    path("userLogout/", views.userLogout, name="userLogout"),
]