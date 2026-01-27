#!/usr/bin/perl
################################################################################
# EJEMPLO DE INTEGRACIÓN - Secciones VETAS
# Este archivo muestra cómo integrar las nuevas secciones en el sitio existente
################################################################################

use strict;
use warnings;
use cPanelUserConfig;
use CGI qw(:standard);
use DBI;
use Entrada;
&Entrada;

use ConectarDB;
my $dbh = ConectarDB->connectWeb();

# Detectar idioma
my $idioma = param('i') || 'es';
$idioma = 'es' unless ($idioma eq 'br' or $idioma eq 'en');

# Configurar textos según idioma
my %textos = (
  'es' => {
    'menu' => 'menu.html',
    'suscripcion' => 'components/seccion-suscripcion.html',
    'anunciar' => 'components/seccion-anunciar.html',
  },
  'en' => {
    'menu' => 'menu_en.html',
    'suscripcion' => 'components/seccion-suscripcion-en.html',
    'anunciar' => 'components/seccion-anunciar.html', # Mismo en inglés
  },
  'br' => {
    'menu' => 'menu_br.html',
    'suscripcion' => 'components/seccion-suscripcion-br.html',
    'anunciar' => 'components/seccion-anunciar.html', # Mismo en portugués
  },
);

# Inicio HTML
print header(-type => 'text/html', -charset => 'utf-8');
print <<'HTML_HEAD';
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="VETAS - Suscripción y Publicidad">
  
  <title>VETAS - Revista de la Industria Maderera</title>
  
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="/css/bootstrap.min.css">
  
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- Estilos base -->
  <link rel="stylesheet" href="/css/estilos.css">
  
  <!-- Estilos nuevas secciones -->
  <link rel="stylesheet" href="/css/suscripcion.css">
  <link rel="stylesheet" href="/css/anunciar.css">
  
  <!-- Preload para performance -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://cdnjs.cloudflare.com">
</head>
<body>
HTML_HEAD

# Incluir menú existente
my $menu_file = $textos{$idioma}{'menu'};
if (-e $menu_file) {
  open(my $fh, '<', $menu_file) or die "No se puede abrir $menu_file: $!";
  print while <$fh>;
  close($fh);
}

# CONTENIDO PRINCIPAL DE TU SITIO
# (tu código existente aquí)

print <<'HTML_CONTENT';
<!-- Tu contenido existente aquí -->
<div class="container">
  <h1>Contenido principal del sitio</h1>
  <p>...</p>
</div>
HTML_CONTENT

# ============================================
# INCLUIR SECCIÓN DE SUSCRIPCIÓN
# ============================================
my $suscripcion_file = $textos{$idioma}{'suscripcion'};
if (-e $suscripcion_file) {
  open(my $fh, '<:utf8', $suscripcion_file) or die "No se puede abrir $suscripcion_file: $!";
  print while <$fh>;
  close($fh);
}

# ============================================
# INCLUIR SECCIÓN DE PUBLICIDAD
# ============================================
my $anunciar_file = $textos{$idioma}{'anunciar'};
if (-e $anunciar_file) {
  open(my $fh, '<:utf8', $anunciar_file) or die "No se puede abrir $anunciar_file: $!";
  print while <$fh>;
  close($fh);
}

# Footer existente
if (-e 'footer.html') {
  open(my $fh, '<:utf8', 'footer.html') or die "No se puede abrir footer.html: $!";
  print while <$fh>;
  close($fh);
}

# Cerrar HTML
print <<'HTML_FOOTER';
  <!-- Bootstrap JS (si lo usas) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  
  <!-- JavaScript de las secciones -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Manejo del formulario de suscripción
      const formSuscripcion = document.getElementById('formSuscripcion');
      
      if (formSuscripcion) {
        formSuscripcion.addEventListener('submit', function(e) {
          const email = document.getElementById('email').value;
          
          // Validación básica
          if (!email || !email.includes('@')) {
            e.preventDefault();
            alert('Por favor, ingresá un email válido');
            return;
          }
          
          // Google Analytics tracking (si está configurado)
          if (typeof gtag === 'function') {
            gtag('event', 'submit', {
              'event_category': 'Suscripción',
              'event_label': 'Formulario enviado'
            });
          }
        });
      }
      
      // Tracking de botones de publicidad
      const btnMediaKit = document.querySelector('.btn-anunciar.primary');
      const btnContacto = document.querySelector('.btn-anunciar.secondary');
      
      if (btnMediaKit) {
        btnMediaKit.addEventListener('click', function() {
          if (typeof gtag === 'function') {
            gtag('event', 'download', {
              'event_category': 'Media Kit',
              'event_label': 'Descarga iniciada'
            });
          }
        });
      }
      
      if (btnContacto) {
        btnContacto.addEventListener('click', function() {
          if (typeof gtag === 'function') {
            gtag('event', 'click', {
              'event_category': 'Contacto Comercial',
              'event_label': 'Botón clickeado'
            });
          }
        });
      }
    });
  </script>
</body>
</html>
HTML_FOOTER

# Cerrar conexión DB
$dbh->disconnect();

################################################################################
# NOTAS DE IMPLEMENTACIÓN:
#
# 1. Este archivo es un EJEMPLO. No lo uses directamente en producción.
#
# 2. Para integrar en tu index.cgi existente:
#    - Copia las líneas de <link> del CSS al <head>
#    - Incluye los componentes HTML donde los necesites
#    - Copia el JavaScript al final del <body>
#
# 3. Estructura de archivos necesarios:
#    /css/suscripcion.css
#    /css/anunciar.css
#    /components/seccion-suscripcion.html (ES)
#    /components/seccion-suscripcion-en.html (EN)
#    /components/seccion-suscripcion-br.html (BR)
#    /components/seccion-anunciar.html
#
# 4. Para crear el handler del formulario, ver ejemplo abajo.
#
################################################################################

__END__

=head1 HANDLER DE SUSCRIPCIÓN (suscripcion_handler.cgi)

#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use DBI;
use ConectarDB;

my $dbh = ConectarDB->connectWeb();

# Obtener datos del formulario
my $email = param('email') || '';
my $nombre = param('nombre') || '';
my $lang = param('lang') || 'es';

# Validar email
if ($email !~ /^[\w\.\-\+]+@[\w\.\-]+\.\w+$/) {
  print redirect('/error.html?msg=email_invalido');
  exit;
}

# Sanitizar datos
$email = lc($email);
$email =~ s/^\s+|\s+$//g;
$nombre =~ s/^\s+|\s+$//g;
$nombre =~ s/[<>'"&]//g; # Prevenir XSS básico

# Verificar si el email ya existe
my $check_sth = $dbh->prepare("SELECT ID FROM SUSCRIPTORES WHERE EMAIL = ?");
$check_sth->execute($email);

if ($check_sth->fetchrow_array) {
  # Email ya existe
  print redirect('/ya-suscrito.html');
  exit;
}

# Insertar en base de datos
my $insert_sth = $dbh->prepare(
  "INSERT INTO SUSCRIPTORES (EMAIL, NOMBRE, IDIOMA, FECHA, IP, ACTIVO) 
   VALUES (?, ?, ?, NOW(), ?, 1)"
);

my $ip = $ENV{'REMOTE_ADDR'} || '';

eval {
  $insert_sth->execute($email, $nombre, $lang, $ip);
};

if ($@) {
  # Error al insertar
  print redirect('/error.html?msg=error_db');
  exit;
}

# Enviar email de confirmación (opcional)
# enviar_email_confirmacion($email, $nombre, $lang);

# Redirigir a página de éxito
print redirect('/gracias-suscripcion.html');

$dbh->disconnect();

=cut

=head1 CREAR TABLA EN LA BASE DE DATOS

CREATE TABLE IF NOT EXISTS SUSCRIPTORES (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  EMAIL VARCHAR(255) NOT NULL UNIQUE,
  NOMBRE VARCHAR(255),
  IDIOMA VARCHAR(5) DEFAULT 'es',
  FECHA DATETIME NOT NULL,
  IP VARCHAR(50),
  ACTIVO TINYINT(1) DEFAULT 1,
  TOKEN VARCHAR(64),
  INDEX idx_email (EMAIL),
  INDEX idx_activo (ACTIVO),
  INDEX idx_fecha (FECHA)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

=cut

=head1 PÁGINAS DE RESPUESTA NECESARIAS

Crear estos archivos HTML:

1. /gracias-suscripcion.html
   - Mensaje de agradecimiento
   - Confirmación de suscripción
   - Link a seguir navegando

2. /ya-suscrito.html
   - Mensaje que el email ya está registrado
   - Opción de actualizar datos
   - Link al sitio

3. /error.html
   - Mensaje de error genérico
   - Sugerencias para solucionar
   - Link al formulario

=cut
