import { Routes } from '@angular/router';
import { Login } from './modules/auth/pages/login/login';
import { Boards } from './pages/boards/boards';
import { EmployeeTasks } from './pages/employee-tasks/employee-tasks';

export const routes: Routes = [
     {
    path: '',
    loadChildren: () => import('./modules/auth/auth-module').then((m) => m.AuthModule),
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
