import { Component, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Task } from './../../../../models/task.model';
import { TaskServiceTs } from './../../../../core/services/task.service.ts';

@Component({
  selector: 'app-employee-tasks',
  imports: [CommonModule],
  templateUrl: './employee-tasks.html',
  styleUrl: './employee-tasks.css'
})
export class EmployeeTasks {
  tasks = signal<Task[]>([]);

  constructor(private taskService: TaskServiceTs){
  }

  ngOnInit(){
    this.loadTasks();
  }


  filter = signal<'all' | 'pending' | 'completed' | 'in progress'>('all')
    tasksByFilter = computed(() => {
      const filter = this.filter();
      const tasks = this.tasks();
      if (filter === 'pending') {
        return tasks.filter(task => task.status === 'pending');
      }
      if (filter === 'in progress') {
        return tasks.filter(task => task.status === 'in progress');
      }
      if (filter === 'completed') {
        return tasks.filter(task => task.status === 'completed');
      }
      return tasks;
    })
  

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
    
    this.tasks.update((tasks) => tasks.filter(task => task.id !== id));
    
  }
  
  
    changeFilter(filter: 'all' | 'pending' | 'completed' | 'in progress') {
    this.filter.set(filter);
  }

  loadTasks() {
    this.taskService.getTasks().subscribe({
      next: (data: Task[]) => this.tasks.set(data),
      error: (err: any) => console.error('Error cargando tareas:', err)
    });
  }
}