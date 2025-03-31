export interface Container {
    container_id: number;
    type: string;
    status: string;
    location: string; 
    owner_id: string;
    created_at: string;
  }
  export interface User {
    user_id: string;
    name: string;
    email: string;
    role: string;
    created_at: string;
  }
  export interface Rental{
    rental_id: string,
    start_date: string,
    end_date: string,
    status: string,
    daily_rate: number
    created_at: string,
    container: string,
    user: string
  }