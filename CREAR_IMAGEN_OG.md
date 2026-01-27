# Cómo Crear la Imagen Open Graph para VETAS

La imagen Open Graph es la que aparece cuando compartes tu sitio en redes sociales (Facebook, LinkedIn, Twitter, WhatsApp).

## Especificaciones Técnicas

- **Tamaño recomendado**: 1200 x 630 píxeles
- **Formato**: JPG o PNG
- **Peso máximo**: menos de 1 MB
- **Nombre del archivo**: `vetas-og-image.jpg`
- **Ubicación**: `/images/vetas-og-image.jpg` (en tu servidor)

---

## 🎨 Opción 1: Usar Canva (Recomendado - Más Fácil)

### Pasos:

1. **Ir a Canva**: https://www.canva.com
2. **Crear diseño personalizado**:
   - Click en "Crear un diseño"
   - Seleccionar "Tamaño personalizado"
   - Ingresar: 1200 x 630 px
3. **Diseñar la imagen**:
   - Agregar el logo de VETAS
   - Agregar texto: "VETAS - El mundo de la madera y el mueble"
   - Usar colores corporativos: #72bf44 (verde), #2c5f2d (verde oscuro)
   - Incluir imágenes de madera/muebles (Canva tiene stock gratuito)
4. **Descargar**:
   - Click en "Compartir" → "Descargar"
   - Formato: JPG
   - Nombre: `vetas-og-image.jpg`

### Plantilla sugerida:

```
┌──────────────────────────────────────────┐
│                                          │
│         [Logo VETAS]                     │
│                                          │
│    VETAS                                 │
│    El mundo de la madera y el mueble    │
│                                          │
│    [Imagen de madera o muebles]         │
│                                          │
└──────────────────────────────────────────┘
```

---

## 🖼️ Opción 2: Usar Figma (Profesional y Gratuito)

1. **Ir a Figma**: https://www.figma.com
2. **Crear archivo nuevo**
3. **Crear frame**: 1200 x 630 px
4. **Diseñar con tus elementos**:
   - Importar logo
   - Agregar texto
   - Colores y fondos
5. **Exportar**:
   - Click derecho en el frame
   - Export → JPG → Download

---

## 🚀 Opción 3: Usar el logo existente con Photoshop/GIMP

Si tienes acceso a `./images/vetaslogo.png`:

### Con Photoshop:

1. Crear nuevo documento: 1200 x 630 px
2. Fondo con degradado verde (#72bf44 a #2c5f2d)
3. Importar vetaslogo.png y centrarlo
4. Agregar texto descriptivo
5. Guardar como JPG

### Con GIMP (Gratuito):

1. Descargar GIMP: https://www.gimp.org/
2. Archivo → Nueva imagen → 1200 x 630 px
3. Usar herramienta de degradado con colores corporativos
4. Archivo → Abrir como capa → vetaslogo.png
5. Agregar texto con la herramienta de texto
6. Exportar como JPG

---

## 📱 Opción 4: Herramientas Online Rápidas

### Meta Tags Generator:

- https://metatags.io/
- Tiene editor visual
- Genera la imagen automáticamente

### Social Image Maker:

- https://www.socialimagemaker.com/
- Templates prediseñados
- Muy rápido

### Bannerbear (Template):

- https://www.bannerbear.com/templates/
- Templates para Open Graph
- Gratis para uso básico

---

## 📤 Subir la Imagen al Servidor

Una vez que tengas la imagen creada:

### Opción A: Via FTP/SFTP

```bash
# Conectar a tu servidor
sftp usuario@vetas.com

# Navegar a la carpeta images
cd /ruta/al/directorio/images

# Subir la imagen
put vetas-og-image.jpg

# Verificar
ls -la
```

### Opción B: Via cPanel

1. Iniciar sesión en cPanel
2. Ir a "Administrador de archivos"
3. Navegar a `/public_html/images/` (o similar)
4. Click en "Subir"
5. Seleccionar `vetas-og-image.jpg`

### Opción C: Via SCP (línea de comandos)

```bash
scp vetas-og-image.jpg usuario@vetas.com:/ruta/images/
```

---

## ✅ Verificar que Funciona

Después de subir la imagen:

1. **Verificar URL directa**:
   - Abrir navegador
   - Ir a: `https://www.vetas.com/images/vetas-og-image.jpg`
   - Debe mostrarse la imagen

2. **Probar en Facebook Debugger**:
   - Ir a: https://developers.facebook.com/tools/debug/
   - Ingresar: `https://www.vetas.com`
   - Click en "Depurar"
   - Click en "Obtener nueva información de extracción"
   - Verificar que se muestre la imagen

3. **Probar en Twitter Card Validator**:
   - Ir a: https://cards-dev.twitter.com/validator
   - Ingresar URL del sitio
   - Verificar preview

4. **Probar en LinkedIn Inspector**:
   - Ir a: https://www.linkedin.com/post-inspector/
   - Ingresar URL
   - Ver preview

---

## 🎨 Elementos de Diseño Sugeridos

### Colores Corporativos:

- Verde principal: `#72bf44`
- Verde oscuro: `#2c5f2d`
- Verde claro: `#e8f5e3`
- Blanco: `#ffffff`

### Tipografía:

- Título: Bold, 60-80px
- Subtítulo: Regular, 32-40px
- Usar fuentes sans-serif (Arial, Helvetica, Roboto)

### Contenido Sugerido:

```
┌──────────────────────────────────────────┐
│  [Logo en esquina superior izquierda]   │
│                                          │
│          VETAS                           │
│  La revista líder de la industria       │
│  de la madera y el mueble               │
│  en América Latina                       │
│                                          │
│  [Imagen de fondo: textura madera]      │
│                                          │
│  www.vetas.com                          │
└──────────────────────────────────────────┘
```

---

## 🔍 Imágenes de Stock Gratuitas

Si necesitas imágenes de madera/muebles:

- **Unsplash**: https://unsplash.com/ (buscar "wood", "furniture")
- **Pexels**: https://www.pexels.com/
- **Pixabay**: https://pixabay.com/
- **Freepik**: https://www.freepik.com/ (requiere atribución)

---

## 📋 Checklist Final

- [ ] Imagen creada en 1200 x 630 px
- [ ] Incluye logo de VETAS
- [ ] Texto descriptivo legible
- [ ] Colores corporativos
- [ ] Peso menor a 1 MB
- [ ] Formato JPG
- [ ] Subida al servidor en `/images/`
- [ ] URL accesible: https://www.vetas.com/images/vetas-og-image.jpg
- [ ] Probada en Facebook Debugger
- [ ] Probada en Twitter Card Validator

---

## 💡 Consejo Rápido

Si tienes prisa, la forma MÁS RÁPIDA es:

1. Ir a https://metatags.io/
2. Usar su editor visual
3. Subir tu logo
4. Agregar texto
5. Descargar la imagen generada
6. Subirla a tu servidor

¡Listo! En 5 minutos tendrás tu imagen Open Graph funcionando.
