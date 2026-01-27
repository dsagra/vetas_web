#!/bin/bash

# Script para configurar Google reCAPTCHA en la sección de suscripción

echo "============================================"
echo "  Configuración de Google reCAPTCHA"
echo "  Sección: Recibí VETAS en tu email"
echo "============================================"
echo ""

# Verificar si se pasaron las claves como parámetros
if [ $# -eq 2 ]; then
    SITE_KEY="$1"
    SECRET_KEY="$2"
else
    echo "📝 Introduce tus claves de Google reCAPTCHA:"
    echo ""
    echo "Si aún no tienes las claves, ve a:"
    echo "🔗 https://www.google.com/recaptcha/admin/create"
    echo ""
    echo "Configuración recomendada:"
    echo "  - Tipo: reCAPTCHA v2"
    echo "  - Subtipo: Casilla de verificación 'No soy un robot'"
    echo "  - Dominios: www.vetas.com, vetas.com"
    echo ""
    read -p "Site Key (clave pública): " SITE_KEY
    read -p "Secret Key (clave secreta): " SECRET_KEY
fi

# Validar que las claves no estén vacías
if [ -z "$SITE_KEY" ] || [ -z "$SECRET_KEY" ]; then
    echo ""
    echo "❌ Error: Debes proporcionar ambas claves"
    exit 1
fi

echo ""
echo "🔧 Configurando archivos..."
echo ""

# Backup de archivos
backup_dir="backup/recaptcha_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$backup_dir"

# Archivos a configurar
archivos=(
    "components/seccion-suscripcion.html"
    "components/seccion-suscripcion-en.html"
    "components/seccion-suscripcion-br.html"
    "suscripcion.cgi"
)

# Hacer backup
echo "📦 Creando backup en: $backup_dir"
for archivo in "${archivos[@]}"; do
    if [ -f "$archivo" ]; then
        cp "$archivo" "$backup_dir/"
        echo "   ✓ $archivo"
    fi
done
echo ""

# Configurar Site Key en archivos HTML
echo "🔑 Configurando Site Key en componentes HTML..."
for archivo in components/seccion-suscripcion*.html; do
    if [ -f "$archivo" ]; then
        if [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            sed -i '' "s/data-sitekey=\"TU_SITE_KEY_AQUI\"/data-sitekey=\"$SITE_KEY\"/" "$archivo"
        else
            # Linux
            sed -i "s/data-sitekey=\"TU_SITE_KEY_AQUI\"/data-sitekey=\"$SITE_KEY\"/" "$archivo"
        fi
        echo "   ✓ $(basename $archivo)"
    fi
done
echo ""

# Configurar Secret Key en CGI
echo "🔐 Configurando Secret Key en suscripcion.cgi..."
if [ -f "suscripcion.cgi" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/my \$RECAPTCHA_SECRET_KEY = 'TU_SECRET_KEY_AQUI';/my \$RECAPTCHA_SECRET_KEY = '$SECRET_KEY';/" "suscripcion.cgi"
    else
        # Linux
        sed -i "s/my \$RECAPTCHA_SECRET_KEY = 'TU_SECRET_KEY_AQUI';/my \$RECAPTCHA_SECRET_KEY = '$SECRET_KEY';/" "suscripcion.cgi"
    fi
    echo "   ✓ suscripcion.cgi"
fi
echo ""

# Verificar permisos
echo "🔒 Verificando permisos de archivos..."
chmod 755 suscripcion.cgi 2>/dev/null && echo "   ✓ suscripcion.cgi (755)" || echo "   ⚠️  No se pudo cambiar permisos de suscripcion.cgi"
chmod 644 components/seccion-suscripcion*.html 2>/dev/null && echo "   ✓ componentes HTML (644)" || echo "   ⚠️  No se pudo cambiar permisos de componentes"
echo ""

# Verificar que las claves se configuraron correctamente
echo "✅ Verificando configuración..."
site_key_found=0
secret_key_found=0

# Verificar Site Key
if grep -q "data-sitekey=\"$SITE_KEY\"" components/seccion-suscripcion.html 2>/dev/null; then
    echo "   ✓ Site Key configurada correctamente"
    site_key_found=1
else
    echo "   ❌ Site Key NO configurada"
fi

# Verificar Secret Key
if grep -q "my \$RECAPTCHA_SECRET_KEY = '$SECRET_KEY';" suscripcion.cgi 2>/dev/null; then
    echo "   ✓ Secret Key configurada correctamente"
    secret_key_found=1
else
    echo "   ❌ Secret Key NO configurada"
fi
echo ""

# Resumen
echo "============================================"
if [ $site_key_found -eq 1 ] && [ $secret_key_found -eq 1 ]; then
    echo "✅ CONFIGURACIÓN COMPLETADA EXITOSAMENTE"
    echo "============================================"
    echo ""
    echo "📋 Próximos pasos:"
    echo ""
    echo "1. Verificar que la tabla SUSCRIPTORES existe:"
    echo "   mysql -u vetascom_web -p vetascom_web < sql/create_suscriptores_table.sql"
    echo ""
    echo "2. Verificar credenciales de BD en suscripcion.cgi"
    echo "   (Buscar la función conectar_db)"
    echo ""
    echo "3. Subir archivos al servidor (si estás en local):"
    echo "   - components/seccion-suscripcion*.html"
    echo "   - suscripcion.cgi"
    echo "   - index.cgi (ya modificado)"
    echo ""
    echo "4. Probar la integración:"
    echo "   🌐 https://www.vetas.com/index.cgi?i=es"
    echo "   🌐 https://www.vetas.com/index.cgi?i=en"
    echo "   🌐 https://www.vetas.com/index.cgi?i=br"
    echo ""
    echo "5. Hacer scroll hasta el final y probar el formulario"
    echo ""
    echo "📦 Backup guardado en: $backup_dir"
    echo ""
    echo "🎉 ¡La sección de suscripción está lista!"
else
    echo "⚠️  CONFIGURACIÓN INCOMPLETA"
    echo "============================================"
    echo ""
    echo "Hubo problemas configurando algunos archivos."
    echo "Por favor, verifica manualmente:"
    echo ""
    if [ $site_key_found -eq 0 ]; then
        echo "❌ Site Key en: components/seccion-suscripcion*.html"
        echo "   Buscar: TU_SITE_KEY_AQUI"
        echo "   Reemplazar por: $SITE_KEY"
        echo ""
    fi
    if [ $secret_key_found -eq 0 ]; then
        echo "❌ Secret Key en: suscripcion.cgi"
        echo "   Buscar: TU_SECRET_KEY_AQUI"
        echo "   Reemplazar por: $SECRET_KEY"
        echo ""
    fi
    echo "📦 Backup disponible en: $backup_dir"
fi
echo "============================================"
