import { Request, Response } from 'express';
import sequelize from '../config/database';

/**
 * Verificar estado del servidor
 */
export const healthCheck = async (req: Request, res: Response) => {
  res.status(200).json({
    success: true,
    message: 'Servidor funcionando correctamente',
    timestamp: new Date().toISOString(),
  });
};

/**
 * Verificar conexión a la base de datos
 */
export const databaseCheck = async (req: Request, res: Response) => {
  try {
    await sequelize.authenticate();
    res.status(200).json({
      success: true,
      message: 'Conexión a la base de datos exitosa',
      database: sequelize.config.database,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Error al conectar con la base de datos',
      error: error instanceof Error ? error.message : 'Unknown error',
    });
  }
};
