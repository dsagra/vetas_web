#!/usr/bin/perl
use cPanelUserConfig;
use Entrada;
&Entrada;
use utf8;

use DBI;
$database1="vetas_VETAS2";
$hostname1="webmail.vetas.com";
$port1="";
$driver1 = "mysql";
$dsn1 = "DBI:$driver1:database=$database1;host=$hostname1;port=$port1;mysql_enable_utf8=1";
$dbh1 = DBI->connect ($dsn1, vetas_admin, 45104510, {mysql_enable_utf8 => 1});
print "Content-Type: text/html; charset=UTF-8\n\n";

# Capturar idioma del formulario
my $lang = $formulario{lang} || 'es';

@keys = keys %formulario;
foreach $key (sort(keys %formulario)) {
	if ($key ne 'cliente' && $key ne 'Submit' && $key ne 'lang')
		{ 
	$sql = "update GUIA_CLIENTES_CLIRUB set CLASE='$formulario{$key}' where ID = $key";
	$dbh1->do($sql);
		}
		}



print <<EOFHTML;
<!DOCTYPE html>
<html lang="$lang">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-i18n="pageTitle4">Registro Completado - Guía Maderera</title>
<link rel="stylesheet" href="css/bootstrap.min.css">
<style>
body {
    background: linear-gradient(135deg, #72bf44 0%, #5fa835 100%);
    min-height: 100vh;
    padding: 20px 0;
    display: flex;
    align-items: center;
    justify-content: center;
}
.container {
    width: 100%;
}
.wizard-container {
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    padding: 40px;
    margin: 20px auto;
    max-width: 700px;
}
.logo-container {
    text-align: center;
    margin-bottom: 30px;
}
.logo-container img {
    max-width: 100%;
    height: auto;
}
.progress-steps {
    display: flex;
    justify-content: space-between;
    margin-bottom: 40px;
    position: relative;
}
.progress-steps::before {
    content: '';
    position: absolute;
    top: 20px;
    left: 0;
    right: 0;
    height: 2px;
    background: #10b981;
    z-index: 0;
}
.step {
    flex: 1;
    text-align: center;
    position: relative;
    z-index: 1;
}
.step-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #10b981;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 10px;
    font-weight: bold;
    animation: pulse 2s infinite;
}
.step-label {
    font-size: 14px;
    color: #10b981;
    font-weight: 600;
}
@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
    }
    50% {
        box-shadow: 0 0 0 10px rgba(16, 185, 129, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
    }
}
.success-icon {
    width: 120px;
    height: 120px;
    margin: 0 auto 30px;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 60px;
    color: white;
    animation: scaleIn 0.5s ease-out;
}
@keyframes scaleIn {
    0% {
        transform: scale(0);
        opacity: 0;
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}
.success-title {
    color: #10b981;
    font-size: 32px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 15px;
}
.success-message {
    color: #555;
    font-size: 18px;
    text-align: center;
    line-height: 1.6;
    margin-bottom: 30px;
}
.info-card {
    background: #f0fdf4;
    border: 2px solid #10b981;
    border-radius: 10px;
    padding: 25px;
    margin: 25px 0;
}
.info-card h4 {
    color: #10b981;
    font-weight: 600;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
}
.info-card h4::before {
    content: '📝';
    margin-right: 10px;
    font-size: 24px;
}
.info-card ul {
    list-style: none;
    padding-left: 0;
    margin: 0;
}
.info-card li {
    padding: 8px 0;
    color: #333;
    display: flex;
    align-items: start;
}
.info-card li::before {
    content: '✓';
    color: #10b981;
    font-weight: bold;
    margin-right: 10px;
    font-size: 18px;
}
.btn-home {
    background: linear-gradient(135deg, #72bf44 0%, #5fa835 100%);
    border: none;
    padding: 14px 40px;
    border-radius: 8px;
    font-weight: 600;
    color: white;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s;
    margin-top: 20px;
}
.btn-home:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(114, 191, 68, 0.4);
    color: white;
}
.contact-box {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 20px;
    margin-top: 25px;
    text-align: center;
}
.contact-box p {
    margin: 5px 0;
    color: #666;
}
.contact-box strong {
    color: #667eea;
}
</style>
</head>
<body>
<div class="container">
    <div class="wizard-container">
        <div class="logo-container">
            <img src="logoguia.jpg" alt="Guía Maderera">
        </div>
        
        <div class="progress-steps">
            <div class="step">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step1Label">Datos Empresa</div>
            </div>
            <div class="step">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step2Label">Rubros</div>
            </div>
            <div class="step">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step3Label">Categorías</div>
            </div>
            <div class="step">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step4Label">Finalizar</div>
            </div>
        </div>

        <div class="success-icon">✓</div>
        
        <h1 class="success-title" data-i18n="registrationComplete">¡Registro Completado!</h1>
        
        <p class="success-message" data-i18n="successMessage">
            Todos sus datos han sido registrados exitosamente en nuestro sistema.
            Su empresa pronto formará parte de la Guía Maderera.
        </p>

        <div class="info-card">
            <h4 data-i18n="nextSteps">Próximos Pasos</h4>
            <ul>
                <li data-i18n="step1Text">Nuestro equipo revisará la información proporcionada</li>
                <li data-i18n="step2Text">Nos comunicaremos con usted en las próximas 48-72 horas</li>
                <li data-i18n="step3Text">Recibirá instrucciones sobre el proceso de publicación</li>
                <li data-i18n="step4Text">Le informaremos sobre las opciones de publicidad disponibles</li>
            </ul>
        </div>

        <div class="contact-box">
            <p><strong data-i18n="questionsTitle">¿Tiene alguna pregunta?</strong></p>
            <p data-i18n="questionsText">No dude en contactarnos para cualquier consulta sobre su registro.</p>
        </div>

        <div class="text-center">
            <a href="https://www.vetas.com" class="btn-home">
                ← <span data-i18n="backToHome">Volver al Inicio</span>
            </a>
        </div>
    </div>
</div>

<script src="js/translations.js"></script>
<script>
// Cargar idioma guardado
document.addEventListener('DOMContentLoaded', () => {
    const lang = localStorage.getItem('selectedLanguage') || '$lang';
    updateTexts(lang);
});

// Confetti effect (opcional)
setTimeout(() => {
    console.log('¡Registro completado exitosamente!');
}, 500);
</script>
</body>
</html>
EOFHTML


