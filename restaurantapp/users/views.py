from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import JsonResponse


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #user authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #user authenticated correctly
            login(request, user)

            if user.is_staff:
                #admin
                return redirect('admin_dashboard')
            else: 
                return redirect('employee_dashboard')

        else:
            return JsonResponse({'error': "Invalid Credentials"})
    
    return render(request, 'login.html')


@login_required
def admin_dashboard(request):
    if request.user.is_staff:
        return render(request, 'admin_dashboard.html')
    else:
        return redirect('employee_dashboard')
    
@login_required
def employee_dashboard(request):
    if request.user.is_staff:
        return render(request, employee_dashboard.html)
    else:
        return redirect('admin_dashboard')
    

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige al login después de cerrar sesión