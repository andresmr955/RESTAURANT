import { Component  } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';

import { RouterModule } from '@angular/router';
import { SessionService } from './core/services/session.service';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css'], 
})
export class App {
  protected title = 'frontend';

  constructor(

  private sessionService: SessionService,

) {}
  ngOnInit(){
    this.sessionService.initializeSessionSync();
    this.sessionService.loadSessionFromStorage().subscribe();
    this.sessionService.redirectToDashboard();
   

  
  }
}

