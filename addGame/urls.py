from django.urls import path

from . import views

urlpatterns = [
    path("addingGame/", views.index, name="addingGame"),
    path("addGameProcessing/", views.addGameProcessing, name="addGameProcessing"),
]