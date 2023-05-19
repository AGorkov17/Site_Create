from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='top'),
    path('authorization', views.auto, name='auto'),
    path('create', views.create, name='create')
]