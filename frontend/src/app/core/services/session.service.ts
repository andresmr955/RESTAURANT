import { Inject, Injectable, PLATFORM_ID } from '@angular/core';
import { AuthService } from './auth.service';
import { isPlatformBrowser } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class SessionService {

  constructor(
    private authService: AuthService,
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
    });
    }
   }
}
