/**
 * Interfaz de respuesta estándar de la API
 */
export interface ApiResponse<T = any> {
  success: boolean;
  message?: string;
  data?: T;
  error?: string;
}

/**
 * Interfaz para paginación
 */
export interface PaginationParams {
  page: number;
  limit: number;
  offset: number;
}

/**
 * Interfaz para respuesta paginada
 */
export interface PaginatedResponse<T> {
  success: boolean;
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}
