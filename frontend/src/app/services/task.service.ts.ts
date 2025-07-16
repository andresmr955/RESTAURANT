import { Injectable } from '@angular/core';
import { environment } from './../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Task } from './../models/task.model';
import { checkToken } from './../interceptors/token-interceptor';

@Injectable({
  providedIn: 'root'
})
export class TaskServiceTs {
  apiURL = environment.API_URL;
  
  constructor(
    private http: HttpClient,
  ) { }


  getTasks():Observable<Task[]> {

    return this.http.get<Task[]>(`${this.apiURL}/api/tasksapp/tasks/`, {
      context: checkToken()
    });
  }
}
