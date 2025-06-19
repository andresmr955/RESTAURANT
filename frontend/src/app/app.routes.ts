import { Routes } from '@angular/router';
import { Login } from './pages/login/login';
import { Boards } from './pages/boards/boards';

export const routes: Routes = [
    {
        path: 'login', 
        component: Login
    },
    {
        path: 'boards', 
        component: Boards
    }
];
