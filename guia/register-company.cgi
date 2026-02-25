#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use utf8;
use CGI;

my $cgi = CGI->new;
my $lang = $cgi->param('lang') || 'es';

$database1="vetas_VETAS2";
$hostname1="webmail.vetas.com";
$port1="";
$driver1 = "mysql";
$dsn1 = "DBI:$driver1:database=$database1;host=$hostname1;port=$port1;mysql_enable_utf8=1";
$dbh1 = DBI->connect ($dsn1, vetas_admin, 45104510, {mysql_enable_utf8 => 1});
print "Content-Type: text/html; charset=UTF-8\n\n";

print <<EOFHTML;
<!DOCTYPE html>
<html lang="es" id="htmlLang">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Registro en Guía Maderera - Paso 1</title>
<link rel="stylesheet" href="css/bootstrap.min.css">
<style>
body {
    background: linear-gradient(135deg, #72bf44 0%, #5fa835 100%);
    min-height: 100vh;
    padding: 20px 0;
}
.wizard-container {
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    padding: 30px;
    margin: 20px auto;
    max-width: 900px;
}
.logo-container {
    text-align: center;
    margin-bottom: 30px;
}
.logo-container img {
    max-width: 100%;
    height: auto;
}
.language-selector {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 30px;
}
.lang-btn {
    padding: 10px 25px;
    border: 2px solid #e0e0e0;
    background: white;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
}
.lang-btn:hover {
    border-color: #72bf44;
    transform: translateY(-2px);
}
.lang-btn.active {
    background: #72bf44;
    color: white;
    border-color: #72bf44;
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
    background: #e0e0e0;
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
    background: #e0e0e0;
    color: #999;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 10px;
    font-weight: bold;
    transition: all 0.3s;
}
.step.active .step-circle {
    background: #72bf44;
    color: white;
    box-shadow: 0 4px 12px rgba(114, 191, 68, 0.4);
}
.step.completed .step-circle {
    background: #10b981;
    color: white;
}
.step-label {
    font-size: 14px;
    color: #666;
}
.step.active .step-label {
    color: #72bf44;
    font-weight: 600;
}
.form-section {
    background: #f8f9fa;
    padding: 25px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.form-section-title {
    color: #72bf44;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #72bf44;
}
.form-label {
    font-weight: 600;
    color: #333;
    margin-bottom: 8px;
}
.form-control, .form-select {
    border-radius: 8px;
    border: 1px solid #ddd;
    padding: 10px 15px;
    transition: all 0.3s;
}
.form-control:focus, .form-select:focus {
    border-color: #72bf44;
    box-shadow: 0 0 0 0.2rem rgba(114, 191, 68, 0.25);
}
.btn-primary {
    background: linear-gradient(135deg, #72bf44 0%, #5fa835 100%);
    border: none;
    padding: 12px 40px;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.3s;
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(114, 191, 68, 0.4);
}
.required-field::after {
    content: '*';
    color: #dc3545;
    margin-left: 4px;
}
</style>
</head>
<body>
<div class="container">
    <div class="wizard-container">
        <div class="logo-container">
            <img src="logoguia.jpg" alt="Guía Maderera" id="logoImage">
        </div>
        
        <div class="language-selector">
            <button type="button" class="lang-btn active" onclick="changeLanguage('es')" id="lang-es">
                🇦🇷 Español
            </button>
            <button type="button" class="lang-btn" onclick="changeLanguage('en')" id="lang-en">
                🇺🇸 English
            </button>
            <button type="button" class="lang-btn" onclick="changeLanguage('br')" id="lang-br">
                🇧🇷 Português
            </button>
        </div>
        
        <div class="progress-steps">
            <div class="step active">
                <div class="step-circle">1</div>
                <div class="step-label" data-i18n="step1">Datos Empresa</div>
            </div>
            <div class="step">
                <div class="step-circle">2</div>
                <div class="step-label" data-i18n="step2">Rubros</div>
            </div>
            <div class="step">
                <div class="step-circle">3</div>
                <div class="step-label" data-i18n="step3">Categorías</div>
            </div>
            <div class="step">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step4">Finalizar</div>
            </div>
        </div>

        <h2 class="text-center mb-4" style="color: #333;" data-i18n="mainTitle">Registro en Guía Maderera</h2>
        <p class="text-center text-muted mb-4" data-i18n="mainSubtitle">Complete los datos de su empresa para aparecer en la Guía</p>

        <form name="formu" method="post" action="select-categories.cgi" onsubmit="return valida_envia()">
            <input type="hidden" name="lang" id="langField" value="$lang">
            
            <div class="form-section">
                <div class="form-section-title"><span data-i18n="sectionGeneral">Información General</span></div>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="form-label required-field" data-i18n="labelCompany">Empresa</label>
                        <input type="text" name="empresa" class="form-control" maxlength="50" required>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label required-field" data-i18n="labelContact">Persona de Contacto</label>
                        <input type="text" name="contacto" class="form-control" maxlength="50" required>
                    </div>
                </div>
            </div>

            <div class="form-section">
                <div class="form-section-title"><span data-i18n="sectionLocation">Ubicación</span></div>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="form-label required-field" data-i18n="labelAddress">Dirección</label>
                        <input type="text" name="dire" class="form-control" maxlength="50" required>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label required-field" data-i18n="labelCity">Ciudad</label>
                        <input type="text" name="ciudad" class="form-control" maxlength="50" required>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4 mb-3">
                        <label class="form-label required-field" data-i18n="labelProvince">Provincia</label>
                        <input type="text" name="prov" class="form-control" maxlength="50" required>
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label required-field" data-i18n="labelPostal">Código Postal</label>
                        <input type="text" name="cpostal" class="form-control" maxlength="10" required>
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label required-field" data-i18n="labelCountry">País</label>
                        <input type="text" name="pais" class="form-control" maxlength="50" required>
                    </div>
                </div>
            </div>

            <div class="form-section">
                <div class="form-section-title"><span data-i18n="sectionContact">Contacto</span></div>
                <div class="row">
                    <div class="col-md-4 mb-3">
                        <label class="form-label required-field" data-i18n="labelPhone">Teléfono</label>
                        <input type="tel" name="tel" class="form-control" maxlength="50" required>
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label" data-i18n="labelFax">Fax</label>
                        <input type="tel" name="fax" class="form-control" maxlength="50">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label required-field" data-i18n="labelEmail">E-mail</label>
                        <input type="email" name="email" class="form-control" maxlength="50" required>
                    </div>
                </div>
            </div>

            <div class="form-section">
                <div class="form-section-title"><span data-i18n="sectionDigital">Presencia Digital</span></div>
                <div class="row">
                    <div class="col-md-4 mb-3">
                        <label class="form-label" data-i18n="labelWebsite">Sitio Web</label>
                        <input type="url" name="site" class="form-control" maxlength="50" placeholder="https://...">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label" data-i18n="labelFacebook">Facebook</label>
                        <input type="text" name="facebook" class="form-control" maxlength="50" placeholder="Usuario o URL">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label" data-i18n="labelInstagram">Instagram</label>
                        <input type="text" name="instagram" class="form-control" maxlength="50" placeholder="@usuario">
                    </div>
                </div>
            </div>

            <div class="form-section">
                <div class="form-section-title"><span data-i18n="sectionAdFormat">Formato del Aviso</span></div>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="form-label required-field" data-i18n="labelFormat">Seleccione el formato</label>
                        <select name="AVISO" class="form-select" required>
                            <option value="" data-i18n="formatSelect">-- Seleccione una opción --</option>
                            <option value="UNA" data-i18n="formatFullPage">Una Página</option>
                            <option value="MEDIA" data-i18n="formatHalfPage">Media Página</option>
                            <option value="CUARTO" data-i18n="formatQuarterPage">Cuarto de Página</option>
                            <option value="OCTAVO" data-i18n="formatEighthPage">Octavo de Página</option>
                            <option value="DIECISEIS" data-i18n="formatSixteenth">Dieciseisavo de Página</option>
                            <option value="MENCION" data-i18n="formatMention">Mención</option>
                            <option value="PROMOCION" data-i18n="formatPromotion">Promoción</option>
                        </select>
                    </div>
                </div>
            </div>

            <div class="text-center mt-4">
                <button type="submit" class="btn btn-primary btn-lg" data-i18n="btnContinue">
                    Continuar al Paso 2 →
                </button>
            </div>
        </form>
    </div>
</div>

<script src="js/translations.js"></script>
<script>
function valida_envia() {
   const lang = localStorage.getItem('selectedLanguage') || 'es';
    const t = translations[lang];
    
    const campos = [
        {name: 'empresa', label: t.labelCompany},
        {name: 'contacto', label: t.labelContact},
        {name: 'dire', label: t.labelAddress},
        {name: 'ciudad', label: t.labelCity},
        {name: 'prov', label: t.labelProvince},
        {name: 'cpostal', label: t.labelPostal},
        {name: 'pais', label: t.labelCountry},
        {name: 'tel', label: t.labelPhone},
        {name: 'email', label: t.labelEmail}
    ];
    
    for (let campo of campos) {
        const elemento = document.formu[campo.name];
        if (!elemento.value.trim()) {
            alert(t.validRequired.replace('{field}', campo.label));
            elemento.focus();
            return false;
        }
    }
    
    // Validar email
    const email = document.formu.email.value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert(t.validEmail);
        document.formu.email.focus();
        return false;
    }
    
    // Validar formato aviso
    if (!document.formu.AVISO.value) {
        alert(t.validFormat);
        document.formu.AVISO.focus();
        return false;
    }
    
    return true;
}

// Establecer idioma inicial desde URL o localStorage
const urlParams = new URLSearchParams(window.location.search);
const urlLang = urlParams.get('lang') || '$lang';
if (urlLang && ['es', 'en', 'br'].includes(urlLang)) {
    localStorage.setItem('selectedLanguage', urlLang);
    changeLanguage(urlLang);
} else {
    const savedLang = localStorage.getItem('selectedLanguage') || 'es';
    changeLanguage(savedLang);
}
</script>
</body>
</html>
EOFHTML



