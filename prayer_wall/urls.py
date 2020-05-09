from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='prayer-wall-home'),
    path('about/', views.about, name='prayer-wall-about'),

]