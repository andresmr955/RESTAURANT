# attendance/serializers.py

from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    total_hours = serializers.ReadOnlyField()
    assigned_employee_id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    login_start = serializers.DateTimeField(format="%d/%m/%Y %H:%M", allow_null=True)
    login_end = serializers.DateTimeField(format="%d/%m/%Y %H:%M", allow_null=True)


    class Meta:
        model = Attendance
        fields = ['id', 'assigned_employee_id', 'login_start', 'login_end', 'total_hours']

        read_only_fields = ['id', 'date_login']

    # Optional validations
    def validate(self, data):
        login_start = data.get('login_start')
        login_end = data.get('login_end')
        if login_start and login_end and login_end <= login_start:
            raise serializers.ValidationError("The end time must be later than the start time.")
        return data
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(f"login_end value: {instance.login_end}")  # para debug
        if not instance.login_end:
            data.pop('login_end', None)
        return data