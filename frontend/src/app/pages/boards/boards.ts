import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Navbar } from '../../components/navbar/navbar';

@Component({
  selector: 'app-boards',
  standalone: true,
  imports: [ CommonModule, Navbar],
  templateUrl: './boards.html',
  styleUrl: './boards.scss'
})
export class Boards {

}
