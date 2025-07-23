import { Component, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Task } from './../../../../models/task.model';
import { TaskServiceTs } from './../../../../core/services/task.service.ts';

@Component({
  selector: 'app-tasks',
  imports: [CommonModule],
  templateUrl: './tasks.html',
  styleUrl: './tasks.css'
})
export class Tasks {
  tasks = signal<Task[]>([]);

  constructor(private taskService: TaskServiceTs, 
  ){
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
  
   

    deleteTask(id: number){
      this.tasks.update((tasks) => tasks.filter(task => task.id !== id)); 
    }
    
    onToggle(task: Task) {
      let newStatus: Task['status'];
      
      switch (task.status) { 
          case 'pending':
            newStatus = 'in progress';
            break;
          case 'in progress':
            newStatus = 'completed';
            break;
          default: 
            newStatus = 'pending'
      }

      //Update local task in signal
      this.tasks.update(tasks => 
        tasks.map(t => 
          t.id === task.id ? { ...t, status: newStatus }: t
        )
      );

      //send to backend

      this.taskService.updateTaskStatus(task.id, newStatus).subscribe({
        next: (updatedTask) => {
          this.tasks.update(tasks =>
            tasks.map(t =>
              t.id === updatedTask.id ? updatedTask : t
            )
          );
        }, 
        error: (err) => {
          console.log('Error updating backend status', err);
          this.tasks.update(
            tasks => 
              tasks.map(t => 
                t.id === task.id ? { ...t, status: task.status}: t
              )
          );
        }
      });
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
    
    clearCompleted() {
      const tasks = this.tasks();
      const allCompleted = tasks.length > 0 && tasks.every(t => t.status === 'completed');
      if (allCompleted) {
          this.notifyChef();
        }
    } 

    notifyChef(){
    this.deleteAllTasks();
    alert('Congratulations! All tasks were completed, The Souschef has been notified');
    }
    deleteAllTasks() {
      console.log('delete all')
    this.tasks.update(() => []); // vacía toda la lista
    
    } 
}

  


