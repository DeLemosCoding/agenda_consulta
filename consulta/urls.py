from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('doctors_list/', views.doctors_list, name='doctors_list'),
    path('doctors_add/', views.doctors_add, name='doctors_add'),
    path('doctors_edit/<int:id>/', views.doctors_edit, name='doctors_edit'),
    path('doctors_delete/<int:id>/', views.doctors_delete, name='doctors_delete'),
    path('patients_list/', views.patients_list, name='patients_list'),
    path('patients_add/', views.patients_add, name='patients_add'),
    path('patients_edit/<int:id>/', views.patients_edit, name='patients_edit'),
    path('patients_delete/<int:id>/', views.patients_delete, name='patients_delete'),
    path('consults_list/', views.consults_list, name="consults_list"),
    path('consults_add/', views.consults_add, name="consults_add"),
    path('consults_edit/<int:id>/', views.consults_edit, name="consults_edit"),
    path('consults_delete/<int:id>/', views.consults_delete, name="consults_delete"),
]

handler403 = 'consultas.views.permission_denied'