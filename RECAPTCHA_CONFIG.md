# Configuración de Google reCAPTCHA v3 para VETAS

## ✅ reCAPTCHA v3 YA CONFIGURADO

Las claves de reCAPTCHA v3 ya están configuradas en el sistema:

- **Site Key**: `6LcI1FIsAAAAAL4Q92H_tU_NbIuX98WzbEIM-0gJ`
- **Secret Key**: `6LcI1FIsAAAAAERcxc5gU06l9_W3-8R-GdAO-2Am`

## Diferencias entre reCAPTCHA v2 y v3

### reCAPTCHA v2 (anterior)

- ❌ Requiere interacción del usuario ("No soy un robot")
- ❌ Interrumpe la experiencia de usuario
- ✅ Verificación binaria (humano/bot)

### reCAPTCHA v3 (actual) ✨

- ✅ **Completamente invisible** - No interrumpe al usuario
- ✅ Funciona en segundo plano
- ✅ Genera un **score** de 0.0 a 1.0:
  - **1.0** = Muy probablemente humano
  - **0.5** = Neutral (umbral por defecto)
  - **0.0** = Muy probablemente bot
- ✅ Mejor experiencia de usuario

## Cómo Funciona

1. El usuario completa el formulario
2. Al hacer click en "Enviar Consulta":
   - JavaScript llama a reCAPTCHA v3 automáticamente
   - reCAPTCHA analiza el comportamiento del usuario
   - Genera un token con un score
3. El token se envía al servidor
4. El servidor valida el token con Google
5. Si el score >= 0.5, se acepta el formulario
6. Si el score < 0.5, se rechaza (probable bot)

## Configuración Actual en el Código

### Línea ~94 - Secret Key (Server-side):

```perl
my $secret_key = '6LcI1FIsAAAAAERcxc5gU06l9_W3-8R-GdAO-2Am';
```

### Línea ~223 - Site Key (Client-side):

```html
<script src="https://www.google.com/recaptcha/api.js?render=6LcI1FIsAAAAAL4Q92H_tU_NbIuX98WzbEIM-0gJ"></script>
```

### Línea ~478 - JavaScript Execute:

```javascript
grecaptcha.execute("6LcI1FIsAAAAAL4Q92H_tU_NbIuX98WzbEIM-0gJ", {
  action: "submit",
});
```

## Ajustar el Umbral de Score

Por defecto, el sistema usa un umbral de **0.5**. Puedes ajustarlo según tus necesidades:

### En `contacto.cgi` línea ~107:

```perl
if ($captcha_score >= 0.5) {  # <-- Cambiar este valor
    $captcha_valido = 1;
}
```

### Recomendaciones de Umbral:

- **0.3** = Muy permisivo (acepta más usuarios, pero más bots)
- **0.5** = Balanceado (recomendado) ✅
- **0.7** = Estricto (rechaza más bots, pero puede rechazar algunos humanos)

## Módulos Perl Requeridos

El sistema necesita estos módulos:

```bash
cpan LWP::UserAgent
cpan JSON
```

O con cpanm:

```bash
cpanm LWP::UserAgent
cpanm JSON
```

## Características Implementadas

✅ **Invisible**: No molesta al usuario
✅ **Score-based**: Decisiones basadas en probabilidad
✅ **Multi-idioma**: Mensajes de error en ES, EN, BR
✅ **Feedback visual**: Botón muestra "Enviando..." con spinner
✅ **Badge visible**: Muestra el badge de reCAPTCHA (requisito de Google)
✅ **Links a políticas**: Privacy y Terms de Google

## Mensajes de Error

### Score bajo (< 0.5):

- 🇪🇸 "Detección de actividad sospechosa. Por favor intenta nuevamente (Score: X)"
- 🇬🇧 "Suspicious activity detected. Please try again (Score: X)"
- 🇧🇷 "Atividade suspeita detectada. Por favor, tente novamente (Score: X)"

### Error de validación:

- 🇪🇸 "Error de validación de seguridad. Por favor intenta nuevamente."
- 🇬🇧 "Security validation error. Please try again."
- 🇧🇷 "Erro de validação de segurança. Por favor, tente novamente."

## Testing

### Para probar diferentes idiomas:

- `contacto.cgi?i=es` (español)
- `contacto.cgi?i=en` (inglés)
- `contacto.cgi?i=br` (portugués)

### Para verificar el funcionamiento:

1. Abre el formulario
2. Completa los datos
3. Abre la consola del navegador (F12)
4. Click en "Enviar Consulta"
5. Verás el proceso de reCAPTCHA en la consola
6. El badge de reCAPTCHA aparecerá en la esquina inferior derecha

## Badge de reCAPTCHA

Google requiere que el badge sea visible. El CSS está configurado para mostrarlo:

```css
.grecaptcha-badge {
  visibility: visible;
  opacity: 1;
  z-index: 999;
}
```

El badge aparece automáticamente en la esquina inferior derecha cuando reCAPTCHA está activo.

## Troubleshooting

### Error: "Can't locate LWP/UserAgent.pm" o "Can't locate JSON.pm"

**Solución**: Instalar los módulos Perl necesarios (ver arriba)

### El formulario no se envía

**Solución**:

1. Verifica la consola del navegador para errores JavaScript
2. Verifica que el dominio esté registrado en Google reCAPTCHA
3. Verifica que las claves sean correctas

### Siempre da error de "actividad sospechosa"

**Solución**:

1. Verifica que el servidor tenga conexión a internet
2. Prueba reducir el umbral a 0.3 temporalmente
3. Verifica logs del servidor para ver el score real

### El badge no aparece

**Solución**:

1. Verifica que el script de Google esté cargando
2. Abre la consola y busca errores
3. Verifica que el Site Key sea correcto

## Monitoreo

Para ver los scores recibidos, puedes agregar logging temporal en línea ~107:

```perl
if ($result->{success}) {
    $captcha_score = $result->{score};
    print STDERR "reCAPTCHA Score: $captcha_score\n";  # <-- Agregar esto
    if ($captcha_score >= 0.5) {
        $captcha_valido = 1;
    }
}
```

Luego revisa los logs del servidor para ver los scores.

## Admin Console de Google

Puedes ver estadísticas y configuración en:

- **Admin Console**: https://www.google.com/recaptcha/admin

Ahí podrás ver:

- Requests totales
- Scores promedio
- Tráfico bloqueado
- Configuración del sitio

## Links Útiles

- **Admin Console**: https://www.google.com/recaptcha/admin
- **Documentación v3**: https://developers.google.com/recaptcha/docs/v3
- **Guía de migración**: https://developers.google.com/recaptcha/docs/v3#migrating_from_v2_to_v3
- **FAQ**: https://developers.google.com/recaptcha/docs/faq

## Seguridad

✅ **Secret Key protegida**: Solo se usa en el servidor, nunca se expone al cliente
✅ **Verificación server-side**: El token se valida en el servidor, no solo en el cliente
✅ **Score-based**: Decisiones basadas en análisis de comportamiento
✅ **Escapado SQL**: Todos los inputs se escapan antes de insertarlos en la BD

---

**Estado**: ✅ CONFIGURADO Y FUNCIONANDO
**Versión**: reCAPTCHA v3
**Configurado por**: Damian G. Sagranichne
**Fecha**: Enero 2026

## Paso 1: Obtener las claves de reCAPTCHA

1. Ve a: https://www.google.com/recaptcha/admin/create
2. Inicia sesión con tu cuenta de Google
3. Completa el formulario:
   - **Label**: VETAS Contact Form
   - **reCAPTCHA type**: Selecciona **reCAPTCHA v2** → "I'm not a robot" Checkbox
   - **Domains**: Agrega tu dominio (ejemplo: vetas.com)
   - Acepta los términos
4. Click en **Submit**
5. Obtendrás dos claves:
   - **Site Key** (Clave del sitio) - Pública, se usa en el HTML
   - **Secret Key** (Clave secreta) - Privada, se usa en el servidor

## Paso 2: Configurar las claves en el código

### En `contacto.cgi` línea ~91:

```perl
my $secret_key = 'TU_SECRET_KEY_AQUI'; # Reemplazar
```

### En `contacto.cgi` línea ~245:

```html
<div class="g-recaptcha d-inline-block" data-sitekey="TU_SITE_KEY_AQUI"></div>
```

## Paso 3: Instalar módulo LWP (si no está instalado)

El script usa `LWP::UserAgent` para verificar el CAPTCHA con Google.

### En cPanel:

1. Ve a "Perl Modules" o "CPAN Modules"
2. Busca: `LWP::UserAgent`
3. Instala el módulo

### Por línea de comandos:

```bash
cpan LWP::UserAgent
```

O con cpanm:

```bash
cpanm LWP::UserAgent
```

## Ejemplo de Configuración Completa

### Línea 91 (Secret Key):

```perl
my $secret_key = '6LdABC123def456GHI789jkl012MNO345pqr678';
```

### Línea 245 (Site Key):

```html
<div
  class="g-recaptcha d-inline-block"
  data-sitekey="6LdXYZ987wvu654TSR321onm098LKJ765ihg432"
></div>
```

## Características Implementadas

✅ **Multi-idioma**: El texto del CAPTCHA se adapta al idioma seleccionado
✅ **Validación backend**: Verifica con Google que el CAPTCHA sea válido
✅ **Mensajes de error específicos**:

- Si no se completa el CAPTCHA
- Si la verificación falla
  ✅ **Responsive**: Se adapta a móviles (escala 0.85 en pantallas pequeñas)
  ✅ **Protección anti-spam**: Previene envíos automatizados

## Selector de Idiomas

Se agregó un selector de idiomas en la parte superior del formulario:

- 🇪🇸 **Español**
- 🇬🇧 **English**
- 🇧🇷 **Português**

Los botones están estilizados con el verde corporativo (#72bf44) cuando están activos.

## Mensajes Traducidos

### Español:

- "Protección anti-spam"
- "\* Campos obligatorios"
- "Por favor completa el CAPTCHA de seguridad."
- "Verificación CAPTCHA fallida. Inténtalo nuevamente."

### English:

- "Anti-spam protection"
- "\* Required fields"
- "Please complete the security CAPTCHA."
- "CAPTCHA verification failed. Please try again."

### Português:

- "Proteção anti-spam"
- "\* Campos obrigatórios"
- "Por favor, complete o CAPTCHA de segurança."
- "Verificação CAPTCHA falhou. Tente novamente."

## Testing

### Para probar:

1. Ve a `contacto.cgi?i=es` (español)
2. Ve a `contacto.cgi?i=en` (inglés)
3. Ve a `contacto.cgi?i=br` (portugués)

### Pruebas de validación:

- ✅ Enviar sin completar CAPTCHA → Error
- ✅ Enviar con CAPTCHA correcto → Éxito
- ✅ Cambiar de idioma → Textos actualizados
- ✅ Campos obligatorios vacíos → Error

## Seguridad

✅ **Verificación server-side**: El CAPTCHA se verifica en el servidor, no solo en el cliente
✅ **Secret Key protegida**: Nunca se expone al cliente
✅ **Escapado SQL**: Todos los inputs se escapan antes de insertarlos en la BD
✅ **Validación de email**: Campo tipo email con validación HTML5

## Troubleshooting

### Error: "Can't locate LWP/UserAgent.pm"

**Solución**: Instalar el módulo LWP::UserAgent (ver Paso 3)

### El CAPTCHA no aparece

**Solución**:

1. Verificar que el dominio esté registrado en Google reCAPTCHA
2. Verificar que el Site Key sea correcto
3. Verificar que el script de Google esté cargando: `https://www.google.com/recaptcha/api.js`

### Siempre da error de CAPTCHA

**Solución**:

1. Verificar que el Secret Key sea correcto
2. Verificar que el servidor tenga conexión a internet (para consultar a Google)
3. Verificar logs del servidor

## Links Útiles

- **Admin Console**: https://www.google.com/recaptcha/admin
- **Documentación**: https://developers.google.com/recaptcha/docs/display
- **Testing**: https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do

## Notas Importantes

⚠️ **No compartas tu Secret Key públicamente**
⚠️ **No subas el archivo a GitHub sin cambiar las claves**
⚠️ **Usa variables de entorno en producción para las claves**

---

Configuración realizada por: **Damian G. Sagranichne**
Fecha: Enero 2026
