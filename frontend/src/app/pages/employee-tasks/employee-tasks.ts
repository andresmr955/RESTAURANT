import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Task } from './../../models/task.model';


@Component({
  selector: 'app-employee-tasks',
  imports: [CommonModule],
  templateUrl: './employee-tasks.html',
  styleUrl: './employee-tasks.scss'
})
export class EmployeeTasks {
  tasks = signal<Task[]>([
    {
      id: 1,
      status: 'in progress',
      description: 'Preparar ingredientes',
      assigned_employee: 7,
      priority: 2,
      assigned_date: '2024-06-25T08:00:00Z',
      start_time: null,
      end_time: null,
      comments: null
    },
    {
      id: 2,
      status: 'in progress',
      description: 'Cocinar arroz',
      assigned_employee: 7,
      priority: 1,
      assigned_date: '2024-06-25T09:00:00Z',
      start_time: '2024-06-25T09:30:00Z',
      end_time: null,
      comments: 'Empezado por el turno anterior'
    }
  ]);

  changeHandler(event: Event){
      const input = event.target as HTMLInputElement;
      const newTask = input.value;
      this.addTask(newTask);
  }
  

  addTask(title: string){
    const newTask: Task = {
      
      id: 3,
      status: 'in progress',
      description: 'Cocinar pasta',
      assigned_employee: 7,
      priority: 1,
      assigned_date: '2024-06-25T09:00:00Z',
      start_time: '2024-06-25T09:30:00Z',
      end_time: null,
      comments: 'Empezado por el turno anterior'
    };

    this.tasks.update((tasks) => [...tasks, newTask]);
  }

  deleteTask(id: number){
    console.log('ID recibido para eliminar:', id);
    this.tasks.update((tasks) => tasks.filter(task => task.id !== id));
    
  }
  onToggle(task: Task) {

    const nuevoEstado = task.status === 'completed' ? 'in progress' : 'completed';
    console.log(`Checkbox cambiado: ${task.description} → ${nuevoEstado}`);
    if (task.status === 'pending') {
      task.status = 'in progress';
    } else if (task.status === 'in progress') {
      task.status = 'completed';
    } else {
      task.status = 'pending';
    }

    this.tasks.update(tasks =>
      tasks.map(t => t.id === task.id ? { ...t, status: task.status } : t)
    );
    }
}
