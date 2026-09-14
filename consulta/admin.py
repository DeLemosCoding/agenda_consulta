from django.contrib import admin
from .models import Doctor, Pacient, Consultation

# Register your models here.

@admin.register(Doctor)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'expertise', 'CRM',)
    search_fields = ('name', 'expertise',)

@admin.register(Pacient)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'CPF', 'gender',)
    search_fields = ('name',)

@admin.register(Consultation)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'pacient', 'date',)
    list_filter = ('doctor', 'date',)
    search_fields = ('doctor', 'date',)