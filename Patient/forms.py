from django import forms
from .models import Patient,Consultaiton



class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['Nom',
                'age',
                'gender',
                'adresse',
                'numéro_téléphone']
        labels={'Nom':'Nom patient',
                'age':'Age',
                'gender':'Genre',
                'adresse':'Adresse',
                'numéro_téléphone':'Numéro téléphone'}
        widgets={
            'Nom':
            forms.TextInput(attrs={'class': 'form-control w-60', 'placeholder': 'Entrez votre nom'}),
            'age':
            forms.TextInput(attrs={'class': 'form-control w-60', 'placeholder': 'Entrez âge'}),
            'gender':
            forms.Select(choices=Patient.GENDER_CHOICES, attrs={'class' : 'form-control w-60'}),
            'adresse':
            forms.TextInput(attrs={'class': 'form-control w-60', 'placeholder': 'Enterz adresse'}),
            'numéro_téléphone':
            forms.TextInput(attrs={'class': 'form-control w-60', 'placeholder': 'Enterz le numéro téléphone'}),
        }


class ConsultationForm(forms.ModelForm):
    patient=forms.ModelChoiceField(queryset=Patient.objects.all(),label="Patient")
    class Meta:
        model=Consultaiton
        fields=['patient',
                'Note',
                'date']
        labels={
            'Note':'Note',
            'date':'Date'
        }

        widgets={
            'Note':
            forms.Textarea(attrs={'class': 'form-control w-50','placeholder':'Consernant le consultation du patient'}),
            'date':
             forms.DateInput(attrs={'class': 'form-control w-50','type':'date'}),
        }