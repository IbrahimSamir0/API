from django.db import models

# Create your models here.

class Doctor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    firstname = models.CharField(db_column='firstName', max_length=10)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=10)  # Field name made lowercase.
    phone = models.CharField(max_length=15)
    image = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'doctor'


class Patient(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctorID')  # Field name made lowercase.
    email = models.CharField(max_length=255)
    firstname = models.CharField(db_column='firstName', max_length=10)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=10)  # Field name made lowercase.
    phone = models.CharField(max_length=15)
    image = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'patient'


class Todolist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctorID')  # Field name made lowercase.
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'todolist'
