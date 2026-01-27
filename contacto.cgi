#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use Entrada;
&Entrada;

use ConectarDB;
$dbh=ConectarDB->connectWeb();
$dbh->do("SET NAMES 'utf8'");
$dbh->do("SET CHARACTER SET utf8");

# Obtener configuración
$stm2 = $dbh->prepare("select * from CONFIG where ID=1");
$stm2->execute();
$revi=$stm2->fetchrow_hashref;

$stm2 = $dbh->prepare("select * from REVISTAS_CONFIG where REVISTA=$revi->{REVISTA}");
$stm2->execute();
$revista=$stm2->fetchrow_hashref;

$envi="$ENV{REQUEST_URI}";
if ($envi =~ m/i=/) {
   
}
else
  {
    if ($envi =~ m/\?/) {
      $envi=$envi."&i=es";
    }
    else
      {
        $envi=$envi."?i=es";
      }
  }

$idioma="es";
$idioma=$formulario{i} if ($formulario{i} eq "br" or $formulario{i} eq "en" );
$MENU="menu.html";
$MENU="menu_en.html" if ($idioma eq "en") ;
$MENU="menu_br.html" if ($idioma eq "br") ;

# Textos según idioma
if ($idioma eq "es")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  $titulo="Contacto";
  $subtitulo="Env&iacute;anos tu consulta";
  $nombre_label="Nombre completo";
  $nombre_placeholder="Ingresa tu nombre";
  $email_label="Correo electr&oacute;nico";
  $email_placeholder="tu@email.com";
  $telefono_label="Tel&eacute;fono";
  $telefono_placeholder="+54 11 1234-5678";
  $empresa_label="Empresa";
  $empresa_placeholder="Nombre de tu empresa (opcional)";
  $pais_label="Pa&iacute;s";
  $pais_placeholder="Argentina";
  $mensaje_label="Mensaje";
  $mensaje_placeholder="Escribe tu consulta aqu&iacute;...";
  $enviar_label="Enviar Consulta";
  $exito_titulo="&iexcl;Mensaje Enviado!";
  $exito_mensaje="Gracias por contactarnos. Responderemos tu consulta a la brevedad.";
  $error_titulo="Error";
  $error_mensaje="Por favor completa todos los campos obligatorios.";
  $volver_label="Volver al inicio";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  $titulo="Contact";
  $subtitulo="Send us your inquiry";
  $nombre_label="Full name";
  $nombre_placeholder="Enter your name";
  $email_label="Email address";
  $email_placeholder="your@email.com";
  $telefono_label="Phone";
  $telefono_placeholder="+1 305 123-4567";
  $empresa_label="Company";
  $empresa_placeholder="Your company name (optional)";
  $pais_label="Country";
  $pais_placeholder="United States";
  $mensaje_label="Message";
  $mensaje_placeholder="Write your inquiry here...";
  $enviar_label="Send Inquiry";
  $exito_titulo="Message Sent!";
  $exito_mensaje="Thank you for contacting us. We will respond to your inquiry shortly.";
  $error_titulo="Error";
  $error_mensaje="Please complete all required fields.";
  $volver_label="Back to home";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  $titulo="Contato";
  $subtitulo="Envie-nos sua consulta";
  $nombre_label="Nome completo";
  $nombre_placeholder="Digite seu nome";
  $email_label="E-mail";
  $email_placeholder="seu@email.com";
  $telefono_label="Telefone";
  $telefono_placeholder="+55 11 1234-5678";
  $empresa_label="Empresa";
  $empresa_placeholder="Nome da sua empresa (opcional)";
  $pais_label="Pa&iacute;s";
  $pais_placeholder="Brasil";
  $mensaje_label="Mensagem";
  $mensaje_placeholder="Escreva sua consulta aqui...";
  $enviar_label="Enviar Consulta";
  $exito_titulo="Mensagem Enviada!";
  $exito_mensaje="Obrigado por entrar em contato. Responderemos sua consulta em breve.";
  $error_titulo="Erro";
  $error_mensaje="Por favor, preencha todos os campos obrigat&oacute;rios.";
  $volver_label="Voltar ao in&iacute;cio";
  }

$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);

# Procesar formulario si se envió
$mensaje_resultado = "";
if ($formulario{submit}) {
    $nombre = $formulario{nombre};
    $email = $formulario{email};
    $telefono = $formulario{telefono};
    $empresa = $formulario{empresa};
    $pais = $formulario{pais};
    $mensaje = $formulario{mensaje};
    $recaptcha_response = $formulario{'g-recaptcha-response'};
    
    # Verificar reCAPTCHA
    # NOTA: Deshabilitado temporalmente - Configurar claves en producción
    $captcha_valido = 1; # Cambiar a 0 cuando el CAPTCHA esté configurado
    
    # DESCOMENTAR ESTE BLOQUE CUANDO TENGAS LAS CLAVES DE RECAPTCHA:
    # if ($recaptcha_response ne "") {
    #     use LWP::UserAgent;
    #     my $ua = LWP::UserAgent->new();
    #     my $secret_key = 'TU_SECRET_KEY_AQUI'; # CAMBIAR POR TU SECRET KEY
    #     my $verify_url = 'https://www.google.com/recaptcha/api/siteverify';
    #     
    #     my $response = $ua->post($verify_url, {
    #         secret => $secret_key,
    #         response => $recaptcha_response
    #     });
    #     
    #     if ($response->is_success) {
    #         my $json_response = $response->decoded_content;
    #         if ($json_response =~ /"success":\s*true/) {
    #             $captcha_valido = 1;
    #         }
    #     }
    # }
    
    # Validar campos obligatorios y CAPTCHA
    if ($nombre ne "" && $email ne "" && $mensaje ne "" && $captcha_valido) {
        # Escapar comillas para SQL
        $nombre =~ s/'/''/g;
        $email =~ s/'/''/g;
        $telefono =~ s/'/''/g;
        $empresa =~ s/'/''/g;
        $pais =~ s/'/''/g;
        $mensaje =~ s/'/''/g;
        
        # Insertar en la base de datos
        $sql = "INSERT INTO CONSULTA_WEB (NOMBRE, EMAIL, TELEFONO, EMPRESA, PAIS, MENSAJE, FECHA, IDIOMA) 
                VALUES ('$nombre', '$email', '$telefono', '$empresa', '$pais', '$mensaje', NOW(), '$idioma')";
        
        $stm = $dbh->prepare($sql);
        if ($stm->execute()) {
            $mensaje_resultado = qq(
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    <h5 class="alert-heading"><i class="fas fa-check-circle"></i> $exito_titulo</h5>
                    <p>$exito_mensaje</p>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            );
            # Limpiar campos
            $nombre = "";
            $email = "";
            $telefono = "";
            $empresa = "";
            $pais = "";
            $mensaje = "";
        }
    } else {
        my $error_msg = $error_mensaje;
        if (!$captcha_valido && $recaptcha_token eq "") {
            $error_msg = ($idioma eq "es") ? "Error de validaci&oacute;n de seguridad. Por favor intenta nuevamente." : 
                         ($idioma eq "en") ? "Security validation error. Please try again." : 
                         "Erro de valida&ccedil;&atilde;o de seguran&ccedil;a. Por favor, tente novamente.";
        } elsif (!$captcha_valido) {
            $error_msg = ($idioma eq "es") ? "Detecci&oacute;n de actividad sospechosa. Por favor intenta nuevamente (Score: $captcha_score)." : 
                         ($idioma eq "en") ? "Suspicious activity detected. Please try again (Score: $captcha_score)." : 
                         "Atividade suspeita detectada. Por favor, tente novamente (Score: $captcha_score).";
        }
        
        $mensaje_resultado = qq(
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <h5 class="alert-heading"><i class="fas fa-exclamation-triangle"></i> $error_titulo</h5>
                <p>$error_msg</p>
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        );
    }
}

print <<EOFHTML;
<!-- Google reCAPTCHA v3 -->
<script src="https://www.google.com/recaptcha/api.js?render=6LcI1FIsAAAAAL4Q92H_tU_NbIuX98WzbEIM-0gJ"></script>

<div class="container mt-4 mb-5">
    <div class="row mb-4">
        <div class="col-md-12 text-center">
            <h1 class="display-4">$titulo</h1>
            <p class="lead text-muted">$subtitulo</p>
        </div>
    </div>

    $mensaje_resultado

    <div class="row justify-content-center">
        <div class="col-lg-8 col-md-10">
            <div class="card shadow-lg border-0">
                <div class="card-body p-4">
                    <form method="post" action="contacto.cgi?i=$idioma" id="contactForm" onsubmit="return submitFormWithRecaptcha(event);">
                        <input type="hidden" name="i" value="$idioma">
                        <input type="hidden" id="g-recaptcha-response" name="g-recaptcha-response">
                        
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="nombre" class="font-weight-bold">
                                        <i class="fas fa-user text-success"></i> $nombre_label *
                                    </label>
                                    <input type="text" class="form-control form-control-lg" id="nombre" name="nombre" 
                                           placeholder="$nombre_placeholder" value="$nombre" required>
                                </div>
                            </div>
                            
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="email" class="font-weight-bold">
                                        <i class="fas fa-envelope text-success"></i> $email_label *
                                    </label>
                                    <input type="email" class="form-control form-control-lg" id="email" name="email" 
                                           placeholder="$email_placeholder" value="$email" required>
                                </div>
                            </div>
                        </div>
                        
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="telefono" class="font-weight-bold">
                                        <i class="fas fa-phone text-success"></i> $telefono_label
                                    </label>
                                    <input type="tel" class="form-control form-control-lg" id="telefono" name="telefono" 
                                           placeholder="$telefono_placeholder" value="$telefono">
                                </div>
                            </div>
                            
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="empresa" class="font-weight-bold">
                                        <i class="fas fa-building text-success"></i> $empresa_label
                                    </label>
                                    <input type="text" class="form-control form-control-lg" id="empresa" name="empresa" 
                                           placeholder="$empresa_placeholder" value="$empresa">
                                </div>
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label for="pais" class="font-weight-bold">
                                <i class="fas fa-globe text-success"></i> $pais_label
                            </label>
                            <input type="text" class="form-control form-control-lg" id="pais" name="pais" 
                                   placeholder="$pais_placeholder" value="$pais">
                        </div>
                        
                        <div class="form-group">
                            <label for="mensaje" class="font-weight-bold">
                                <i class="fas fa-comment-alt text-success"></i> $mensaje_label *
                            </label>
                            <textarea class="form-control form-control-lg" id="mensaje" name="mensaje" rows="6" 
                                      placeholder="$mensaje_placeholder" required>$mensaje</textarea>
                        </div>
                        
                        <div class="form-group text-center mt-4">
                            <button type="submit" name="submit" value="1" id="submitBtn" class="btn btn-lg btn-block" 
                                    style="background-color: #72bf44; color: white; border: none; padding: 15px;">
                                <i class="fas fa-paper-plane"></i> $enviar_label
                            </button>
                        </div>
                        
                        <div class="text-center mt-3">
                            <small class="text-muted">
EOFHTML

if ($idioma eq "es") {
    print "* Campos obligatorios | Protegido por reCAPTCHA";
} elsif ($idioma eq "en") {
    print "* Required fields | Protected by reCAPTCHA";
} else {
    print "* Campos obrigat&oacute;rios | Protegido por reCAPTCHA";
}

print <<EOFHTML;
                            </small>
                            <div class="mt-2">
                                <small class="text-muted">
                                    <a href="https://policies.google.com/privacy" target="_blank" style="color: #72bf44;">Privacy</a> - 
                                    <a href="https://policies.google.com/terms" target="_blank" style="color: #72bf44;">Terms</a>
                                </small>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        
        <!-- Información de contacto adicional -->
        <div class="col-lg-4 col-md-10 mt-4 mt-lg-0">
            <div class="card shadow-sm border-0 h-100">
                <div class="card-body">
                    <h5 class="card-title text-center mb-4" style="color: #72bf44;">
                        <i class="fas fa-info-circle"></i> 
EOFHTML

if ($idioma eq "es") {
    print "Contacto Directo";
} elsif ($idioma eq "en") {
    print "Direct Contact";
} else {
    print "Contato Direto";
}

print <<EOFHTML;
                    </h5>
                    
                    <div class="contact-info">
                        <div class="mb-3">
                            <h6 class="font-weight-bold">U.S.A.</h6>
                            <p class="mb-1"><i class="fas fa-map-marker-alt text-success"></i> Miami, FL</p>
                            <p class="mb-1"><i class="fas fa-phone text-success"></i> +1-305-968-3936</p>
                            <p class="mb-1"><i class="fas fa-envelope text-success"></i> usa@vetas.com</p>
                        </div>
                        
                        <hr>
                        
                        <div class="mb-3">
                            <h6 class="font-weight-bold">LATINOAM&Eacute;RICA</h6>
                            <p class="mb-1"><i class="fas fa-map-marker-alt text-success"></i> Buenos Aires, Argentina</p>
                            <p class="mb-1"><i class="fas fa-phone text-success"></i> +54-11-4803-9650</p>
                            <p class="mb-1"><i class="fas fa-envelope text-success"></i> info@vetas.com</p>
                        </div>
                        
                        <hr>
                        
                        <div class="mb-3">
                            <h6 class="font-weight-bold">BRASIL</h6>
                            <p class="mb-1"><i class="fas fa-map-marker-alt text-success"></i> Caxias do Sul, RS</p>
                            <p class="mb-1"><i class="fas fa-mobile-alt text-success"></i> +55-54-9973-3842</p>
                            <p class="mb-1"><i class="fas fa-envelope text-success"></i> brasil@vetas.com</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.card {
    border-radius: 15px;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}

.form-control:focus {
    border-color: #72bf44;
    box-shadow: 0 0 0 0.2rem rgba(114, 191, 68, 0.25);
}

.btn:hover {
    background-color: #5da835 !important;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(114, 191, 68, 0.3);
}

.contact-info {
    font-size: 0.9rem;
}

.contact-info h6 {
    color: #72bf44;
    margin-bottom: 10px;
}

.contact-info p {
    color: #666;
}

.contact-info i {
    width: 20px;
}

/* Botón reCAPTCHA badge */
.grecaptcha-badge {
    visibility: visible;
    opacity: 1;
    z-index: 999;
}
</style>

<script>
// reCAPTCHA v3 - Ejecutar antes de enviar el formulario
function submitFormWithRecaptcha(event) {
    event.preventDefault();
    
    var submitBtn = document.getElementById('submitBtn');
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 
EOFHTML

if ($idioma eq "es") {
    print "Enviando...";
} elsif ($idioma eq "en") {
    print "Sending...";
} else {
    print "Enviando...";
}

print <<EOFHTML;
';
    
    grecaptcha.ready(function() {
        grecaptcha.execute('6LcI1FIsAAAAAL4Q92H_tU_NbIuX98WzbEIM-0gJ', {action: 'submit'}).then(function(token) {
            // Agregar el token al campo oculto
            document.getElementById('g-recaptcha-response').value = token;
            // Enviar el formulario
            document.getElementById('contactForm').submit();
        });
    });
    
    return false;
}
</script>

EOFHTML

open FOOTER, $FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}
close FOOTER;

$dbh->disconnect;
