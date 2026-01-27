#!/usr/bin/perl
use strict;
use warnings;
use cPanelUserConfig;
use CGI;
use DBI;
use LWP::UserAgent;
use JSON;
use Encode;

# Configuración de reCAPTCHA
my $RECAPTCHA_SECRET_KEY = 'TU_SECRET_KEY_AQUI';  # Cambiar por tu clave secreta real

# Crear objeto CGI
my $cgi = CGI->new;

# Obtener parámetros del formulario
my $email = $cgi->param('email') || '';
my $nombre = $cgi->param('nombre') || '';
my $idioma = $cgi->param('idioma') || 'es';
my $recaptcha_response = $cgi->param('g-recaptcha-response') || '';

# Headers HTTP
print $cgi->header(
    -type => 'text/html',
    -charset => 'UTF-8'
);

# Validar email
if (!$email || $email !~ /^[\w\.-]+@[\w\.-]+\.\w+$/) {
    mostrar_error("Por favor, ingresa un email válido.", $idioma);
    exit;
}

# Validar reCAPTCHA (temporal: solo validar si está configurado)
my $captcha_valido = 1; # Por defecto válido para testing

if ($RECAPTCHA_SECRET_KEY ne 'TU_SECRET_KEY_AQUI' && $recaptcha_response) {
    $captcha_valido = validar_recaptcha($recaptcha_response, $RECAPTCHA_SECRET_KEY);
    
    if (!$captcha_valido) {
        mostrar_error("Error de validación reCAPTCHA. Por favor, intenta nuevamente.", $idioma);
        exit;
    }
}

# Conectar a la base de datos
my $dbh = conectar_db();

if (!$dbh) {
    mostrar_error("Error de conexión a la base de datos.", $idioma);
    exit;
}

# Verificar si el email ya existe
my $existe = verificar_email_existente($dbh, $email);

if ($existe) {
    mostrar_mensaje("Este email ya está suscrito a VETAS.", $idioma, "info");
    $dbh->disconnect;
    exit;
}

# Insertar nuevo suscriptor
my $id_insertado = insertar_suscriptor($dbh, $email, $nombre, $idioma);

if ($id_insertado) {
    # Enviar email de bienvenida (opcional - implementar después)
    # enviar_email_bienvenida($email, $nombre, $idioma);
    
    mostrar_exito($nombre || $email, $idioma);
} else {
    mostrar_error("Hubo un error al procesar tu suscripción. Por favor, intenta nuevamente.", $idioma);
}

$dbh->disconnect;
exit;

# ============================================
# FUNCIONES
# ============================================

sub conectar_db {
    my $database = "vetas_VETAS2";
    my $host = "localhost";
    my $user = "vetas_user";
    my $password = "ghewrp54";
    
    my $dbh = DBI->connect(
        "DBI:mysql:database=$database;host=$host",
        $user,
        $password,
        {
            RaiseError => 0,
            PrintError => 0,
            mysql_enable_utf8 => 1
        }
    );
    
    return $dbh;
}

sub validar_recaptcha {
    my ($response, $secret) = @_;
    
    # Si no hay respuesta de reCAPTCHA, retornar false
    return 0 unless $response;
    
    # Crear user agent
    my $ua = LWP::UserAgent->new;
    $ua->timeout(10);
    
    # Hacer request a Google
    my $verify_url = 'https://www.google.com/recaptcha/api/siteverify';
    my $response_obj = $ua->post($verify_url, {
        secret => $secret,
        response => $response
    });
    
    # Si la request falla, retornar false
    return 0 unless $response_obj->is_success;
    
    # Parsear JSON
    my $json_response = decode_json($response_obj->decoded_content);
    
    # Retornar si es válido
    return $json_response->{success} ? 1 : 0;
}

sub verificar_email_existente {
    my ($dbh, $email) = @_;
    
    my $sth = $dbh->prepare("SELECT COUNT(*) as count FROM SUSCRIPTORES WHERE EMAIL = ? AND ACTIVO = 1");
    $sth->execute($email);
    
    my $result = $sth->fetchrow_hashref;
    
    return $result->{count} > 0;
}

sub insertar_suscriptor {
    my ($dbh, $email, $nombre, $idioma) = @_;
    
    my $sth = $dbh->prepare(
        "INSERT INTO SUSCRIPTORES (EMAIL, NOMBRE, IDIOMA, FECHA, ACTIVO, IP) 
         VALUES (?, ?, ?, NOW(), 1, ?)"
    );
    
    my $ip = $ENV{REMOTE_ADDR} || '';
    
    my $success = $sth->execute($email, $nombre, $idioma, $ip);
    
    if ($success) {
        return $dbh->last_insert_id(undef, undef, 'SUSCRIPTORES', 'ID');
    }
    
    return 0;
}

sub mostrar_exito {
    my ($nombre, $idioma) = @_;
    
    my %textos = (
        'es' => {
            titulo => '¡Suscripción Exitosa!',
            mensaje => "Gracias por suscribirte a VETAS, $nombre.",
            descripcion => 'Recibirás en tu email las últimas ediciones digitales, notas técnicas y novedades del sector de la madera y el mueble en Latinoamérica.',
            boton => 'Volver al inicio',
            link => 'index.cgi?i=es'
        },
        'en' => {
            titulo => 'Subscription Successful!',
            mensaje => "Thank you for subscribing to VETAS, $nombre.",
            descripcion => 'You will receive the latest digital editions, technical articles and news from the wood and furniture sector in Latin America.',
            boton => 'Back to home',
            link => 'index.cgi?i=en'
        },
        'br' => {
            titulo => 'Assinatura Bem-Sucedida!',
            mensaje => "Obrigado por assinar VETAS, $nombre.",
            descripcion => 'Você receberá as últimas edições digitais, artigos técnicos e notícias do setor de madeira e móveis na América Latina.',
            boton => 'Voltar ao início',
            link => 'index.cgi?i=br'
        }
    );
    
    my $t = $textos{$idioma} || $textos{'es'};
    
    print <<HTML;
<!DOCTYPE html>
<html lang="$idioma">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$t->{titulo} - VETAS</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .success-container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 3rem;
            max-width: 600px;
            text-align: center;
            animation: slideUp 0.5s ease-out;
        }
        \@keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .success-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #72bf44, #5fa835);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            animation: scaleIn 0.5s ease-out 0.2s backwards;
        }
        \@keyframes scaleIn {
            from {
                transform: scale(0);
            }
            to {
                transform: scale(1);
            }
        }
        .success-icon svg {
            width: 50px;
            height: 50px;
            stroke: white;
            stroke-width: 3;
            stroke-linecap: round;
            stroke-linejoin: round;
            fill: none;
        }
        h1 {
            color: #2c3e50;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        .success-message {
            color: #5a6c7d;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        .success-description {
            color: #7f8c8d;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        }
        .btn-home {
            background: linear-gradient(135deg, #72bf44, #5fa835);
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            display: inline-block;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(114, 191, 68, 0.3);
        }
        .btn-home:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(114, 191, 68, 0.4);
            color: white;
            text-decoration: none;
        }
        .logo {
            width: 150px;
            margin-bottom: 2rem;
        }
    </style>
</head>
<body>
    <div class="success-container">
        <img src="images/logo_vetas.png" alt="VETAS" class="logo" onerror="this.style.display='none'">
        
        <div class="success-icon">
            <svg viewBox="0 0 52 52">
                <polyline points="14 27 22 35 38 19"/>
            </svg>
        </div>
        
        <h1>$t->{titulo}</h1>
        <p class="success-message">$t->{mensaje}</p>
        <p class="success-description">$t->{descripcion}</p>
        
        <a href="$t->{link}" class="btn-home">$t->{boton}</a>
    </div>
</body>
</html>
HTML
}

sub mostrar_error {
    my ($mensaje, $idioma) = @_;
    
    my %textos = (
        'es' => {
            titulo => 'Error en la Suscripción',
            boton => 'Volver a intentar',
            link => 'index.cgi?i=es'
        },
        'en' => {
            titulo => 'Subscription Error',
            boton => 'Try again',
            link => 'index.cgi?i=en'
        },
        'br' => {
            titulo => 'Erro na Assinatura',
            boton => 'Tentar novamente',
            link => 'index.cgi?i=br'
        }
    );
    
    my $t = $textos{$idioma} || $textos{'es'};
    
    print <<HTML;
<!DOCTYPE html>
<html lang="$idioma">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$t->{titulo} - VETAS</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .error-container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 3rem;
            max-width: 600px;
            text-align: center;
        }
        .error-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #f5576c, #f093fb);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
        }
        .error-icon svg {
            width: 50px;
            height: 50px;
            stroke: white;
            stroke-width: 3;
            stroke-linecap: round;
            stroke-linejoin: round;
            fill: none;
        }
        h1 {
            color: #2c3e50;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        .error-message {
            color: #7f8c8d;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }
        .btn-retry {
            background: linear-gradient(135deg, #f5576c, #f093fb);
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            display: inline-block;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }
        .btn-retry:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(245, 87, 108, 0.4);
            color: white;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-icon">
            <svg viewBox="0 0 52 52">
                <line x1="18" y1="18" x2="34" y2="34"/>
                <line x1="34" y1="18" x2="18" y2="34"/>
            </svg>
        </div>
        
        <h1>$t->{titulo}</h1>
        <p class="error-message">$mensaje</p>
        
        <a href="$t->{link}" class="btn-retry">$t->{boton}</a>
    </div>
</body>
</html>
HTML
}

sub mostrar_mensaje {
    my ($mensaje, $idioma, $tipo) = @_;
    $tipo ||= 'info';
    
    my %textos = (
        'es' => {
            boton => 'Volver al inicio',
            link => 'index.cgi?i=es'
        },
        'en' => {
            boton => 'Back to home',
            link => 'index.cgi?i=en'
        },
        'br' => {
            boton => 'Voltar ao início',
            link => 'index.cgi?i=br'
        }
    );
    
    my $t = $textos{$idioma} || $textos{'es'};
    
    print <<HTML;
<!DOCTYPE html>
<html lang="$idioma">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VETAS</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .message-container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 3rem;
            max-width: 600px;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
            font-size: 1.5rem;
            margin-bottom: 2rem;
        }
        .btn-home {
            background: linear-gradient(135deg, #72bf44, #5fa835);
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            display: inline-block;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .btn-home:hover {
            transform: translateY(-2px);
            color: white;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="message-container">
        <h1>$mensaje</h1>
        <a href="$t->{link}" class="btn-home">$t->{boton}</a>
    </div>
</body>
</html>
HTML
}
