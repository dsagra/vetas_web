# 📧 Integración de Suscripción en VETAS

## ✅ Integración Completa

La sección de suscripción "Recibí VETAS en tu email" ha sido **integrada exitosamente** en la página principal de VETAS (`index.cgi`).

## 🎯 Ubicación

La sección se muestra **al final de la página**, justo antes del footer, después de los banners y videos. Esta posición estratégica maximiza la visibilidad sin interrumpir la navegación.

## 🌍 Soporte Multiidioma

La integración incluye soporte automático para los 3 idiomas:

- **Español** (`i=es`): `components/seccion-suscripcion.html`
- **English** (`i=en`): `components/seccion-suscripcion-en.html`
- **Português** (`i=br`): `components/seccion-suscripcion-br.html`

El sistema detecta automáticamente el idioma actual y muestra la versión correspondiente.

## 📝 Archivos Integrados

### 1. `index.cgi` (Modificado)
```perl
# Incluir la sección de suscripción según el idioma
if ($idioma eq "es") {
    open SUSCRIPCION, "components/seccion-suscripcion.html" or die "No se pudo abrir seccion-suscripcion.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}
elsif ($idioma eq "en") {
    open SUSCRIPCION, "components/seccion-suscripcion-en.html" or die "No se pudo abrir seccion-suscripcion-en.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}
elsif ($idioma eq "br") {
    open SUSCRIPCION, "components/seccion-suscripcion-br.html" or die "No se pudo abrir seccion-suscripcion-br.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}
```

### 2. `suscripcion.cgi` (Nuevo)
Script CGI completo que procesa las suscripciones con:
- ✅ Validación de email
- ✅ reCAPTCHA v2 para prevenir spam
- ✅ Almacenamiento en base de datos
- ✅ Detección de suscripciones duplicadas
- ✅ Páginas de éxito/error personalizadas
- ✅ Soporte multiidioma

## 🔧 Configuración Requerida

### 1. Google reCAPTCHA

**Obtener las claves:**
1. Ve a: https://www.google.com/recaptcha/admin/create
2. Crea un nuevo sitio con reCAPTCHA v2
3. Añade tu dominio: `www.vetas.com`
4. Copia las claves generadas

**Configurar en los archivos:**

#### A. En `components/seccion-suscripcion.html` (y versiones EN/BR)
```html
<!-- Buscar esta línea: -->
<div class="g-recaptcha" data-sitekey="TU_SITE_KEY_AQUI"></div>

<!-- Reemplazar por: -->
<div class="g-recaptcha" data-sitekey="6LeXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"></div>
```

#### B. En `suscripcion.cgi`
```perl
# Buscar esta línea:
my $RECAPTCHA_SECRET_KEY = 'TU_SECRET_KEY_AQUI';

# Reemplazar por:
my $RECAPTCHA_SECRET_KEY = '6LeXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
```

### 2. Credenciales de Base de Datos

En `suscripcion.cgi`, actualizar las credenciales si es necesario:

```perl
sub conectar_db {
    my $database = "vetascom_web";
    my $host = "localhost";
    my $user = "vetascom_web";
    my $password = "w3bv3t4s";  # ⚠️ Cambiar por tu contraseña real
    
    # ... resto del código
}
```

### 3. Tabla de Base de Datos

La tabla `SUSCRIPTORES` debe estar creada. Si no existe, ejecutar:

```bash
mysql -u vetascom_web -p vetascom_web < sql/create_suscriptores_table.sql
```

O manualmente en MySQL:

```sql
CREATE TABLE IF NOT EXISTS SUSCRIPTORES (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    EMAIL VARCHAR(255) NOT NULL UNIQUE,
    NOMBRE VARCHAR(255),
    IDIOMA VARCHAR(10) DEFAULT 'es',
    FECHA_SUSCRIPCION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO TINYINT(1) DEFAULT 1,
    IP VARCHAR(45),
    USER_AGENT TEXT,
    INDEX idx_email (EMAIL),
    INDEX idx_activo (ACTIVO),
    INDEX idx_fecha (FECHA_SUSCRIPCION)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## 🚀 Instalación Rápida

### Script Automático (Recomendado)

```bash
# Desde el directorio del proyecto
./configure_recaptcha.sh [SITE_KEY] [SECRET_KEY]
```

### Manual

1. **Configurar reCAPTCHA**
   ```bash
   # Editar los 3 archivos de componentes
   nano components/seccion-suscripcion.html
   nano components/seccion-suscripcion-en.html
   nano components/seccion-suscripcion-br.html
   
   # Buscar y reemplazar: TU_SITE_KEY_AQUI
   ```

2. **Configurar Secret Key**
   ```bash
   nano suscripcion.cgi
   # Buscar y reemplazar: TU_SECRET_KEY_AQUI
   ```

3. **Verificar permisos**
   ```bash
   chmod 755 suscripcion.cgi
   chmod 644 components/seccion-suscripcion*.html
   ```

4. **Crear tabla de BD** (si no existe)
   ```bash
   mysql -u vetascom_web -p vetascom_web < sql/create_suscriptores_table.sql
   ```

5. **Probar la integración**
   ```bash
   # Visitar:
   https://www.vetas.com/index.cgi?i=es
   
   # Scroll hasta el final y verificar que aparece el formulario
   ```

## 🧪 Testing

### 1. Verificar Visualización
- [ ] La sección aparece al final de la home
- [ ] El diseño es responsive (mobile/desktop)
- [ ] Los 3 idiomas funcionan correctamente
- [ ] El reCAPTCHA se muestra correctamente

### 2. Verificar Funcionalidad
- [ ] El formulario envía datos correctamente
- [ ] reCAPTCHA valida antes de enviar
- [ ] Los datos se guardan en la base de datos
- [ ] Página de éxito se muestra correctamente
- [ ] Emails duplicados se detectan
- [ ] Errores se manejan apropiadamente

### 3. Testing por Idioma

**Español:**
```
https://www.vetas.com/index.cgi?i=es
```

**English:**
```
https://www.vetas.com/index.cgi?i=en
```

**Português:**
```
https://www.vetas.com/index.cgi?i=br
```

## 📊 Consultas Útiles

### Ver todos los suscriptores
```sql
SELECT * FROM SUSCRIPTORES ORDER BY FECHA_SUSCRIPCION DESC;
```

### Contar suscriptores activos
```sql
SELECT COUNT(*) as total FROM SUSCRIPTORES WHERE ACTIVO = 1;
```

### Suscriptores por idioma
```sql
SELECT IDIOMA, COUNT(*) as total 
FROM SUSCRIPTORES 
WHERE ACTIVO = 1 
GROUP BY IDIOMA;
```

### Suscriptores del último mes
```sql
SELECT * FROM SUSCRIPTORES 
WHERE FECHA_SUSCRIPCION >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
AND ACTIVO = 1
ORDER BY FECHA_SUSCRIPCION DESC;
```

### Exportar emails para newsletter
```sql
SELECT EMAIL, NOMBRE, IDIOMA 
FROM SUSCRIPTORES 
WHERE ACTIVO = 1 
INTO OUTFILE '/tmp/suscriptores.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

## 🎨 Personalización

### Modificar Diseño

Los estilos CSS están dentro de cada archivo HTML en `components/`. Para personalizar:

```html
<style>
    /* Variables de color */
    :root {
        --vetas-primary: #72bf44;    /* Verde principal */
        --vetas-dark: #2c5f2d;       /* Verde oscuro */
        --vetas-wood: #8B7355;       /* Madera */
    }
    
    /* Personalizar aquí... */
</style>
```

### Modificar Textos

Editar directamente los archivos HTML en `components/`:
- `seccion-suscripcion.html` (Español)
- `seccion-suscripcion-en.html` (English)
- `seccion-suscripcion-br.html` (Português)

## 🔒 Seguridad

### ✅ Implementado
- [x] reCAPTCHA v2 para prevenir bots
- [x] Validación de formato de email
- [x] Sanitización de inputs
- [x] Protección contra SQL injection (prepared statements)
- [x] Registro de IP y User Agent
- [x] HTTPS recomendado

### ⚠️ Recomendaciones
1. **NUNCA** commitear las claves de reCAPTCHA al repositorio
2. Usar variables de entorno para credenciales sensibles
3. Implementar rate limiting si hay mucho spam
4. Configurar HTTPS/SSL en el servidor
5. Hacer backups regulares de la tabla SUSCRIPTORES

## 📧 Próximos Pasos (Opcional)

### 1. Email de Bienvenida
Implementar función `enviar_email_bienvenida()` en `suscripcion.cgi` usando:
- SMTP
- SendGrid
- Amazon SES

### 2. Confirmación de Email (Double Opt-in)
1. Enviar email con link de confirmación
2. Token único de verificación
3. Activar solo después del click

### 3. Panel de Administración
- Ver lista de suscriptores
- Exportar a CSV/Excel
- Estadísticas y métricas
- Gestión de bajas

### 4. Integración con Newsletter
- Mailchimp
- SendGrid
- Newsletter propia

## 🆘 Troubleshooting

### El formulario no se muestra
```bash
# Verificar que los archivos existen
ls -la components/seccion-suscripcion*.html

# Verificar permisos
chmod 644 components/seccion-suscripcion*.html
```

### Error "No se pudo abrir seccion-suscripcion.html"
```bash
# Verificar que estás en el directorio correcto
pwd
# Debe mostrar: /home/vetascom/public_html (o similar)

# Si no, ajustar la ruta en index.cgi
```

### reCAPTCHA no funciona
1. Verificar que la Site Key es correcta
2. Verificar que el dominio está autorizado en Google reCAPTCHA
3. Verificar que el script de Google se carga: View Source → buscar `www.google.com/recaptcha`

### Error al guardar en base de datos
```bash
# Verificar conexión
mysql -u vetascom_web -p vetascom_web

# Verificar que la tabla existe
SHOW TABLES LIKE 'SUSCRIPTORES';

# Verificar estructura
DESCRIBE SUSCRIPTORES;
```

### Módulos Perl faltantes
```bash
# Instalar módulos necesarios
cpan install LWP::UserAgent
cpan install JSON
cpan install DBI
cpan install DBD::mysql
```

## 📞 Soporte

Para problemas o consultas:
- Email: info@vetas.com
- Revisar logs del servidor: `/var/log/apache2/error.log`
- Revisar logs de MySQL: `/var/log/mysql/error.log`

---

**✨ La sección de suscripción está lista para captar nuevos lectores de VETAS!**
