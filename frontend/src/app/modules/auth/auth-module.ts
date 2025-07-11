import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { AuthRoutingModule } from './auth-routing-module';
import { Login } from './pages/login/login';



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    AuthRoutingModule,
    Login
  ]
})
export class AuthModule { }
