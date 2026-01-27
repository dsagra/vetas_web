# SEO Implementation - VETAS.com

## Archivos SEO Agregados

### 1. Meta Tags SEO (menu.html, menu_en.html, menu_br.html)

Se agregaron los siguientes meta tags en cada versión de idioma:

- **Meta Description**: Descripciones optimizadas en español, inglés y portugués
- **Meta Keywords**: Palabras clave relevantes para la industria maderera
- **Meta Author**: VETAS Magazine
- **Meta Robots**: index, follow (para permitir indexación)
- **Open Graph Tags**: Para compartir en redes sociales (Facebook, LinkedIn)
- **Twitter Cards**: Para compartir en Twitter con imágenes
- **Hreflang Tags**: Para indicar versiones en múltiples idiomas
- **Canonical URL**: Para evitar contenido duplicado
- **Geo Tags**: Ubicación geográfica (Buenos Aires, Argentina)

### 2. Datos Estructurados JSON-LD (index.cgi)

Se agregó schema markup para:

- Tipo: Magazine
- Información de la organización
- Datos de contacto (múltiples oficinas)
- Redes sociales
- Idiomas disponibles

### 3. Sitemap.xml

Archivo sitemap que incluye:

- Todas las páginas principales del sitio
- Versiones en 3 idiomas (es, en, pt)
- Prioridades de páginas
- Frecuencia de actualización
- Fecha de última modificación

### 4. Robots.txt

Configuración para bots de búsqueda:

- Permite indexación general
- Bloquea directorios privados (/backup/, /privado/, /cgi-bin/)
- Especifica ubicación del sitemap
- Configuración específica para Googlebot, Bingbot, Slurp

## Checklist de Optimización SEO

### ✅ Completado

- [x] Meta tags básicos (title, description, keywords)
- [x] Open Graph tags para redes sociales
- [x] Twitter Card tags
- [x] Canonical URLs
- [x] Hreflang tags para multiidioma
- [x] Schema.org JSON-LD (Magazine/Organization)
- [x] Sitemap.xml con multiidioma
- [x] Robots.txt
- [x] Geo-tags para ubicación
- [x] Integración con Google Analytics (ya existente)
- [x] Google Tag Manager (ya existente)

### 📋 Recomendaciones Adicionales

1. **Imagen Open Graph**: Crear/verificar que exista `/images/vetas-og-image.jpg`
   - Tamaño recomendado: 1200x630px
   - Debe representar la marca VETAS

2. **Google Search Console**:
   - Registrar el sitio en Google Search Console
   - Enviar el sitemap.xml: https://www.vetas.com/sitemap.xml
   - Verificar propiedad del dominio

3. **Bing Webmaster Tools**:
   - Registrar en Bing Webmaster Tools
   - Enviar sitemap

4. **Rich Snippets Testing**:
   - Probar en Google Rich Results Test: https://search.google.com/test/rich-results
   - Verificar que los datos estructurados se lean correctamente

5. **Page Speed**:
   - Optimizar imágenes (compresión, formato WebP)
   - Implementar lazy loading para imágenes
   - Minificar CSS y JavaScript

6. **SSL/HTTPS**:
   - Verificar que todo el sitio esté en HTTPS
   - Actualizar enlaces internos para usar HTTPS

7. **Alt Tags en Imágenes**:
   - Agregar atributos alt descriptivos a todas las imágenes

8. **Enlaces Internos**:
   - Crear breadcrumbs
   - Mejorar la estructura de enlaces internos

## Verificación

### Herramientas para verificar SEO:

1. **Google Search Console**: https://search.google.com/search-console
2. **Google Rich Results Test**: https://search.google.com/test/rich-results
3. **Google PageSpeed Insights**: https://pagespeed.web.dev/
4. **GTmetrix**: https://gtmetrix.com/
5. **Screaming Frog**: Para auditoría completa del sitio
6. **Ahrefs/SEMrush**: Para análisis de keywords y backlinks

### URLs a verificar:

```bash
# Verificar que sitemap sea accesible
https://www.vetas.com/sitemap.xml

# Verificar robots.txt
https://www.vetas.com/robots.txt

# Verificar hreflang
https://www.vetas.com/index.cgi?i=es
https://www.vetas.com/index.cgi?i=en
https://www.vetas.com/index.cgi?i=br
```

## Keywords Target

### Español:

- vetas
- revista madera
- industria maderera
- carpintería
- muebles
- aserradero
- forestal
- ferias madera

### English:

- vetas
- wood magazine
- timber industry
- carpentry
- furniture
- sawmill
- forestry
- wood fairs

### Português:

- vetas
- revista madeira
- indústria madeireira
- carpintaria
- móveis
- serraria
- florestal
- feiras madeira

## Notas

- Todos los meta tags usan codificación HTML entities para caracteres especiales (á = &aacute;)
- El sitemap incluye hreflang tags para indicar versiones de idioma
- JSON-LD usa escape (\@) para @ en el contexto
- Los errores de linting en archivos HTML son del código jQuery escapado y no afectan funcionalidad
