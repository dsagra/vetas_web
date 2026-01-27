import app from './app';
import config from './config/config';
import { testConnection } from './config/database';

const PORT = config.server.port;

const startServer = async () => {
  try {
    // Iniciar servidor
    app.listen(PORT, () => {
      console.log('=================================');
      console.log(`🚀 Servidor corriendo en puerto ${PORT}`);
      console.log(`📊 Ambiente: ${config.server.env}`);
      console.log(`🗄️  Base de datos: ${config.database.name}`);
      console.log('=================================');
      
      // Testear conexión a la base de datos (no bloqueante)
      testConnection().catch((error) => {
        console.warn('⚠️  Advertencia: No se pudo conectar a la base de datos');
        console.warn('   El servidor está corriendo pero las operaciones de BD fallarán');
        console.warn('   Error:', error.message);
      });
    });
  } catch (error) {
    console.error('❌ Error al iniciar el servidor:', error);
    process.exit(1);
  }
};

startServer();
