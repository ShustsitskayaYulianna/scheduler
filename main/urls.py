from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('date', views.date),
    path('view/', views.view, name='view'),
    path('preview/', views.createDoc, name='preview'),
    path('download/', views.createDoc, name='createDoc'),
]