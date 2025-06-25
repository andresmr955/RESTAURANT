import { Routes } from '@angular/router';
import { Login } from './pages/login/login';
import { Boards } from './pages/boards/boards';
import { EmployeeTasks } from './pages/employee-tasks/employee-tasks';

export const routes: Routes = [
    {
        path: 'login', 
        component: Login
    },
    {
        path: 'boards', 
        component: Boards
    },
    {
        path: 'employee-tasks', 
        component: EmployeeTasks
    }
];
