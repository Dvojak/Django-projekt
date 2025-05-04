from django.urls import path
from . import views

urlpatters = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deskovky/', views.deskovka_list, name='deskovka_list'),
    path('zanry/', views.zanr_list, name='zanr_list'),
    path('rozsireni/', views.rozsireni_list, name='rozsireni_list'),
    path('deskovka/<int:pk>/', views.deskovka_detail, name='deskovka_detail'),
    path('zanr/<int:pk>/', views.zanr_detail, name='zanr_detail'),
    path('rozsireni/<int:pk>/', views.rozsireni_detail, name='rozsireni_detail'),
    path('deskovka/add/', views.deskovka_create, name='deskovka_create'),
    path('zanr/add/', views.zanr_create, name='zanr_create'),
    path('rozsireni/add/', views.rozsireni_create, name='rozsireni_create'),
    path('deskovka/<int:pk>/edit/', views.deskovka_update, name='deskovka_update'),
    path('zanr/<int:pk>/edit/', views.zanr_update, name='zanr_update'),
    path('rozsireni/<int:pk>/edit/', views.rozsireni_update, name='rozsireni_update'),
    path('deskovka/<int:pk>/delete/', views.deskovka_delete, name='deskovka_delete'),
    path('zanr/<int:pk>/delete/', views.zanr_delete, name='zanr_delete'),
    path('rozsireni/<int:pk>/delete/', views.rozsireni_delete, name='rozsireni_delete'),

]