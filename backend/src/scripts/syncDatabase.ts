import sequelize, { syncDatabase } from '../config/database';

/**
 * Script para sincronizar la base de datos
 * Úsalo con precaución - force: true eliminará todas las tablas
 */
const sync = async () => {
  try {
    console.log('🔄 Iniciando sincronización de base de datos...');
    
    // Cambiar a true solo si quieres eliminar y recrear las tablas
    const force = process.argv.includes('--force');
    
    if (force) {
      console.log('⚠️  ADVERTENCIA: Modo force activado - Se eliminarán todas las tablas');
    }
    
    await syncDatabase(force);
    
    console.log('✅ Sincronización completada');
    process.exit(0);
  } catch (error) {
    console.error('❌ Error durante la sincronización:', error);
    process.exit(1);
  }
};

sync();
