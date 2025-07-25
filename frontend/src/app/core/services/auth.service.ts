import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../../../environments/environment';
import { switchMap, tap } from 'rxjs/operators';
import { TokenService } from './token.service';
import { MeService } from './me.service';
import { ResponseLogin } from './../../models/auth.model';
import { CustomerUser } from './../../models/user.model';
import { BehaviorSubject, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  apiUrl = environment.API_URL;
  user = new BehaviorSubject<CustomerUser | null>(null);
  user$ = this.user.asObservable();

  constructor(
    private http: HttpClient,
    private tokenService: TokenService,
    private meService: MeService,
    private router: Router
  ) { }

  getDataUser() {
    return this.user.getValue();
  }
  setUser(user: CustomerUser | null){
    this.user.next(user)
  }
  login(email: string, password: string) {
    return this.http.post<ResponseLogin>(`${this.apiUrl}/api/auth/loginjwt/`, {
      
      email,
      password
    })
    .pipe(
      tap(response => {
        localStorage.setItem('token', response.access);
        this.tokenService.saveToken(response.access);
        this.tokenService.saveRefreshToken(response.refresh);
        
        
      })
    );
  }

  refreshToken(refreshToken: string) {
    return this.http.post<ResponseLogin>(`${this.apiUrl}/api/auth/refresh/`, {refreshToken})
    .pipe(
      tap(response => {
        this.tokenService.saveToken(response.access);
        this.tokenService.saveRefreshToken(response.refresh);
      })
    );;
  }

  register(name: string, email: string, password: string) {
    return this.http.post(`${this.apiUrl}/api/v1/auth/register`, {
      name,
      email,
      password
    });
  }

  registerAndLogin(name: string, email: string, password: string) {
    return this.register(name, email, password)
    .pipe(
      switchMap(() => this.login(email, password))
    );
  }

  isAvailable(email: string) {
    return this.http.post<{isAvailable: boolean}>(`${this.apiUrl}/api/v1/auth/is-available`, {email});
  }

  recovery(email: string) {
    return this.http.post(`${this.apiUrl}/api/v1/auth/recovery`, { email });
  }

  changePassword(token: string, newPassword: string) {
    return this.http.post(`${this.apiUrl}/api/v1/auth/change-password`, { token, newPassword });
  }

getProfile() {
  
  return this.meService.getMeProfile().pipe(
    tap(user => {
      
      this.user.next(user);
    }),
    catchError(err => {
     
      this.user.next(null);
      return of(null);
    })
  );
}


  loginAndGet(email: string, password: string) {
  return this.login(email, password).pipe(
    switchMap(() => this.getProfile()), // <- devuelve un observable

  );
}

  logout() {
    localStorage.removeItem('user');
    localStorage.removeItem('token');
    this.tokenService.removeToken();
    this.tokenService.removeRefreshToken();
    this.setUser(null);
    this.router.navigate(['/login'])
  }
}