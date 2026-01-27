import { Router } from 'express';
import { getHome, getInfo } from '../controllers/home.controller';

const router = Router();

/**
 * @route   GET /api/home
 * @desc    Página principal de la API
 * @access  Public
 */
router.get('/', getHome);

/**
 * @route   GET /api/home/info
 * @desc    Información del sistema
 * @access  Public
 */
router.get('/info', getInfo);

export default router;
