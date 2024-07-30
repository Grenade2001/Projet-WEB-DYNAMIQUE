from django.urls import path
from . import  views

urlpatterns=[
    path('',views.Index,name='index'),
    path('Contact/',views.Contact,name='contact'),
       path('index/',views.Index1,name='dasbord'),
    path('Ajout_patient/',views.Ajout_patient,name='ajout_patient'),
    path('Modifier_patient/<int:F>',views.Modifier_patient,name='modifier_patient'),
    path('liste_patient/',views.Liste_patient,name='listpatient'),
    path('liste_consultation/',views.Liste_consultation,name='listconsultation'),
    path('Ajout_consultation/',views.Ajout_consultation,name='ajout_consultation'),
    path('Modifier_consultation/<int:C>',views.Modifier_consultation,name='modifier_consultation'),
    path('Consultation_patient/<int:D>',views.Consultation_patient,name='consultation_patient'),
    path('Effacer_patient/<int:E>',views.Effacer_patient,name='effacer_patient'),
    path('Effacer_consultation/<int:S>',views.Effacer_consultation,name='effacer_consultation'),
    path('admin_login/',views.Login, name='login'),
    path('logout/',views.Logout,name='logout_admin'),
]