from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer
from datetime import datetime

class ListaDePacientes(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data["created_at"] = datetime.now()
        data["updated_at"] = datetime.now()
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            Patient(**serializer.validated_data).save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListaDePaciente(APIView):
    def get(self, request, id):
        try:
            paciente = Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(paciente)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            paciente = Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        request.data["updated_at"] = datetime.now()
        serializer = PatientSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            paciente = Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
