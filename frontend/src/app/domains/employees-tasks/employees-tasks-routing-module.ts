import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Tasks } from './pages/tasks/tasks';

const routes: Routes = [

    {
      path: '',
      redirectTo: 'tasks',
      pathMatch: 'full'
    },
    {
      path: 'tasks',
      component: Tasks,
      title: 'tasks'
    },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EmployeesTasksRoutingModule { }
