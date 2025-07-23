import { Component } from '@angular/core';
import { EmployeesListComponent } from '../employees-list/employees-list';

@Component({
  selector: 'app-cms',
  imports: [EmployeesListComponent],
  templateUrl: './cms.html',
  styleUrl: './cms.scss'
})
export class Cms {

}
