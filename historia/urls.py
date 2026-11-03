from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='historia_inicio'),
    path('bosque/', views.bosque, name='historia_bosque'),
    path('torre/', views.torre, name='historia_torre'),
    path('final-bueno/', views.final_bueno, name='historia_final_bueno'),
    path('final-malo/', views.final_malo, name='historia_final_malo'),
]
