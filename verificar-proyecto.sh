#!/bin/bash

################################################################################
# SCRIPT DE VERIFICACIÓN - SECCIONES VETAS
# Verifica que todos los archivos estén presentes y correctos
################################################################################

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Contadores
SUCCESS=0
WARNINGS=0
ERRORS=0

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🔍 VERIFICACIÓN DE SECCIONES VETAS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

################################################################################
# FUNCIÓN: Verificar archivo existe
################################################################################
check_file() {
  local file=$1
  local description=$2
  
  if [ -f "$file" ]; then
    echo -e "${GREEN}✅${NC} $description"
    ((SUCCESS++))
    return 0
  else
    echo -e "${RED}❌${NC} $description ${RED}(FALTA)${NC}"
    ((ERRORS++))
    return 1
  fi
}

################################################################################
# FUNCIÓN: Verificar directorio existe
################################################################################
check_dir() {
  local dir=$1
  local description=$2
  
  if [ -d "$dir" ]; then
    echo -e "${GREEN}✅${NC} $description"
    ((SUCCESS++))
    return 0
  else
    echo -e "${YELLOW}⚠️${NC} $description ${YELLOW}(NO EXISTE)${NC}"
    ((WARNINGS++))
    return 1
  fi
}

################################################################################
# FUNCIÓN: Verificar contenido de archivo
################################################################################
check_content() {
  local file=$1
  local search=$2
  local description=$3
  
  if [ -f "$file" ]; then
    if grep -q "$search" "$file"; then
      echo -e "${GREEN}✅${NC} $description"
      ((SUCCESS++))
      return 0
    else
      echo -e "${YELLOW}⚠️${NC} $description ${YELLOW}(CONTENIDO FALTANTE)${NC}"
      ((WARNINGS++))
      return 1
    fi
  else
    echo -e "${RED}❌${NC} $description ${RED}(ARCHIVO NO EXISTE)${NC}"
    ((ERRORS++))
    return 1
  fi
}

################################################################################
# 1. VERIFICAR ESTRUCTURA DE DIRECTORIOS
################################################################################
echo "📁 1. ESTRUCTURA DE DIRECTORIOS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

check_dir "css" "Directorio CSS"
check_dir "components" "Directorio Components"
check_dir "sql" "Directorio SQL"

echo ""

################################################################################
# 2. VERIFICAR ARCHIVOS CSS
################################################################################
echo "🎨 2. ARCHIVOS CSS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

check_file "css/suscripcion.css" "CSS Sección Suscripción"
check_file "css/anunciar.css" "CSS Sección Anunciar"

# Verificar contenido crítico en CSS
check_content "css/suscripcion.css" ".vetas-suscripcion" "CSS contiene clase principal suscripción"
check_content "css/anunciar.css" ".vetas-anunciar" "CSS contiene clase principal anunciar"

echo ""

################################################################################
# 3. VERIFICAR COMPONENTES HTML
################################################################################
echo "📄 3. COMPONENTES HTML"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

check_file "components/seccion-suscripcion.html" "HTML Suscripción (Español)"
check_file "components/seccion-suscripcion-en.html" "HTML Suscripción (Inglés)"
check_file "components/seccion-suscripcion-br.html" "HTML Suscripción (Portugués)"
check_file "components/seccion-anunciar.html" "HTML Anunciar"

# Verificar contenido crítico en HTML
check_content "components/seccion-suscripcion.html" "vetas-suscripcion" "HTML suscripción tiene clase correcta"
check_content "components/seccion-suscripcion.html" 'type="email"' "HTML tiene input de email"
check_content "components/seccion-anunciar.html" "vetas-anunciar" "HTML anunciar tiene clase correcta"

echo ""

################################################################################
# 4. VERIFICAR ARCHIVOS DE BASE DE DATOS
################################################################################
echo "🗄️  4. BASE DE DATOS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

check_file "sql/create_suscriptores_table.sql" "Script SQL Tabla Suscriptores"
check_content "sql/create_suscriptores_table.sql" "CREATE TABLE" "SQL contiene CREATE TABLE"
check_content "sql/create_suscriptores_table.sql" "SUSCRIPTORES" "SQL crea tabla SUSCRIPTORES"

echo ""

################################################################################
# 5. VERIFICAR PÁGINAS DE RESPUESTA
################################################################################
echo "📃 5. PÁGINAS DE RESPUESTA"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

check_file "gracias-suscripcion.html" "Página de Agradecimiento"
check_content "gracias-suscripcion.html" "Gracias" "Página contiene mensaje de agradecimiento"

echo ""

################################################################################
# 6. VERIFICAR ARCHIVOS DE DEMO Y EJEMPLOS
################################################################################
echo "🎬 6. DEMO Y EJEMPLOS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

check_file "demo-secciones.html" "Demo Completa"
check_file "ejemplo-integracion.cgi" "Ejemplo de Integración CGI"

echo ""

################################################################################
# 7. VERIFICAR DOCUMENTACIÓN
################################################################################
echo "📚 7. DOCUMENTACIÓN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

check_file "SECCIONES_README.md" "README Principal"
check_file "QUICK_START.md" "Guía Quick Start"
check_file "GUIA_VISUAL.md" "Guía Visual"
check_file "RESUMEN_EJECUTIVO.md" "Resumen Ejecutivo"

echo ""

################################################################################
# 8. VERIFICAR PERMISOS (si es en servidor)
################################################################################
echo "🔐 8. PERMISOS DE ARCHIVOS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -f "ejemplo-integracion.cgi" ]; then
  if [ -x "ejemplo-integracion.cgi" ]; then
    echo -e "${GREEN}✅${NC} CGI tiene permisos de ejecución"
    ((SUCCESS++))
  else
    echo -e "${YELLOW}⚠️${NC} CGI NO tiene permisos de ejecución ${YELLOW}(ejecutar: chmod 755)${NC}"
    ((WARNINGS++))
  fi
fi

echo ""

################################################################################
# 9. VERIFICAR SINTAXIS CSS (básico)
################################################################################
echo "🔧 9. VALIDACIÓN DE SINTAXIS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Verificar llaves balanceadas en CSS
for css_file in css/suscripcion.css css/anunciar.css; do
  if [ -f "$css_file" ]; then
    open_braces=$(grep -o "{" "$css_file" | wc -l)
    close_braces=$(grep -o "}" "$css_file" | wc -l)
    
    if [ $open_braces -eq $close_braces ]; then
      echo -e "${GREEN}✅${NC} $css_file - Sintaxis CSS válida"
      ((SUCCESS++))
    else
      echo -e "${RED}❌${NC} $css_file - Sintaxis CSS inválida (llaves desbalanceadas)"
      ((ERRORS++))
    fi
  fi
done

echo ""

################################################################################
# 10. VERIFICAR ENLACES Y RUTAS
################################################################################
echo "🔗 10. ENLACES Y RUTAS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Verificar que los CSS están referenciados correctamente en demo
if [ -f "demo-secciones.html" ]; then
  if grep -q 'href="/css/suscripcion.css"' "demo-secciones.html"; then
    echo -e "${GREEN}✅${NC} Demo referencia suscripcion.css"
    ((SUCCESS++))
  else
    echo -e "${YELLOW}⚠️${NC} Demo NO referencia suscripcion.css correctamente"
    ((WARNINGS++))
  fi
  
  if grep -q 'href="/css/anunciar.css"' "demo-secciones.html"; then
    echo -e "${GREEN}✅${NC} Demo referencia anunciar.css"
    ((SUCCESS++))
  else
    echo -e "${YELLOW}⚠️${NC} Demo NO referencia anunciar.css correctamente"
    ((WARNINGS++))
  fi
fi

echo ""

################################################################################
# RESUMEN FINAL
################################################################################
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📊 RESUMEN DE VERIFICACIÓN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${GREEN}✅ Exitosos:${NC} $SUCCESS"
echo -e "${YELLOW}⚠️  Advertencias:${NC} $WARNINGS"
echo -e "${RED}❌ Errores:${NC} $ERRORS"
echo ""

TOTAL=$((SUCCESS + WARNINGS + ERRORS))
if [ $TOTAL -gt 0 ]; then
  PERCENTAGE=$((SUCCESS * 100 / TOTAL))
  echo -e "Completitud: ${BLUE}${PERCENTAGE}%${NC}"
  echo ""
fi

################################################################################
# RECOMENDACIONES
################################################################################
if [ $ERRORS -gt 0 ]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo -e "${RED}⚠️  ACCIÓN REQUERIDA${NC}"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  echo "Hay errores críticos que deben solucionarse antes de continuar."
  echo "Revisa los archivos marcados con ❌ arriba."
  echo ""
  exit 1
elif [ $WARNINGS -gt 0 ]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo -e "${YELLOW}⚠️  ADVERTENCIAS${NC}"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  echo "Hay algunas advertencias pero el proyecto es funcional."
  echo "Revisa los items marcados con ⚠️  si es necesario."
  echo ""
  exit 0
else
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo -e "${GREEN}✅ TODO PERFECTO${NC}"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  echo "Todos los archivos están presentes y correctos."
  echo "El proyecto está listo para implementación."
  echo ""
  echo "Próximos pasos:"
  echo "1. Abre demo-secciones.html en tu navegador"
  echo "2. Revisa QUICK_START.md para implementación"
  echo "3. Sube archivos al servidor"
  echo ""
  exit 0
fi
