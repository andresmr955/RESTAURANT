import { Component } from '@angular/core';
import { CustomerUser } from '../../../../models/user.model';
import { EmployeesListService } from '../../../../core/services/employees-list.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-employees-list',
  imports: [CommonModule],
  templateUrl: './employees-list.html',
  styleUrl: './employees-list.scss'
})
export class EmployeesListComponent {
  employees: CustomerUser[] = [];
  loading = true;

  constructor(private employeeListService: EmployeesListService){}

  ngOnInit():void{
    this.employeeListService.getAllEmployeesList()
    .subscribe({
      next: (data) => {
        console.log(data)
        this.employees = data;
        console.log(this.employees)
        this.loading = false;
      }, 
      error: (err) => {
        console.log('Error loading employees', err)
        this.loading = false;
      }
    })
  }
}
