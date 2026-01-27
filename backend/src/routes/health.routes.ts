import { Router } from 'express';
import { healthCheck, databaseCheck } from '../controllers/health.controller';

const router = Router();

/**
 * @route   GET /api/health
 * @desc    Verificar estado del servidor
 * @access  Public
 */
router.get('/', healthCheck);

/**
 * @route   GET /api/health/database
 * @desc    Verificar conexión a la base de datos
 * @access  Public
 */
router.get('/database', databaseCheck);

export default router;
