from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    run = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    birth_date = serializers.DateField()
    gender = serializers.CharField()
    region = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()
    health_provider = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Patient(**validated_data).save()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance