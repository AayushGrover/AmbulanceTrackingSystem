from django.contrib.auth.models import User, Group
from .models import Hospital, Patient, Ambulance, Trip
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'latitude', 'longitude')


class PatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Patient.objects.all())])
    dob = serializers.DateField(required=False)
    contact_number = serializers.CharField(validators=[UniqueValidator(queryset=Patient.objects.all())])

    def create_user(self, validated_data):
        patient = Patient.objects.create_user(validated_data['name'], validated_data['dob'], validated_data['contact_number'])
        return patient

    class Meta:
        model = Patient
        fields = ('id', 'name', 'dob', 'contact_number')


class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = ('number_plate', 'latitude', 'longitude', 'contact_number', 'status')