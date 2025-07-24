import { Component, signal } from '@angular/core';
import { CustomerUser } from '../../../../models/user.model';
import { EmployeesListService } from '../../../../core/services/employees-list.service';
import { CommonModule } from '@angular/common';
import { Aside } from '../../components/aside/aside';

import { RouterModule } from '@angular/router';
import { Navbar } from '../../components/navbar/navbar';

@Component({
  selector: 'app-employees-list',
  imports: [CommonModule, Aside, RouterModule, Navbar],
  templateUrl: './employees-list.html',
  styleUrl: './employees-list.scss'
})
export class EmployeesListComponent {
    employees = signal<CustomerUser[]>([]);
    

    loading = true;

    constructor(

      private employeeListService: EmployeesListService){}

    ngOnInit(){
      console.log('ngOnInit ejecutado');
      this.loadEmployees();
    }


  loadEmployees(){
    this.employeeListService.getAllEmployeesList().subscribe({
        next: (data: CustomerUser[]) => { this.employees.set(data);
          console.log(this.employees)
          this.loading = false;
        }, 
        error: (err: any) => {
          console.log('Error loading employees', err)
          this.loading = false;
        }
      })
    } 

}