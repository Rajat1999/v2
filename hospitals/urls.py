from django.urls import path
from . import views

urlpatterns = [
    
    path('hospitals/register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('map/', views.map, name='map'),
]
