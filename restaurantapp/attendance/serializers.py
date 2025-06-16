# attendance/serializers.py

from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    total_hours = serializers.ReadOnlyField()
    class Meta:
        model = Attendance
        fields = ['id', 'assigned_employee', 'login_start', 'login_end', 'total_hours']

        read_only_fields = ['id', 'assigned_employee']

    # Optional validations
    def validate(self, data):
        if data['end'] <= data['start']:
            raise serializers.ValidationError("The end time must be later than the start time.")
        return data
