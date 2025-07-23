import { Routes } from '@angular/router';
import { NotFoundComponent } from './shared/components/not-found-component/not-found-component';
export const routes: Routes = [
     {
        path: '',
        loadChildren: () => import('./domains/auth/auth-module').then((m) => m.AuthModule),
    },
    {
        path: 'dashboard', 
        loadChildren: () => import('./domains/dashboard/dashboard-module').then((m) => m.DashboardModule)
    },
    {
        path: 'employee-tasks', 
        loadChildren: () => import('./domains/employees-tasks/employees-tasks-module').then((m) => m.EmployeesTasksModule)
    },
    {   
        path: '**',
        component: NotFoundComponent
    }
];
