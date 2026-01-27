/**
 * Utilidad para crear respuestas exitosas estandarizadas
 */
export const successResponse = <T>(data: T, message?: string) => {
  return {
    success: true,
    message: message || 'Operación exitosa',
    data,
  };
};

/**
 * Utilidad para crear respuestas de error estandarizadas
 */
export const errorResponse = (message: string, error?: any) => {
  return {
    success: false,
    message,
    ...(error && { error }),
  };
};

/**
 * Utilidad para calcular offset de paginación
 */
export const getPaginationParams = (page = 1, limit = 10) => {
  const parsedPage = parseInt(String(page), 10);
  const parsedLimit = parseInt(String(limit), 10);
  
  return {
    page: parsedPage > 0 ? parsedPage : 1,
    limit: parsedLimit > 0 ? parsedLimit : 10,
    offset: (parsedPage - 1) * parsedLimit,
  };
};

/**
 * Utilidad para crear respuesta paginada
 */
export const paginatedResponse = <T>(
  data: T[],
  page: number,
  limit: number,
  total: number
) => {
  return {
    success: true,
    data,
    pagination: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit),
    },
  };
};
