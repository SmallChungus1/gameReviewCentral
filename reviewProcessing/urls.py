from django.urls import path

from . import views

urlpatterns = [
    path('addComment/', views.addComment, name='addComment'),
    path('delComment/', views.delUserComment, name='delComment'),
]