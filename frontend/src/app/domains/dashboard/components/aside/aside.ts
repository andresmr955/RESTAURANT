import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AuthService } from '../../../../core/services/auth.service';

@Component({
  selector: 'app-aside',
  imports: [RouterModule],
  templateUrl: './aside.html',
  styleUrl: './aside.scss'
})
export class Aside {
constructor(private authService: AuthService){}

  logout(){
    this.authService.logout()
  }
}
