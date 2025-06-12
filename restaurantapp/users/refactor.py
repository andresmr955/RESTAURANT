
from app_name.models import Patient
from .serializers import PatientSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()