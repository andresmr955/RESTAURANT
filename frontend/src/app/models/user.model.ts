export interface CustomerUser {
  id: number;
  username: string;
  email: string;
  role: 'admin' | 'chef' | 'cook';
  phone_number: string | null;
  avatar: string | null; // será una URL del archivo
  date_birth: string | null; // viene como string ISO
  address: string | null;
  notifications_enabled: boolean;
  date_joined_restaurant: string | null;
  average_task_completed: string | null; // cuidado: DateTimeField

  // campos heredados de AbstractUser que usualmente también llegan
  first_name?: string;
  last_name?: string;
  is_active?: boolean;
  is_staff?: boolean;
  last_login?: string | null;
  date_joined?: string;
}
