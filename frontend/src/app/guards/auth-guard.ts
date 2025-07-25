import { CanActivateFn } from '@angular/router';
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { map, switchMap, take, of } from 'rxjs';
import { AuthService } from '../core/services/auth.service';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);
  return authService.user$.pipe(
    take(1),
    
    map(user => {
      if (!user) {
        return router.createUrlTree(['/login']);
      }

      if (user.role === 'admin') {
        return true;
      }

      if (user.role === 'cook') {
        console.log(user.role, 'redirigio al empleado')
        return router.createUrlTree(['/employee-tasks']);
      }

      return router.createUrlTree(['/login']);
    })
  );
};