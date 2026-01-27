# VETAS Backend API

Backend API para el sistema VETAS desarrollado con Node.js, Express, TypeScript y Sequelize.

## 🚀 Características

- **TypeScript**: Tipado estático para mejor mantenibilidad
- **Express**: Framework web minimalista y flexible
- **Sequelize**: ORM para MySQL con soporte completo
- **Arquitectura en capas**: Separación clara de responsabilidades
- **Variables de entorno**: Configuración segura con dotenv
- **Error handling**: Manejo centralizado de errores
- **CORS configurado**: Listo para desarrollo cross-origin

## 📁 Estructura del Proyecto

```
backend/
├── src/
│   ├── config/           # Configuraciones (DB, app)
│   ├── controllers/      # Controladores de rutas
│   ├── middlewares/      # Middlewares personalizados
│   ├── models/          # Modelos de Sequelize
│   ├── routes/          # Definición de rutas
│   ├── services/        # Lógica de negocio
│   ├── types/           # Tipos TypeScript personalizados
│   ├── utils/           # Utilidades y helpers
│   ├── scripts/         # Scripts de utilidad
│   ├── app.ts           # Configuración de Express
│   └── server.ts        # Punto de entrada
├── dist/                # Código compilado
├── .env                 # Variables de entorno (no commitear)
├── .env.example         # Ejemplo de variables de entorno
├── tsconfig.json        # Configuración de TypeScript
├── nodemon.json         # Configuración de Nodemon
└── package.json         # Dependencias y scripts
```

## 🔧 Instalación

### Requisitos previos

- Node.js (versión 18 o superior recomendada)
- npm o yarn
- MySQL (ya configurado)

### Pasos

1. **Instalar dependencias de producción:**

```bash
cd backend
npm install express cors dotenv mysql2 sequelize
```

2. **Instalar dependencias de desarrollo:**

```bash
npm install -D @types/node @types/express @types/cors typescript ts-node nodemon eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

3. **Configurar variables de entorno:**
   El archivo `.env` ya está configurado con:

```env
DB_HOST=localhost
DB_NAME=vetas_VETAS2
DB_USER=vetas_user
DB_PASSWORD=ghewrp54
PORT=3000
```

## 🏃 Ejecutar el Proyecto

### Modo desarrollo (con hot-reload)

```bash
npm run dev
```

### Compilar TypeScript

```bash
npm run build
```

### Ejecutar en producción

```bash
npm start
```

## 📡 Endpoints Disponibles

### Health Check

- **GET** `/` - Estado del servidor
- **GET** `/api/health` - Estado del servidor
- **GET** `/api/health/database` - Verificar conexión a BD

### Próximamente

- `/api/empresas` - CRUD de empresas
- `/api/noticias` - CRUD de noticias
- `/api/menu` - Gestión de menús

## 🗄️ Base de Datos

### Conexión

El proyecto está configurado para conectarse a:

- **Base de datos**: `vetas_VETAS2`
- **Host**: `localhost`
- **Usuario**: `vetas_user`
- **Password**: `ghewrp54`

### Sincronizar modelos

```bash
npm run db:sync
```

⚠️ **Advertencia**: Usar `--force` eliminará todas las tablas:

```bash
npm run db:sync -- --force
```

## 🏗️ Arquitectura

### Patrón MVC

- **Models**: Definición de esquemas de datos (Sequelize)
- **Controllers**: Lógica de manejo de requests
- **Routes**: Definición de endpoints
- **Services**: Lógica de negocio reutilizable

### Middlewares

- `errorHandler`: Manejo centralizado de errores
- `notFoundHandler`: Manejo de rutas no encontradas
- CORS configurado
- JSON y URL-encoded parsing

## 📝 Agregar Nuevas Funcionalidades

### 1. Crear un nuevo modelo

```typescript
// src/models/TuModelo.model.ts
import { DataTypes, Model } from "sequelize";
import sequelize from "../config/database";

class TuModelo extends Model {
  // ... definir atributos
}

TuModelo.init(
  {
    /* ... */
  },
  { sequelize },
);
export default TuModelo;
```

### 2. Crear un controlador

```typescript
// src/controllers/tuModelo.controller.ts
import { Request, Response } from "express";

export const getTodos = async (req: Request, res: Response) => {
  // ... lógica
};
```

### 3. Crear rutas

```typescript
// src/routes/tuModelo.routes.ts
import { Router } from "express";
import { getTodos } from "../controllers/tuModelo.controller";

const router = Router();
router.get("/", getTodos);
export default router;
```

### 4. Registrar en app.ts

```typescript
import tuModeloRoutes from "./routes/tuModelo.routes";
// ...
this.app.use("/api/tu-modelo", tuModeloRoutes);
```

## 🔒 Seguridad

- [ ] Implementar autenticación JWT
- [ ] Implementar rate limiting
- [ ] Implementar helmet para headers de seguridad
- [ ] Validación de inputs con express-validator
- [ ] Sanitización de datos

## 🧪 Testing

```bash
npm test
```

## 📚 Recursos

- [Express Docs](https://expressjs.com/)
- [Sequelize Docs](https://sequelize.org/)
- [TypeScript Docs](https://www.typescriptlang.org/)

## 👤 Autor

Proyecto VETAS

## 📄 Licencia

ISC
