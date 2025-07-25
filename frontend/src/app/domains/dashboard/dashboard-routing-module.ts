import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Cms } from './pages/cms/cms';
import { EmployeesListComponent } from './pages/employees-list/employees-list';
import { authGuard } from '../../guards/auth-guard';
authGuard
const routes: Routes = [

    {
      path: '',
      redirectTo: 'cms', 
      pathMatch: 'full'
    },
    {
      path: 'cms',
      canActivate: [ authGuard ],
      component: Cms, 
      title: 'cms'
    }, 
    {
    path: 'employees',
    component: EmployeesListComponent
    }

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
