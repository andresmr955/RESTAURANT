from django.urls import path
from .views import (
    EmployeeCreateView, 
    EmployeeList, 

    EmployeeListCreateAPI, 
    EmployeeDetailUpdateAPI
    )


app_name = 'users'

urlpatterns = [
   
   
        #URLS TO PROVE MY MODELS
    path('add-employee/', EmployeeCreateView.as_view(), name="add-employee"),
    path('employee-list/', EmployeeList.as_view(), name="employee_list" ),
    


    ##APIS FOR MY FRONTEND
  
    
    path("employees/", EmployeeListCreateAPI.as_view(), name="employees_api"),
    # http://127.0.0.1:8000/api/auth/employees/
    path('employees/<int:pk>/', EmployeeDetailUpdateAPI.as_view(), name='employee-detail-update')
    # http://127.0.0.1:8000/api/auth/employees/<int:id>/

  
]