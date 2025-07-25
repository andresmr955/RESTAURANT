import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from './../../../environments/environment';
import { CustomerUser } from './../../models/user.model';
import { checkToken } from '../interceptors/token-interceptor';

@Injectable({
  providedIn: 'root'
})
export class MeService {

  apiUrl = environment.API_URL;

  constructor(private http: HttpClient) {}

  getMeProfile() {
    return this.http.get<CustomerUser>(`${this.apiUrl}/api/users/employees-actions/me/`, {
      context: checkToken(),
    })
    ;
  }
 
}