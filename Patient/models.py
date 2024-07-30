from django.db import models

# Create your models here.


class Patient(models.Model):
    GENDER_CHOICES =[
        ('M','Masculin'),
        ('F','Féminin'),
    ]
    Nom=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    adresse=models.CharField(max_length=50)
    numéro_téléphone=models.IntegerField()

    def __str__(self) :
        return self.Nom
    
    def get_consultation(self):
        return self.consultation_set.all()
    
class Consultaiton(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='consultations')
    Note=models.TextField()
    date=models.DateField()

    def __str__(self):
        return f"{self.patient.Nom} - {self.date}"
