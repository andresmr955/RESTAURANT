# attendance/serializers.py

from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'assigned_employee', 'login_start', 'login_end']

        read_only_fields = ['id', 'assigned_employee']

    # Validaciones opcionales
    def validate(self, data):
        if data['end'] <= data['start']:
            raise serializers.ValidationError("La hora de fin debe ser posterior a la hora de inicio.")
        return data
