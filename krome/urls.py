from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('kromehome/', views.kromehome, name='kromehome'),
    path('about/', views.about, name='about'),
    path('conditioning/', views.conditioning, name='conditioning'),
    path('flexmob/', views.flexmob, name='flexmob'),
    path('kromereg/', views.kromereg, name='kromereg'),
    path('kfmembers/', views.kfmembers, name='kfmembers'),
    path('kspmembers/', views.kspmembers, name='kspmembers'),
    path('ksp6week1/intro6wk/', views.intro6wk, name='intro6wk'),
    path('ksp6week1/kspchallenge/', views.kspchallenge, name='kspchallenge'),
    path('ksphome/', views.ksphome, name='ksphome'),
    path('kfprograms/', views.kfprograms, name='kfprograms'),
    path('kfmemprog/', views.kfmemprog, name='kfmemprog'),
    path('kspmemprog/', views.kspmemprog, name='kspmemprog'),
    path('mw/', views.mw, name='mw'),
    path('meals/', views.meals, name='meals'),
    path('programonline/', views.programonline, name='programonline'),
    path('shop/', views.shop, name='shop'),
    path('kfmemshop/', views.kfmemshop, name='kfmemshop'),
    path('kspshop/', views.kspshop, name='kspshop'),
    path('strength/', views.strength, name='strength'),
    path('tt/', views.tt, name='tt'),
    path('challenges/', views.challenges, name='challenges'),
    path('transformation/', views.transformation, name='transformation'),
    path('ksp6week1/monday/', views.monday, name='monday'),
    path('ksp6week1/tuesday/', views.tuesday, name='tuesday'),
    path('ksp6week1/wednesday/', views.wednesday, name='wednesday'),
    path('ksp6week1/thursday/', views.thursday, name='thursday'),
    path('ksp6week1/friday/', views.friday, name='friday'),
    
    
]