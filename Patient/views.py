from django.shortcuts import render,get_object_or_404,redirect

from .models import Patient ,Consultaiton
from .forms import PatientForm,ConsultationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def Index(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

def Index1(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Ajout_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        form= PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listpatient')

    else:
        form=PatientForm()

    return render(request,'patient.html',{'form':form})

def Modifier_patient(request,F):
    if not request.user.is_staff:
        return redirect('login')
    
    patient=get_object_or_404(Patient,id=F)
    if request.method=='POST':
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
        return redirect('listpatient')
    else:
        form=PatientForm(instance=patient)
    return render(request,'modifier_patient.html',{'form':form})

def Liste_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    
    patients=Patient.objects.all()
    return render(request,'liste_patient.html',{'patients':patients})

def Liste_consultation(request):
    if not request.user.is_staff:
        return redirect('login')
    
    consultations=Consultaiton.objects.all()
    return render(request,'liste_consultation.html',{'consultations':consultations})

def Ajout_consultation(request):
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method=='POST':
        form= ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listconsultation')

    else:
        form=ConsultationForm()

    return render(request,'consultation.html',{'form':form})

def Modifier_consultation(request,C):
    if not request.user.is_staff:
        return redirect('login')
    
    consultation=get_object_or_404(Consultaiton,id=C)
    if request.method=='POST':
        form=ConsultationForm(request.POST,instance=consultation)
        if form.is_valid():
            form.save()
        return redirect('listconsultation')
    else:
        form=ConsultationForm(instance=consultation)
    return render(request,'modifier_consultation.html',{'form':form})

def Consultation_patient(request,D):
    if not request.user.is_staff:
        return redirect('login')
    
    patient=get_object_or_404(Patient,id=D)
    consultation=patient.consultations.all()
    return render(request,'consultation_patient.html',{'patient':patient,'consultation':consultation})

def Effacer_patient(request,E):
    if not request.user.is_staff:
        return redirect('login')
    
    efface_patient=Patient.objects.get(id=E)
    efface_patient.delete()
    return redirect('listpatient')

def Effacer_consultation(request,S):
    if not request.user.is_staff:
        return redirect('login')
    
    efface_consultation=Consultaiton.objects.get(id=S)
    efface_consultation.delete()
    return redirect('listconsultation')

def Login(request):
    error=" "
    if request.method== "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username= u ,password= p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"

            else:
                error= "yes"
        
        except:
          error="yes"
    d= {'error':error}
    return render(request,'login.html',d)

def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('index')


      
    


 
            
          


