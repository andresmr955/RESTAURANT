import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Tasks } from './pages/tasks/tasks';

const routes: Routes = [

    {
      path: '',
      redirectTo: 'employee-tasks',
      pathMatch: 'full'
    },
    {
      path: 'employee-tasks',
      component: Tasks,
      title: 'employee-tasks'
    },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EmployeesTasksRoutingModule { }
