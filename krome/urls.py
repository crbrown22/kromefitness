from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('kromehome/', views.kromehome, name='kromehome'),
    path('about/', views.about, name='about'),
    path('conditioning/', views.conditioning, name='conditioning'),
    path('flexmob/', views.flexmob, name='flexmob'),
    path('kromereg/', views.kromereg, name='kromereg'),
    path('ksphome/', views.ksphome, name='ksphome'),
    path('mw/', views.mw, name='mw'),
    path('meals/', views.meals, name='meals'),
    path('programonline/', views.programonline, name='programonline'),
    path('shop/', views.shop, name='shop'),
    path('strength/', views.strength, name='strength'),
    path('tt/', views.tt, name='tt'),
    path('transformation/', views.transformation, name='transformation'),
    
    
]