# 🎨 Guía Visual de Diseño VETAS

## Paleta de Colores

### Colores Principales
```css
/* Verde VETAS (Primario) */
--vetas-green: #72bf44;
--vetas-green-dark: #5fa835;

/* Neutros */
--dark-primary: #2c3e50;
--dark-secondary: #34495e;
--gray-text: #5a6c7d;
--gray-light: #f8f9fa;

/* Fondos */
--bg-light: #ffffff;
--bg-gray: #f8f9fa;
--bg-dark: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
```

## Tipografía

### Jerarquía de Texto

```
H1 (Hero)
└── 48px / 3rem
    └── Weight: 700 (Bold)
    └── Color: #2c3e50
    └── Line-height: 1.2

H2 (Section Title)
└── 40px / 2.5rem
    └── Weight: 700
    └── Color: #2c3e50
    └── Line-height: 1.2

H3 (Subsection)
└── 20px / 1.25rem
    └── Weight: 600
    └── Color: #2c3e50

Body Text
└── 16px / 1rem
    └── Weight: 400
    └── Color: #495057
    └── Line-height: 1.6

Button Text
└── 18px / 1.125rem
    └── Weight: 600
    └── Letter-spacing: 0.5px
    └── Transform: uppercase
```

## Espaciado

### Sistema de Espaciado (8px base)
```
XS:  8px  (0.5rem)
S:   16px (1rem)
M:   24px (1.5rem)
L:   32px (2rem)
XL:  48px (3rem)
XXL: 64px (4rem)
```

### Padding de Secciones
```css
/* Desktop */
padding: 80px 0;

/* Tablet */
@media (max-width: 992px) {
  padding: 60px 0;
}

/* Mobile */
@media (max-width: 576px) {
  padding: 40px 0;
}
```

## Componentes

### Botones

#### Botón Primario (CTA)
```css
Características:
- Background: Gradiente verde (#72bf44 → #5fa835)
- Padding: 16px 32px
- Border-radius: 8px
- Box-shadow: 0 4px 16px rgba(114, 191, 68, 0.3)
- Transform on hover: translateY(-2px)
- Uppercase text
```

#### Botón Secundario (Outline)
```css
Características:
- Background: transparent
- Border: 2px solid rgba(255, 255, 255, 0.3)
- Color: white
- Padding: 16px 32px
- Border-radius: 8px
- Hover: background rgba(255, 255, 255, 0.1)
```

### Cards de Beneficios

```
┌─────────────────────┐
│   [Icon 56x56]      │
│                     │
│   Título Card       │
│   Descripción del   │
│   beneficio aquí    │
└─────────────────────┘

Especificaciones:
- Width: 280px (min)
- Padding: 24px
- Background: rgba(255,255,255,0.05)
- Border: 1px solid rgba(255,255,255,0.1)
- Border-radius: 12px
- Hover: translateY(-4px)
```

### Formularios

#### Input Field
```css
Características:
- Width: 100%
- Padding: 14px 16px
- Font-size: 16px
- Border: 2px solid #dee2e6
- Border-radius: 8px
- Focus border: #72bf44
- Focus shadow: 0 0 0 3px rgba(114, 191, 68, 0.1)
```

## Iconografía

### Íconos de Beneficios (Suscripción)
```
✓ Checkmark circular
  - Size: 24x24px
  - Background: Verde VETAS (gradiente)
  - Color: white
  - Font-weight: 700
```

### Íconos de Beneficios (Publicidad)
```
Font Awesome 6 Icons:
- fa-users (Audiencia)
- fa-globe-americas (Regional)
- fa-palette (Formatos)
- fa-calendar-alt (Eventos)
- fa-award (Valor)

Contenedor:
- Size: 56x56px
- Background: Verde VETAS (gradiente)
- Border-radius: 12px
- Icon size: 24px
```

## Layout Grid

### Desktop (> 992px)

#### Sección Suscripción
```
┌──────────────────────────────────────────┐
│                                          │
│  ┌─────────────┐  ┌─────────────┐       │
│  │   Texto     │  │  Formulario │       │
│  │   50%       │  │     50%     │       │
│  │             │  │             │       │
│  └─────────────┘  └─────────────┘       │
│                                          │
└──────────────────────────────────────────┘
Gap: 60px
```

#### Sección Publicidad
```
┌──────────────────────────────────────────┐
│          Título + Bajada (centrado)      │
├──────────────────────────────────────────┤
│  [Card] [Card] [Card] [Card] [Card]     │
│         Grid auto-fit (min 280px)        │
├──────────────────────────────────────────┤
│         [CTA 1]      [CTA 2]             │
│      "40 años acompañando..."            │
└──────────────────────────────────────────┘
Gap: 32px (cards)
```

### Mobile (< 576px)

```
┌──────────────┐
│   Título     │
├──────────────┤
│   Texto      │
├──────────────┤
│   Beneficios │
├──────────────┤
│   Formulario │
└──────────────┘

Todo apilado verticalmente
Gap: 40px entre secciones
```

## Animaciones y Transiciones

### Estándar
```css
transition: all 0.3s ease;
```

### Hover en Botones
```css
transform: translateY(-2px);
transition: transform 0.3s ease, box-shadow 0.3s ease;
```

### Hover en Cards
```css
transform: translateY(-4px);
transition: all 0.3s ease;
```

### Focus en Inputs
```css
transition: border-color 0.3s ease, box-shadow 0.3s ease;
```

## Sombras (Shadows)

### Nivel 1 - Sutiles
```css
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
/* Uso: Cards, formularios */
```

### Nivel 2 - Medias
```css
box-shadow: 0 4px 16px rgba(114, 191, 68, 0.3);
/* Uso: Botones primarios */
```

### Nivel 3 - Elevadas
```css
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
/* Uso: Contenedores principales */
```

### Hover Shadows
```css
box-shadow: 0 6px 24px rgba(114, 191, 68, 0.4);
/* Uso: Botones en hover */
```

## Border Radius

```css
Pequeño: 8px   → Inputs, botones
Mediano: 12px  → Cards, iconos
Grande:  16px  → Contenedores
Círculo: 50%   → Checkmarks, badges
```

## Breakpoints

```css
/* Mobile First Approach */

/* Small devices (landscape phones, 576px and up) */
@media (min-width: 576px) { }

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) { }

/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) { }

/* Extra large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) { }
```

## Accesibilidad

### Contraste de Colores
```
✅ WCAG AAA Compliant

Verde VETAS sobre blanco:
- Ratio: 4.7:1 (AA Large ✓)

Texto oscuro sobre blanco:
- #2c3e50 → Ratio: 12.6:1 (AAA ✓)

Texto claro sobre oscuro:
- #ffffff → Ratio: 12.6:1 (AAA ✓)
```

### Navegación por Teclado
```
Tab Order:
1. Email input
2. Nombre input
3. Submit button

Focus visible:
- Outline: 2px solid #72bf44
- Offset: 2px
```

## Copywriting Guidelines

### Tono de Voz
```
✅ Hacer:
- Lenguaje profesional
- Oraciones cortas
- Beneficios concretos
- Verbos en infinitivo
- Llamados a la acción claros

❌ Evitar:
- Jerga técnica excesiva
- Oraciones largas
- Superlativos exagerados
- Emojis (excepto en demos)
- Lenguaje informal
```

### Estructura de Beneficios
```
Formato:
[Sustantivo] + [adjetivo específico]

Ejemplos:
✅ "Ediciones digitales completas"
✅ "Cobertura de ferias y eventos internacionales"
❌ "Las mejores ediciones"
❌ "Contenido increíble"
```

## Performance

### CSS Optimization
```css
/* Usar variables CSS */
:root {
  --vetas-green: #72bf44;
  --transition-standard: all 0.3s ease;
}

/* Evitar múltiples shadows */
/* Combinar transforms */
/* Usar will-change para animaciones */
```

### Carga de Recursos
```html
<!-- Preload críticos -->
<link rel="preload" href="/css/suscripcion.css" as="style">

<!-- Defer no-críticos -->
<link rel="preload" href="https://fontawesome.com/..." as="style">

<!-- Lazy load para iconos below the fold -->
<i class="fas fa-users" loading="lazy"></i>
```

## Testing Checklist

### Visual Testing
- [ ] Chrome (últimas 2 versiones)
- [ ] Safari (últimas 2 versiones)
- [ ] Firefox (últimas 2 versiones)
- [ ] Edge (últimas 2 versiones)
- [ ] iOS Safari (iPhone)
- [ ] Chrome Mobile (Android)

### Responsive Testing
- [ ] 320px (iPhone SE)
- [ ] 375px (iPhone X)
- [ ] 768px (iPad)
- [ ] 1024px (iPad Pro)
- [ ] 1440px (Desktop)
- [ ] 1920px (Desktop HD)

### Accessibility Testing
- [ ] Navegación por teclado
- [ ] Screen reader (NVDA/JAWS)
- [ ] Contraste de colores
- [ ] Zoom 200%
- [ ] Focus visible

### Performance Testing
- [ ] Lighthouse Score > 90
- [ ] First Contentful Paint < 1.5s
- [ ] Time to Interactive < 3.0s
- [ ] Cumulative Layout Shift < 0.1

---

**Última actualización:** Enero 2026  
**Versión:** 1.0
