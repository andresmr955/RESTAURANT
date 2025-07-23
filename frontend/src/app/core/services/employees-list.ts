import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../../../environments/environment';
import { CustomerUser } from './../../models/user.model';
import { Observable } from 'rxjs';
import { checkToken } from '../interceptors/token-interceptor';

@Injectable({
  providedIn: 'root'
})
export class EmployeesList {

  apiUrl = environment.API_URL

  constructor(private http: HttpClient) { }

  getAllEmployeesList(): Observable<CustomerUser[]>{
    return this.http.get<any[]>(`${this.apiUrl}/api/users/employees-actions/`,  {
          context: checkToken()
        })
  }
}
