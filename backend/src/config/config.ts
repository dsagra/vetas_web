import dotenv from 'dotenv';

dotenv.config();

interface Config {
  server: {
    env: string;
    port: number;
  };
  database: {
    host: string;
    port: number;
    name: string;
    user: string;
    password: string;
  };
  cors: {
    origin: string;
  };
}

const config: Config = {
  server: {
    env: process.env.NODE_ENV || 'development',
    port: parseInt(process.env.PORT || '3000', 10),
  },
  database: {
    host: process.env.DB_HOST || 'localhost',
    port: parseInt(process.env.DB_PORT || '3306', 10),
    name: process.env.DB_NAME || 'vetas_VETAS2',
    user: process.env.DB_USER || 'vetas_user',
    password: process.env.DB_PASSWORD || '',
  },
  cors: {
    origin: process.env.CORS_ORIGIN || '*',
  },
};

export default config;
