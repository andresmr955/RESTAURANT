export interface Task {
  id: number;  
  status: 'pending' | 'in progress' | 'completed';
  description: string;
  assigned_employee: number; 
  priority: number;
  assigned_date: string;     
  start_time: string | null; 
  end_time: string | null;
  comments: string | null;
}

