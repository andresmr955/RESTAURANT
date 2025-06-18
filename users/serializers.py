from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import CustomerUser
from rest_framework import serializers
from tasks.serializers import TaskSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    tasks_completed_count = serializers.SerializerMethodField()

    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = CustomerUser
        fields = [  
                    'role',
                    'username',
                    'email',
                    'phone_number',
                    'avatar',
                    'date_birth',
                    'address',
                    'notifications_enabled',
                    'date_joined_restaurant',
                    'average_task_completed',
                    'tasks',
                    'tasks_completed_count',
                ]

    def validate_email(self, value):
        if "@email.com" in value:
            return value
        raise serializers.ValidationError("The email should include @email.com")

    def validate(self, attrs):
        notifications_enabled = attrs.get('notifications_enabled', getattr(self.instance, 'notifications_enabled', False))
        phone_number = attrs.get('phone_number', getattr(self.instance, 'phone_number', '') or '')

        phone_number = str(phone_number)

        if notifications_enabled:
            if not phone_number.isdigit():
                raise serializers.ValidationError("The number should ony contain numbers.")
            if len(phone_number) < 10:
                raise serializers.ValidationError("The number should contain at least 10 numbers if notifications are active.")
        
        return attrs
        
    def get_tasks_completed_count(self, obj):
        return obj.tasks.filter(status='completed').count()

class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [  'email',
                    'role',
                    'phone_number',
                    'avatar',
                    'date_birth',
                    'address',
                    'notifications_enabled',
                    'date_joined_restaurant',
                    'average_task_completed']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Use create_user if you have a method that handles password hashing
        validated_data['username'] = validated_data['email'].split('@')[0]

        user = CustomerUser.objects.create_user(**validated_data)
        return user

    def validate_email(self, value):
        if "@email.com" in value:
            return value
        raise serializers.ValidationError("The email should include @email.com")

    def validate(self, attrs):
            notifications_enabled = attrs.get('notifications_enabled', getattr(self.instance, 'notifications_enabled', False))
            phone_number = attrs.get('phone_number', getattr(self.instance, 'phone_number', '') or '')

            phone_number = str(phone_number)

            if notifications_enabled:
                if not phone_number.isdigit():
                    raise serializers.ValidationError("The number should ony contain numbers.")
                if len(phone_number) < 10:
                    raise serializers.ValidationError("The number should contain at least 10 numbers if notifications are active.")
            
            return attrs



