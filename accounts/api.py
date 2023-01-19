from .models import Patient, Doctor, Todolist
from .serializers import DoctorSerializer , PatientSerializer , TodolistSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics , status, filters


@api_view(['GET','POST'])
def patient_list(request):
    # GET
    if request.method == 'GET':    
        all_patient= Patient.objects.all()
        all_patient_data = PatientSerializer(all_patient, many=True)
        return Response(all_patient_data.data)
    #POST
    elif request.method == 'POST':
        all_patient= Patient.objects.all()
        all_patient_data = PatientSerializer(all_patient, many=True)
        patient_data =PatientSerializer(data= request.data)
        if (patient_data.is_valid()):
            patient_data.save()
            return Response(all_patient_data.data,status= status.HTTP_201_CREATED)
        return Response(patient_data.data,status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def FBV_pk_patient(request,id):
    try:
        patient = Patient.objects.get(id = id)
    except Patient.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET':    
        patient_data = PatientSerializer(patient)
        return Response(patient_data.data)
    
    #PUT
    elif request.method == 'PUT':
        patient_data =PatientSerializer(patient,data= request.data)
        if (patient_data.is_valid()):
            patient_data.save()
            return Response(patient_data.data)
        return Response(Patient.errors,status= status.HTTP_400_BAD_REQUEST)
    
    # #DELETE
    # elif request.method == 'DELETE':    
    #     patient.delete()
    #     return Response(status= status.HTTP_204_NO_CONTENT )
