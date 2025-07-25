import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, Validators, FormGroup, ReactiveFormsModule  } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { faPen, faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome'; // Import FontAwesomeModule
import { Button } from './../../../../shared/components/button/button'
import { AuthService } from './../../../../core/services/auth.service';
import { RequestStatus } from './../../../../models/request-status.model';
import { TokenService } from './../../../../core/services/token.service';
@Component({
  selector: 'app-login-form',
  imports: [CommonModule, FontAwesomeModule, ReactiveFormsModule, Button ],
  templateUrl: './login-form.html',
  styleUrl: './login-form.scss'
})
export class LoginForm {
  form: FormGroup;

  
  faPen = faPen;
  faEye = faEye;
  faEyeSlash = faEyeSlash;
  showPassword = false;
  status: RequestStatus = 'init';

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private authService: AuthService,
    private route: ActivatedRoute,
    private tokenService: TokenService
  ) {
    this.form = this.formBuilder.nonNullable.group({
    email: ['', [Validators.email, Validators.required]],
    password: ['', [Validators.required, Validators.minLength(6)]],
  });

  // Luego se accede a los parámetros de la URL
  this.route.queryParamMap.subscribe(params => {
    const email = params.get('email');
    if (email) {
      this.form.controls['email'].setValue(email);
    }
  });
  }

  doLogin() {

    if (this.form.valid) {
      this.status = 'loading';
      const { email, password } = this.form.getRawValue();
      this.authService.loginAndGet(email, password).subscribe({
  next: user => {
      this.router.navigate(['/dashboard']);
    }
});
    } else {
      this.form.markAllAsTouched();
    }
  }

}