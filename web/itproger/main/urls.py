from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='top'),
    path('register', views.reg, name='reg'),
    path('authorization', views.auto, name='auto'),
    path('about', views.about, name='about')
]