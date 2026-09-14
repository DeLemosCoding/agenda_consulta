from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation
        fields = ['doctor', 'pacient', 'date']

        widgets = {
            'doctor': forms.Select(
                attrs = {'class': 'form-select'}
            ),
            'pacient': forms.Select(
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