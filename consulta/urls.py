from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('consults_list/', views.consults_list, name="consults_list"),
    path('consults_add/', views.consults_add, name="consults_add"),
    path('consults_edit/<int:id>/', views.consults_edit, name="consults_edit"),
    path('consults_delete/<int:id>/', views.consults_delete, name="consults_delete"),
    path('patients_add/', views.patients_add, name='patients_add'),
    path('patients_list/', views.patients_list, name='patients_list'),
]