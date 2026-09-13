from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    CRM = models.CharField(max_length=20, unique=True, verbose_name="CRM")
    gender = models.CharField(max_length=10, choices=[("M", "Masculino"), ("F", "Feminino")], verbose_name="Gênero")
    expertise = models.CharField(max_length=100, verbose_name="Especialidade")
    rating = models.DecimalField(max_digits = 3, decimal_places = 2, validators = [MinValueValidator(0), MaxValueValidator(5)], verbose_name ="Classificação")
    place = models.CharField(max_length=100, verbose_name="Local da Consulta")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Preço da Consulta")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Pacients(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    CPF = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    gender = models.CharField(max_length=10, choices=[("M", "Masculino"), ("F", "Feminino")])
    health_insurance = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Consultation(models.Model):
    pacient = models.ForeignKey(Pacients, on_delete=models.CASCADE, verbose_name="Paciente")
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name="Médico")
    date = models.DateTimeField(verbose_name="Data da Consulta")

    def __str__(self):
        return f"{self.pacient} - {self.doctor} - {self.date}"