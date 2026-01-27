# Sistema de Contacto - VETAS Web

## Descripción

Sistema completo de formulario de contacto para el sitio web de VETAS.

## Archivos Creados

### 1. `contacto.cgi`

Script principal que:

- Muestra el formulario de contacto
- Procesa los datos enviados
- Guarda las consultas en la base de datos
- Maneja 3 idiomas (ES, EN, BR)
- Muestra mensajes de éxito/error
- Incluye información de contacto directo

### 2. `sql/create_consulta_web_table.sql`

Script SQL para crear la tabla `CONSULTA_WEB` con los siguientes campos:

- **ID**: Identificador único auto-incremental
- **NOMBRE**: Nombre completo (obligatorio)
- **EMAIL**: Email del contacto (obligatorio)
- **TELEFONO**: Teléfono (opcional)
- **EMPRESA**: Empresa (opcional)
- **PAIS**: País (opcional)
- **MENSAJE**: Mensaje o consulta (obligatorio)
- **FECHA**: Fecha y hora de la consulta
- **IDIOMA**: Idioma usado (es, en, br)
- **LEIDO**: Si fue leído (0/1)
- **RESPONDIDO**: Si fue respondido (0/1)
- **NOTAS**: Notas internas

### 3. `footer.html` (modificado)

Actualizado el link "Contacto" para apuntar a `contacto.cgi`

## Instalación

### Paso 1: Crear la tabla en la base de datos

```sql
mysql -u usuario -p nombre_db < sql/create_consulta_web_table.sql
```

O ejecutar directamente en MySQL/phpMyAdmin el contenido del archivo SQL.

### Paso 2: Configurar Google reCAPTCHA

Ver instrucciones detalladas en: `RECAPTCHA_CONFIG.md`

1. Obtener Site Key y Secret Key de Google reCAPTCHA
2. Reemplazar en `contacto.cgi`:
   - Línea ~91: `my $secret_key = 'TU_SECRET_KEY';`
   - Línea ~245: `data-sitekey="TU_SITE_KEY"`

### Paso 3: Instalar módulo LWP (si no está instalado)

```bash
cpan LWP::UserAgent
```

### Paso 4: Verificar permisos

```bash
chmod +x contacto.cgi
```

## Características

### Formulario de Contacto

✅ **Campos obligatorios**: Nombre, Email, Mensaje
✅ **Campos opcionales**: Teléfono, Empresa, País
✅ **Validación**: HTML5 + Backend
✅ **Diseño responsive**: Adaptable a móviles
✅ **Multi-idioma**: Español, Inglés, Portugués
✅ **Selector de idioma**: Botones en la parte superior
✅ **Google reCAPTCHA v2**: Protección anti-spam
✅ **Verificación server-side**: CAPTCHA validado en el servidor

### Seguridad

✅ **Escapado de SQL**: Prevención de inyección SQL
✅ **Validación de email**: Tipo email en HTML
✅ **Charset UTF-8**: Soporte completo de caracteres especiales

### UX/UI

✅ **Mensajes de éxito**: Alert verde con icono
✅ **Mensajes de error**: Alert rojo con icono
✅ **Iconos FontAwesome**: Para cada campo
✅ **Cards con sombra**: Diseño moderno
✅ **Hover effects**: Botones interactivos
✅ **Información de contacto**: Panel lateral con oficinas

### Panel de Información

- **U.S.A.**: Miami, FL
- **LATINOAMÉRICA**: Buenos Aires, Argentina
- **BRASIL**: Caxias do Sul, RS

Cada oficina muestra:

- 📍 Ubicación
- 📞 Teléfono
- 📧 Email

## Uso

### Para usuarios

1. Hacer clic en "Contacto" en el footer
2. Completar el formulario
3. Hacer clic en "Enviar Consulta"
4. Ver mensaje de confirmación

### Para administradores

Consultar las consultas recibidas:

```sql
SELECT * FROM CONSULTA_WEB ORDER BY FECHA DESC;
```

Ver consultas no leídas:

```sql
SELECT * FROM CONSULTA_WEB WHERE LEIDO = 0 ORDER BY FECHA DESC;
```

Ver consultas pendientes de respuesta:

```sql
SELECT * FROM CONSULTA_WEB WHERE RESPONDIDO = 0 ORDER BY FECHA DESC;
```

Marcar como leído:

```sql
UPDATE CONSULTA_WEB SET LEIDO = 1 WHERE ID = ?;
```

Marcar como respondido:

```sql
UPDATE CONSULTA_WEB SET RESPONDIDO = 1, NOTAS = 'Respuesta enviada' WHERE ID = ?;
```

## Personalización

### Colores

El formulario usa el color verde corporativo de VETAS:

- **Verde principal**: `#72bf44`
- **Verde hover**: `#5da835`
- **Verde focus**: `rgba(114, 191, 68, 0.25)`

### Idiomas

El sistema detecta automáticamente el idioma del parámetro `?i=` en la URL:

- `?i=es` - Español (por defecto)
- `?i=en` - English
- `?i=br` - Português

## Próximos pasos recomendados

1. **Sistema de notificaciones por email**: Enviar email al admin cuando llega una consulta
2. **Panel de administración**: Crear `admin_consultas.cgi` para gestionar consultas
3. **Estadísticas**: Dashboard con gráficos de consultas por país, idioma, etc.
4. **Exportación**: Opción de exportar consultas a CSV/Excel
5. **Respuesta automática**: Email de confirmación al usuario

## Soporte

Para dudas o modificaciones, contactar a: **Damian G. Sagranichne**
