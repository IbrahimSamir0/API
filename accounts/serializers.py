from rest_framework import  serializers
from .models import Doctor, Patient, Todolist

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['email','firstname','lastname','phone','image']
        

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['doctorid','email','firstname','lastname','phone','image']

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = '__all__'
