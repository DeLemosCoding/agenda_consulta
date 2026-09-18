from django import forms
from .models import Consultation, Patient

class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation
        fields = ['doctor', 'patient', 'date']

        labels = {
            'doctor': 'Médico',
            'patient': 'Paciente',
            'date': 'Data e horário',
        }

        widgets = {
            'doctor': forms.Select(
                attrs = {'class': 'form-select'}
            ),
            'patient': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        doctor = cleaned_data.get('doctor')
        date = cleaned_data.get('date')

        if doctor and date:
            consulta_existente = Consultation.objects.filter(
                doctor=doctor,
                date=date
            ).exclude(
                pk=self.instance.pk
            ).exists()

            if consulta_existente:
                raise forms.ValidationError('Este médico já possui uma consulta marcada neste horário.')

        return cleaned_data

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
            'name',
            'birth_date',
            'CPF',
            'gender',
            'health_insurance',
        ]

        labels = {
            'name': 'Nome',
            'birth_date': 'Data de Nascimento',
            'CPF': 'CPF',
            'gender': 'Gênero',
            'health_insurance': 'Convênio Médico',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome completo'
                }
            ),

            'birth_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'CPF': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '000.000.000-00',
                    'maxlength': '14'
                }
            ),

            'gender': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'health_insurance': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Convênio médico (opcional)'
                }
            ),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data['CPF']

        cpf = cpf.replace('.', '').replace('-', '').strip()

        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError('Digite um CPF válido no formato 000.000.000-00.')
            
        return cpf