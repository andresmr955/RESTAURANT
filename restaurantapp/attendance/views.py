from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Attendance

# Create your views here.

######API

from rest_framework.views import APIView

from rest_framework.response import Response



class HelloWorld(APIView):

    def get(self, request):

        return Response({"message": "¡Hola desde Django!"})


######################

@csrf_exempt
def start_attendance(request):
    if request.method == 'POST':
        # Lógica para registrar la hora de entrada
        print("¡Punch In recibido!")
        # (p. ej., Attendance.objects.create())
        return JsonResponse({'status': 'started', 'timestamp': timezone.now().isoformat()})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def stop_attendance(request):
    if request.method == 'POST':
        # Lógica para registrar la hora de salida
        # y calcular la duración si lo deseas
        return JsonResponse({'status': 'stopped'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def attendance_page(request):
    return render(request, 'attendance_page.html')