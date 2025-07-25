import { Inject, Injectable, PLATFORM_ID } from '@angular/core';
import { AuthService } from './auth.service';
import { isPlatformBrowser } from '@angular/common';
import { Observable, of, filter, take } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class SessionService {

  constructor(
    private authService: AuthService,
    private router: Router,
    @Inject(PLATFORM_ID) private platformId: Object
  ) {
    
   }

   initializeSessionSync(): void {
    if(isPlatformBrowser(this.platformId)){
      const userJson = localStorage.getItem('user')
      if (userJson ){
        const user = JSON.parse(userJson);
        this.authService.setUser(user)
      }

      window.addEventListener('storage', (event) => {
      if (event.key === 'token' && event.newValue === null){
        this.authService.logout()
      }

      if (event.key === 'token' && event.newValue !== null) {
        this.loadSessionFromStorage();
      }

      // Si se actualizó el user manualmente
      if (event.key === 'user' && event.newValue) {
        console.log('se actualizo')
        const user = JSON.parse(event.newValue);
        this.authService.setUser(user);
      }
    });
    }
   }
   loadSessionFromStorage(): Observable<any>{
    console.log('[Session] Revisando token en otra pestaña...');
    if (isPlatformBrowser(this.platformId)) {
    const token = localStorage.getItem('token');
    if(token){
       console.log('[Session] Hay token, obteniendo perfil...');
      this.authService.getProfile().subscribe({
        next: (user) => { 
          console.log('[Session] Usuario recuperado:', user);
          this.authService.setUser(user)},
        error:() => {
          this.authService.logout()
        }
      })
    }

    }return of(null);
  }

  redirectToDashboard(){
    // Redirige si ya hay un usuario autenticado
  this.authService.user$.pipe(
    filter(user => !!user), // Solo cuando haya un usuario
    take(1)  // Solo la primera vez que el usuario está disponible
  ).subscribe(user => {
    const currentUrl = this.router.url;
    console.log("current url", currentUrl)
    if (currentUrl === '/' && user?.role === 'admin') {
      console.log('Redirigiendo al dashboard');
      this.router.navigate(['/dashboard']);
    }
  });
  }
}
