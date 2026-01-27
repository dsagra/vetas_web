import express, { Application } from 'express';
import cors from 'cors';
import config from './config/config';
import { errorHandler } from './middlewares/errorHandler';
import { notFoundHandler } from './middlewares/notFoundHandler';

// Importar rutas
import healthRoutes from './routes/health.routes';

class App {
  public app: Application;

  constructor() {
    this.app = express();
    this.config();
    this.routes();
    this.errorHandling();
  }

  private config(): void {
    // Middlewares
    this.app.use(cors({
      origin: config.cors.origin,
      credentials: true,
    }));
    this.app.use(express.json());
    this.app.use(express.urlencoded({ extended: true }));

    // Logging middleware (opcional)
    if (config.server.env === 'development') {
      this.app.use((req, res, next) => {
        console.log(`${req.method} ${req.path}`);
        next();
      });
    }
  }

  private routes(): void {
    // Ruta base
    this.app.get('/', (req, res) => {
      res.json({
        message: 'VETAS API Backend',
        version: '1.0.0',
        status: 'running',
      });
    });

    // Rutas de la aplicación
    this.app.use('/api/health', healthRoutes);
    
    // Aquí irán las demás rutas
    // this.app.use('/api/empresas', empresaRoutes);
    // this.app.use('/api/noticias', noticiasRoutes);
    // this.app.use('/api/menu', menuRoutes);
  }

  private errorHandling(): void {
    // Manejar rutas no encontradas
    this.app.use(notFoundHandler);
    
    // Manejar errores
    this.app.use(errorHandler);
  }
}

export default new App().app;
