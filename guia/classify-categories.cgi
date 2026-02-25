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
$dbh1 = DBI->connect ($dsn1, vetas_admin, 45104510, {mysql_enable_utf8 => 1}) or die "Error connecting to database: $DBI::errstr";
print "Content-Type: text/html; charset=UTF-8\n\n";


# Capturar idioma del formulario
my $lang = $formulario{lang} || 'es';

# Primero, eliminar los rubros anteriores de este cliente
$dbh1->do("DELETE FROM GUIA_CLIENTES_CLIRUB WHERE CLIENTE='$formulario{cliente}'") or die "Error deleting: " . $dbh1->errstr;

# Luego, insertar los nuevos rubros seleccionados
@keys = keys %formulario;
foreach $key (sort(keys %formulario)) {
	if ($key ne 'cliente' && $key ne 'Submit' && $key ne 'lang')
		{ 
$dbh1->do("INSERT INTO GUIA_CLIENTES_CLIRUB(CLIENTE,RUBRO) VALUES ('$formulario{cliente}',$key)") or die "Error inserting key $key: " . $dbh1->errstr;
		}
		}



print <<EOFHTML;
<!DOCTYPE html>
<html lang="$lang">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-i18n="pageTitle3">Registro en Guía Maderera - Paso 3</title>
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
.category-card {
    background: #f8f9fa;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 15px;
    transition: all 0.3s;
}
.category-card:hover {
    border-color: #72bf44;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.rubro-name {
    font-weight: 600;
    color: #333;
    margin-bottom: 12px;
    font-size: 16px;
    display: flex;
    align-items: center;
}
.rubro-name::before {
    content: '📦';
    margin-right: 10px;
    font-size: 20px;
}
.form-select {
    border-radius: 8px;
    border: 2px solid #e0e0e0;
    padding: 10px 15px;
    font-weight: 500;
    transition: all 0.3s;
}
.form-select:focus {
    border-color: #72bf44;
    box-shadow: 0 0 0 0.2rem rgba(114, 191, 68, 0.25);
    outline: none;
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
.btn-secondary {
    background: #6c757d;
    border: none;
    padding: 12px 30px;
    border-radius: 8px;
    font-weight: 600;
    color: white;
}
.info-box {
    background: #f0fdf4;
    border-left: 4px solid #72bf44;
    border-radius: 8px;
    padding: 15px 20px;
    margin-bottom: 25px;
}
.info-box strong {
    color: #72bf44;
}
.category-icon {
    display: inline-block;
    width: 30px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    border-radius: 50%;
    background: #72bf44;
    color: white;
    margin-right: 10px;
    font-size: 14px;
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
            <div class="step completed">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step1Label">Datos Empresa</div>
            </div>
            <div class="step completed">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step2Label">Rubros</div>
            </div>
            <div class="step active">
                <div class="step-circle">3</div>
                <div class="step-label" data-i18n="step3Label">Categorías</div>
            </div>
            <div class="step">
                <div class="step-circle">✓</div>
                <div class="step-label" data-i18n="step4Label">Finalizar</div>
            </div>
        </div>

        <h2 class="text-center mb-2" style="color: #333;" data-i18n="categorizeTitle">Categorización de Rubros</h2>
        <p class="text-center text-muted mb-4" data-i18n="categorizeSubtitle">Indique la categoría para cada uno de los rubros seleccionados</p>

        <div class="info-box">
            <strong>💡 <span data-i18n="important">Importante</span>:</strong> <span data-i18n="categorizeInfo">Seleccione la categoría que mejor describa su relación comercial con cada rubro</span>.
        </div>

        <form name="form1" method="post" action="registration-complete.cgi" onsubmit="return validarCategorias()">
            <input type="hidden" name="lang" value="$lang">
EOFHTML

# Seleccionar el campo RUBRO correcto según idioma
my $rubro_field = $lang eq 'en' ? 'R.RUBRO_EN' : ($lang eq 'br' ? 'R.RUBRO_BR' : 'R.RUBRO_ES');
$stm0 = $dbh1->prepare("select *,C.ID as rubro from GUIA_CLIENTES_CLIRUB as C, RUBROS as R where C.CLIENTE=$formulario{cliente} and C.RUBRO=R.ID order by $rubro_field");
$stm0->execute();

my $count = 0;
while ($r=$stm0->fetchrow_hashref)
{
    $count++;
    # Mostrar el nombre del rubro en el idioma seleccionado
    my $rubro_name = $lang eq 'en' ? $r->{RUBRO_EN} : ($lang eq 'br' ? $r->{RUBRO_BR} : $r->{RUBRO_ES});
    
    print <<CARDHTML;
            <div class="category-card">
                <div class="rubro-name">$rubro_name</div>
                <select name="$r->{rubro}" class="form-select categoria-select" required>
                    <option value="" data-i18n="selectCategory">-- Seleccione una categoría --</option>
                    <option value="D" data-i18n="distributor">🏪 Distribuidor</option>
                    <option value="I" data-i18n="importer">📦 Importador</option>
                    <option value="E" data-i18n="exporter">🌍 Exportador</option>
                    <option value="F" data-i18n="manufacturer">🏭 Fabricante</option>
                    <option value="P" data-i18n="producer">🌾 Productor</option>
                    <option value="R" data-i18n="representative">🤝 Representante</option>
                </select>
            </div>
CARDHTML
}

print <<EOFHTML;
            <div class="text-center mt-4" style="display: flex; gap: 15px; justify-content: center;">
                <button type="button" class="btn btn-secondary" onclick="history.back()">
                    ← <span data-i18n="back">Volver</span>
                </button>
                <button type="submit" class="btn btn-primary btn-lg">
                    <span data-i18n="finishRegistration">Finalizar Registro</span> →
                </button>
            </div>
        </form>
    </div>
</div>

<script src="js/translations.js"></script>
<script>
// Cargar idioma guardado
document.addEventListener('DOMContentLoaded', () => {
    const lang = localStorage.getItem('selectedLanguage') || '$lang';
    localStorage.setItem('selectedLanguage', lang);
    updateTexts(lang);
});

function validarCategorias() {
    const lang = localStorage.getItem('selectedLanguage') || 'es';
    const t = translations[lang];
    const selects = document.querySelectorAll('.categoria-select');
    let todasCompletas = true;
    let primeraIncompleta = null;
    
    selects.forEach(select => {
        if (!select.value) {
            todasCompletas = false;
            if (!primeraIncompleta) {
                primeraIncompleta = select;
            }
            select.style.borderColor = '#dc3545';
        } else {
            select.style.borderColor = '#e0e0e0';
        }
    });
    
    if (!todasCompletas) {
        alert(t.validCategory);
        if (primeraIncompleta) {
            primeraIncompleta.focus();
            primeraIncompleta.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        return false;
    }
    
    return true;
}

// Resetear borde al seleccionar
document.querySelectorAll('.categoria-select').forEach(select => {
    select.addEventListener('change', function() {
        if (this.value) {
            this.style.borderColor = '#10b981';
        }
    });
});
</script>
</body>
</html>
EOFHTML


