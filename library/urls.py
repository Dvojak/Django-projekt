from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deskovky/', views.DeskovkaListView.as_view(), name='deskovka_list'),
    path('zanry/', views.ZanrListView.as_view(), name='zanr_list'),
    path('rozsireni/', views.RozsireniListView.as_view(), name='rozsireni_list'),
    path('deskovka/<int:pk>/', views.DeskovkaDetailView.as_view(), name='deskovka_detail'),
    path('zanr/<int:pk>/', views.zanr_detail, name='zanr_detail'),
    path('rozsireni/<int:pk>/', views.rozsireni_detail, name='rozsireni_detail'),
    path('deskovka/add/', views.create_deskovka, name='deskovka_create'),
    path('zanr/add/', views.zanr_create, name='zanr_create'),
    path('rozsireni/add/', views.rozsireni_create, name='rozsireni_create'),
    path('deskovka/<int:pk>/edit/', views.upadate_deskovka, name='deskovka_update'),
    path('rozsireni/<int:pk>/edit/', views.rozsireni_update, name='rozsireni_update'),
    path('deskovka/<int:pk>/delete/', views.delete_deskovka, name='deskovka_delete'),
    path('zanr/<int:pk>/delete/', views.zanr_delete, name='zanr_delete'),
    path('rozsireni/<int:pk>/delete/', views.rozsireni_delete, name='rozsireni_delete'),
    path('tvurci/', views.tvurci_list, name='tvurci_list'),
    path('tvurci/add/', views.tvurci_create, name='tvurci_create'),
    path('tvurci/<int:pk>/', views.tvurci_detail, name='tvurci_detail'),
    path('tvurci/<int:pk>/edit/', views.tvurci_update, name='tvurci_update'),
    path('tvurci/<int:pk>/delete/', views.tvurci_delete, name='tvurci_delete'),
    path('vydavatelstvi/', views.vydavatelstvi_list, name='vydavatelstvi_list'),
    path('vydavatelstvi/<int:pk>/', views.vydavatelstvi_detail, name='vydavatelstvi_detail'),
    path('vydavatelstvi/add/', views.vydavatelstvi_create, name='vydavatelstvi_create'),
    path('vydavatelstvi/<int:pk>/edit/', views.vydavatelstvi_update, name='vydavatelstvi_update'),
    path('vydavatelstvi/<int:pk>/delete/', views.vydavatelstvi_delete, name='vydavatelstvi_delete'),
    path('deskovka/<int:hra_id>/hodnoceni/', views.add_change_review, name='hodnoceni_add'),
    path('deskovka/<int:hra_id>/hodnoceni/smazat/', views.review_delete, name='hodnoceni_delete'),
    path('deskovka/<int:hra_id>/hodnoceni/vse/', views.review_deskovky, name='hodnoceni_list'),









    

]