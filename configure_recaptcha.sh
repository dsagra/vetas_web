#!/bin/bash

# Script para configurar Google reCAPTCHA en contacto.cgi

echo "============================================"
echo "  Configuración de Google reCAPTCHA"
echo "  para VETAS - Formulario de Contacto"
echo "============================================"
echo ""

# Verificar si se pasaron las claves como parámetros
if [ $# -eq 2 ]; then
    SITE_KEY="$1"
    SECRET_KEY="$2"
else
    echo "Introduce tus claves de Google reCAPTCHA:"
    echo ""
    echo "Si aún no tienes las claves, ve a:"
    echo "https://www.google.com/recaptcha/admin/create"
    echo ""
    read -p "Site Key (clave pública): " SITE_KEY
    read -p "Secret Key (clave secreta): " SECRET_KEY
fi

echo ""
echo "Configurando..."

# Backup del archivo original
cp contacto.cgi contacto.cgi.backup
echo "✓ Backup creado: contacto.cgi.backup"

# Habilitar el script de reCAPTCHA
sed -i.tmp 's/<!-- <script src="https:\/\/www.google.com\/recaptcha\/api.js" async defer><\/script> -->/<script src="https:\/\/www.google.com\/recaptcha\/api.js" async defer><\/script>/' contacto.cgi

# Descomentar el div del reCAPTCHA y configurar Site Key
sed -i.tmp "s/<!--$//" contacto.cgi
sed -i.tmp "s/-->$//" contacto.cgi
sed -i.tmp "s/data-sitekey=\"TU_SITE_KEY_AQUI\"/data-sitekey=\"$SITE_KEY\"/" contacto.cgi

# Configurar Secret Key y habilitar validación
sed -i.tmp "s/\$captcha_valido = 1;/\$captcha_valido = 0;/" contacto.cgi
sed -i.tmp "s/# if (\$recaptcha_response ne \"\") {/if (\$recaptcha_response ne \"\") {/" contacto.cgi
sed -i.tmp "s/# }/}/" contacto.cgi
sed -i.tmp "s/my \$secret_key = 'TU_SECRET_KEY_AQUI';/my \$secret_key = '$SECRET_KEY';/" contacto.cgi

# Descomentar las líneas comentadas
sed -i.tmp 's/^#     /    /' contacto.cgi

# Limpiar archivos temporales
rm -f contacto.cgi.tmp

echo "✓ Configuración completada"
echo ""
echo "Claves configuradas:"
echo "  Site Key: $SITE_KEY"
echo "  Secret Key: ${SECRET_KEY:0:10}..."
echo ""
echo "IMPORTANTE:"
echo "1. Verifica que tu dominio esté registrado en Google reCAPTCHA"
echo "2. Instala el módulo LWP::UserAgent si no lo tienes:"
echo "   cpan LWP::UserAgent"
echo "3. Si algo sale mal, restaura el backup:"
echo "   mv contacto.cgi.backup contacto.cgi"
echo ""
echo "¡Listo! El formulario ahora tiene reCAPTCHA activado."
echo "============================================"
