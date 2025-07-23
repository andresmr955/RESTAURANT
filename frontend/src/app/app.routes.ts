import { Routes } from '@angular/router';
import { Login } from './domains/auth/pages/login/login';
import { EmployeeTasks } from './domains/employees_tasks/pages/employee-tasks/employee-tasks';
import { NotFoundComponent } from './shared/components/not-found-component/not-found-component';
export const routes: Routes = [
     {
    path: '',
    loadChildren: () => import('./domains/auth/auth-module').then((m) => m.AuthModule),
    },
    {
        path: 'employee-tasks', 
        component: EmployeeTasks
    },
    {   
        path: '**',
        component: NotFoundComponent
    }
];
