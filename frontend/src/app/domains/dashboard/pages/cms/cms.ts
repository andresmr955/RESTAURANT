import { Component } from '@angular/core';
import { Navbar } from '../../components/navbar/navbar';
import { Aside } from '../../components/aside/aside';
import { RouterModule } from '@angular/router';
RouterModule
@Component({
  selector: 'app-cms',
  imports: [ Navbar, Aside, RouterModule],
  templateUrl: './cms.html',
  styleUrl: './cms.scss'
})
export class Cms {

}
