from django.contrib import admin
from .models import Doctor, Patient, Consultation

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'expertise',
        'CRM',
        'place',
        'price',
        'rating',
    )

    search_fields = (
        'name',
        'expertise',
        'CRM',
    )

    list_filter = (
        'expertise',
        'gender',
    )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'CPF',
        'gender',
        'health_insurance',
    )

    search_fields = (
        'name',
        'CPF',
    )

    list_filter = (
        'gender',
        'health_insurance',
    )

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'doctor',
        'date',
    )

    list_filter = (
        'doctor',
        'date',
    )

    search_fields = (
        'patient__name',
        'doctor__name',
    )

    ordering = (
        'date',
    )