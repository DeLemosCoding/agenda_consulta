from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    CRM = models.CharField(max_length=20, unique=True, verbose_name="CRM")
    gender = models.CharField(max_length=10, choices=[("M", "Masculino"), ("F", "Feminino")], verbose_name="Gênero")
    expertise = models.CharField(max_length=100, verbose_name="Especialidade")
    rating = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0, validators = [MinValueValidator(0), MaxValueValidator(5)], verbose_name ="Classificação")
    place = models.CharField(max_length=100, verbose_name="Local da Consulta")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Preço da Consulta")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Patient(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    CPF = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    gender = models.CharField(max_length=10, choices=[("M", "Masculino"), ("F", "Feminino")], verbose_name="Gênero")
    health_insurance = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Médico")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    date = models.DateTimeField(verbose_name="Data da Consulta")

    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.date}"

    class Meta:
        constraints = [models.UniqueConstraint(fields=['doctor', 'date'], name='unique_doctor_date')]