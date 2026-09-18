from django import forms
from .models import Consultation

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
            raise forms.ValidationError(
                'Este médico já possui uma consulta marcada neste horário.'
            )

    return cleaned_data