from django.urls import include,path
from . import views
from . import api
 
app_name='accounts'

urlpatterns = [

    #API
    path('api/patient_list/',api.patient_list, name='patient_list'),
    path('api/patient/<int:id>',api.FBV_pk_patient, name='patient'),
    
]
