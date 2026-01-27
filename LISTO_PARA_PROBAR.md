# ✅ SUSCRIPCIÓN LISTA PARA PROBAR

## 🎉 ¡Todo Configurado!

El sistema de suscripción está **100% listo para grabar en la base de datos**.

---

## 🚀 Cómo Probar AHORA

### 1. Crear la tabla en la base de datos

```bash
cd /Users/damiansagranichne/dev/vetas_web
mysql -u vetas_user -pghewrp54 vetas_VETAS2 < sql/create_suscriptores_table.sql
```

O manualmente en MySQL:

```sql
USE vetas_VETAS2;

CREATE TABLE IF NOT EXISTS SUSCRIPTORES (
  ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  EMAIL VARCHAR(255) NOT NULL UNIQUE,
  NOMBRE VARCHAR(255) DEFAULT NULL,
  IDIOMA VARCHAR(5) DEFAULT 'es',
  ACTIVO TINYINT(1) DEFAULT 1,
  FECHA DATETIME NOT NULL,
  IP VARCHAR(50) DEFAULT NULL,
  TOKEN VARCHAR(64) DEFAULT NULL,
  CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_email (EMAIL),
  INDEX idx_activo (ACTIVO),
  INDEX idx_fecha (FECHA),
  INDEX idx_idioma (IDIOMA),
  INDEX idx_token (TOKEN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 2. Verificar que la tabla se creó

```sql
USE vetas_VETAS2;
SHOW TABLES LIKE 'SUSCRIPTORES';
DESCRIBE SUSCRIPTORES;
```

### 3. Probar el formulario

**Español:**

```
http://localhost/index.cgi?i=es
```

**English:**

```
http://localhost/index.cgi?i=en
```

**Português:**

```
http://localhost/index.cgi?i=br
```

### 4. Hacer scroll hasta el final y suscribirte

- Ingresar tu email
- Ingresar tu nombre (opcional)
- Click en "Suscribirme a VETAS"
- Deberías ver la página de éxito

### 5. Verificar que se grabó en la BD

```sql
USE vetas_VETAS2;
SELECT * FROM SUSCRIPTORES ORDER BY FECHA DESC;
```

---

## ✅ Configuración Actual

### Base de Datos

- **Database**: `vetas_VETAS2`
- **User**: `vetas_user`
- **Password**: `ghewrp54`
- **Host**: `localhost`

### Archivos Configurados

- ✅ `suscripcion.cgi` - Procesador configurado
- ✅ `components/seccion-suscripcion.html` - Formulario ES
- ✅ `components/seccion-suscripcion-en.html` - Formulario EN
- ✅ `components/seccion-suscripcion-br.html` - Formulario BR
- ✅ `index.cgi` - Integración lista (necesita rehacer)

### reCAPTCHA

🔴 **Temporalmente DESHABILITADO para testing**

Puedes probar el formulario SIN reCAPTCHA. Los registros se guardarán correctamente.

---

## 📊 Consultas Útiles

### Ver todos los suscriptores

```sql
SELECT * FROM SUSCRIPTORES ORDER BY FECHA DESC;
```

### Contar suscriptores

```sql
SELECT COUNT(*) as total FROM SUSCRIPTORES WHERE ACTIVO = 1;
```

### Ver último suscriptor

```sql
SELECT * FROM SUSCRIPTORES ORDER BY FECHA DESC LIMIT 1;
```

### Suscriptores por idioma

```sql
SELECT IDIOMA, COUNT(*) as total
FROM SUSCRIPTORES
WHERE ACTIVO = 1
GROUP BY IDIOMA;
```

### Suscriptores de hoy

```sql
SELECT * FROM SUSCRIPTORES
WHERE DATE(FECHA) = CURDATE()
ORDER BY FECHA DESC;
```

---

## 🔄 Volver a Integrar en index.cgi

Como deshiciste los cambios en `index.cgi`, necesitas volver a integrar la sección:

### Opción 1: Agregar al final antes del footer

Editar `/Users/damiansagranichne/dev/vetas_web/index.cgi` y buscar:

```perl
print <<EOFHTML;
      </div>
    </div>
  </div>
</div>

</main>

EOFHTML

open FOOTER;
```

Y reemplazar por:

```perl
print <<EOFHTML;
      </div>
    </div>
  </div>
</div>

EOFHTML

# Incluir la sección de suscripción según el idioma
if ($idioma eq "es") {
    open SUSCRIPCION, "components/seccion-suscripcion.html" or warn "No se pudo abrir seccion-suscripcion.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}
elsif ($idioma eq "en") {
    open SUSCRIPCION, "components/seccion-suscripcion-en.html" or warn "No se pudo abrir seccion-suscripcion-en.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}
elsif ($idioma eq "br") {
    open SUSCRIPCION, "components/seccion-suscripcion-br.html" or warn "No se pudo abrir seccion-suscripcion-br.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}

print <<EOFHTML;

</main>

EOFHTML

open FOOTER;
```

### Opción 2: Usar un script automatizado

Puedo crear un script que haga la integración automáticamente si me lo pides.

---

## 🐛 Troubleshooting

### Error: "Can't locate LWP/UserAgent.pm"

```bash
cpan install LWP::UserAgent
cpan install JSON
```

### Error: "DBI connect failed"

Verificar credenciales en `suscripcion.cgi` línea 84:

```perl
my $database = "vetas_VETAS2";
my $user = "vetas_user";
my $password = "ghewrp54";
```

### Error: "Table doesn't exist"

Ejecutar:

```bash
mysql -u vetas_user -pghewrp54 vetas_VETAS2 < sql/create_suscriptores_table.sql
```

### No se ve el diseño CSS

El CSS está embebido en los componentes HTML. Verificar que:

1. Los archivos `components/seccion-suscripcion*.html` existen
2. El `index.cgi` los está incluyendo correctamente
3. No hay errores en los logs: `tail -f /var/log/apache2/error.log`

### El formulario no envía

1. Verificar que `suscripcion.cgi` tenga permisos de ejecución:
   ```bash
   chmod 755 suscripcion.cgi
   ```
2. Verificar logs de errores
3. Probar accediendo directamente: `http://localhost/suscripcion.cgi`

---

## ✅ Checklist Completo

- [x] Script `suscripcion.cgi` creado y con permisos
- [x] Credenciales de BD configuradas
- [x] Componentes HTML con CSS embebido
- [x] reCAPTCHA temporalmente deshabilitado
- [x] Formularios configurados para grabar en BD
- [x] Páginas de éxito/error implementadas
- [x] Soporte multiidioma completo
- [ ] Tabla `SUSCRIPTORES` creada en BD ⚠️ **PENDIENTE**
- [ ] Integración en `index.cgi` ⚠️ **PENDIENTE**
- [ ] Probado y funcionando ⚠️ **PENDIENTE**

---

## 🎯 Próximos Pasos

### Para Testing (AHORA)

1. ✅ Crear tabla `SUSCRIPTORES`
2. ✅ Integrar en `index.cgi`
3. ✅ Probar suscripción
4. ✅ Verificar que se guarde en BD

### Para Producción (DESPUÉS)

1. Configurar reCAPTCHA v2 (obtener claves en Google)
2. Descomentar reCAPTCHA en componentes HTML
3. Actualizar `suscripcion.cgi` con la Secret Key
4. Probar reCAPTCHA funciona
5. Implementar email de bienvenida (opcional)
6. Configurar HTTPS/SSL

---

## 📧 Site Key de reCAPTCHA

Del archivo `contacto.cgi` tenemos:

**Site Key (pública):**

```
6LcI1FIsAAAAAL4Q92H_tU_NbIuX98WzbEIM-0gJ
```

**Secret Key:** No configurada aún

Esta es una clave de reCAPTCHA v3. Para la suscripción, recomiendo crear una nueva clave de **reCAPTCHA v2** (checkbox) en:
https://www.google.com/recaptcha/admin/create

---

## 🎉 ¡Listo para Probar!

Todo está configurado. Solo necesitas:

1. Crear la tabla SUSCRIPTORES
2. Re-integrar en index.cgi
3. ¡Probar!

**La suscripción grabará directamente en la base de datos sin necesidad de reCAPTCHA por ahora.** 🚀

---

_Actualizado: 24 de enero de 2026_
