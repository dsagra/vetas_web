import { Request, Response } from 'express';

/**
 * Endpoint principal de Home
 */
export const getHome = async (req: Request, res: Response) => {
  res.status(200).json({
    success: true,
    message: '¡Bienvenido a VETAS API!',
    data: {
      name: 'VETAS Backend',
      version: '1.0.0',
      description: 'API para el sistema VETAS',
      endpoints: {
        health: '/api/health',
        home: '/api/home',
      },
    },
    timestamp: new Date().toISOString(),
  });
};

/**
 * Información del sistema
 */
export const getInfo = async (req: Request, res: Response) => {
  res.status(200).json({
    success: true,
    data: {
      server: 'VETAS Backend API',
      version: '1.0.0',
      status: 'online',
      uptime: process.uptime(),
      environment: process.env.NODE_ENV || 'development',
    },
    timestamp: new Date().toISOString(),
  });
};
