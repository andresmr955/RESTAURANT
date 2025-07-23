import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../../../environments/environment';
import { CustomerUser } from './../../models/user.model';

@Injectable({
  providedIn: 'root'
})
export class EmployeesList {

  apiUrl = environment.API_URL

  constructor(private http: HttpClient) { }

  
}
