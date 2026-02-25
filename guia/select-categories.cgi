#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use utf8;
use Encode;

use Entrada;
&Entrada;

$database1="vetas_VETAS2";
$hostname1="webmail.vetas.com";
$port1="";
$driver1 = "mysql";
$dsn1 = "DBI:$driver1:database=$database1;host=$hostname1;port=$port1;mysql_enable_utf8=1";
$dbh1 = DBI->connect ($dsn1, vetas_admin, 45104510, {mysql_enable_utf8 => 1});
print "Content-Type: text/html; charset=UTF-8\n\n";

# Capturar el idioma seleccionado
$lang = $formulario{lang} || 'es';
# Determinar el campo de rubro según el idioma
my $rubro_field = "RUBRO_ES";
if ($lang eq 'en') {
    $rubro_field = "RUBRO_EN";
} elsif ($lang eq 'br') {
    $rubro_field = "RUBRO_BR";
}

$sql=qq(insert into GUIA_CLIENTES_ALTA(EMPRESA,DIRE,CIUDAD,TEL,FAX,CONTACTO,PROV,CPOSTAL,PAIS,EMAIL,WEB,AVISO,FECHA,FACEBOOK,INSTAGRAM) values ("$formulario{empresa}","$formulario{dire}","$formulario{ciudad}","$formulario{tel}","$formulario{fax}","$formulario{contacto}","$formulario{prov}","$formulario{cpostal}","$formulario{pais}","$formulario{email}","$formulario{site}","$formulario{AVISO}",now(),"$formulario{facebook}","$formulario{instagram}")); 
$dbh1->do($sql);
$stm6 = $dbh1->prepare("select last_insert_id() as id from GUIA_CLIENTES_ALTA");
$stm6->execute();
$id=$stm6->fetchrow_hashref;

$stm0 = $dbh1->prepare("select *, $rubro_field as RUBRO_NOMBRE from RUBROS where SALE_EN_GUIA=1 order by CODIGO,$rubro_field");
$stm0->execute();
print <<EOFHTML;
<!DOCTYPE html>
<html lang="es" id="htmlLang">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Registro en Guía Maderera - Paso 2</title>
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
    max-width: 1000px;
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
.rubros-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 15px;
    margin-top: 20px;
}
.rubro-card {
    background: #f8f9fa;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    padding: 15px;
    transition: all 0.3s;
    cursor: pointer;
}
.rubro-card:hover {
    border-color: #72bf44;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.rubro-card.selected {
    border-color: #72bf44;
    background: #f0fdf4;
}
.rubro-category {
    background: linear-gradient(135deg, #72bf44 0%, #5fa835 100%);
    color: white;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
    font-weight: 600;
    font-size: 18px;
}
.rubro-subcategory {
    background: #f0fdf4;
    color: #5fa835;
    padding: 12px;
    border-radius: 8px;
    margin: 15px 0 10px;
    font-weight: 600;
    border-left: 4px solid #72bf44;
}
.custom-checkbox {
    width: 20px;
    height: 20px;
    cursor: pointer;
    margin-right: 10px;
}
.rubro-label {
    display: flex;
    align-items: flex-start;
    cursor: pointer;
    user-select: none;
}
.rubro-text {
    flex: 1;
}
.badge-online {
    background: #72bf44;
    color: white;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 11px;
    margin-top: 5px;
    display: inline-block;
}
.badge-printed {
    background: #10b981;
    color: white;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 11px;
    margin-top: 5px;
    display: inline-block;
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
.selection-counter {
    background: #fff3cd;
    border: 1px solid #ffc107;
    border-radius: 8px;
    padding: 12px 20px;
    margin-bottom: 20px;
    text-align: center;
    font-weight: 600;
    color: #856404;
}
.search-box {
    margin-bottom: 20px;
}
.search-box input {
    border-radius: 8px;
    border: 2px solid #e0e0e0;
    padding: 12px 20px;
    width: 100%;
    transition: all 0.3s;
}
.search-box input:focus {
    border-color: #72bf44;
    outline: none;
    box-shadow: 0 0 0 0.2rem rgba(114, 191, 68, 0.25);
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
                <div class="step-label" data-i18n="step1">Datos Empresa</div>
            </div>
            <div class="step active">
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

        <h2 class="text-center mb-2" style="color: #333;" data-i18n="step2Title">Selección de Rubros</h2>
        <p class="text-center text-muted mb-4" data-i18n="step2Subtitle">Seleccione todos los rubros que comercializa su empresa</p>

        <div class="selection-counter" id="counter" data-i18n="noSelection">
            No ha seleccionado ningún rubro aún
        </div>

        <div class="search-box">
            <input type="text" id="searchInput" placeholder="🔍 Buscar rubros..." data-i18n="searchPlaceholder">
        </div>

        <form name="form1" method="post" action="classify-categories.cgi" onsubmit="return validarSeleccion()">
            <input name="cliente" type="hidden" value="$id->{id}">
            <input name="lang" type="hidden" value="$lang">
            <div id="rubrosContainer">
EOFHTML

my $categoria_actual = "";
my $subcategoria_actual = "";
my $grid_abierto = 0;

# Definir los badges según el idioma
my %marca_labels = (
    'es' => {'online' => 'Solo On-line', 'printed' => 'Impreso y On-line'},
    'en' => {'online' => 'Online Only', 'printed' => 'Printed and Online'},
    'br' => {'online' => 'Somente On-line', 'printed' => 'Impresso e On-line'}
);

my $marca_online = $marca_labels{$lang}{'online'} || $marca_labels{'es'}{'online'};
my $marca_printed = $marca_labels{$lang}{'printed'} || $marca_labels{'es'}{'printed'};

while ($r=$stm0->fetchrow_hashref)
{
    my $marca = $r->{MARCA} == 1 ? $marca_online : $marca_printed;
    my $badge_class = $r->{MARCA} == 1 ? "badge-online" : "badge-printed";
    
    if ($r->{"CODIGO"} =~ /000$/)
    {
        if ($grid_abierto) {
            print "</div>"; # Cerrar grid anterior si existe
        }
        $categoria_actual = $r->{RUBRO_NOMBRE};
        print "<div class=\"rubro-category\">📁 $r->{RUBRO_NOMBRE}</div>";
        print "<div class=\"rubros-grid\">";
        $grid_abierto = 1;
        $subcategoria_actual = "";
    }
    elsif ($r->{"CODIGO"} =~ /00$/)
    {
        if ($grid_abierto) {
            print "</div>"; # Cerrar grid anterior
        }
        $subcategoria_actual = $r->{RUBRO_NOMBRE};
        print "<div class=\"rubro-subcategory\">📂 $r->{RUBRO_NOMBRE}</div>";
        print "<div class=\"rubros-grid\">";
        $grid_abierto = 1;
    }
    else 
    {
        print <<RUBROHTML;
                <div class="rubro-card" onclick="toggleRubroCard(event, '$r->{ID}')">
                    <label class="rubro-label">
                        <input type="checkbox" name="$r->{ID}" id="rubro_$r->{ID}" value="ok" class="custom-checkbox" onclick="event.stopPropagation()" onchange="updateCounter(); updateCardStyle('$r->{ID}')">
                        <div class="rubro-text">
                            <div>$r->{RUBRO_NOMBRE}</div>
                     
                        </div>
                    </label>
                </div>
RUBROHTML
    }
}

# Cerrar el último grid abierto
if ($grid_abierto) {
    print "</div>";
}

print <<EOFHTML;
            </div>
            </div>

            <div class="text-center mt-4" style="display: flex; gap: 15px; justify-content: center;">
                <button type="button" class="btn btn-secondary" onclick="history.back()" data-i18n="btnBack">
                    ← Volver
                </button>
                <button type="submit" class="btn btn-primary btn-lg" data-i18n="btnContinue">
                    Continuar al Paso 3 →
                </button>
            </div>
        </form>
    </div>
</div>

<script src="js/translations.js"></script>
<script>
// Cargar idioma en el paso 2
document.addEventListener('DOMContentLoaded', function() {
    const savedLang = '$lang';
    localStorage.setItem('selectedLanguage', savedLang);
    updateTexts(savedLang);
    document.getElementById('htmlLang').setAttribute('lang', savedLang === 'br' ? 'pt' : savedLang);
});

function toggleRubroCard(event, id) {
    // Solo toggle si no se hizo clic en el checkbox directamente
    if (event.target.type !== 'checkbox') {
        const checkbox = document.getElementById('rubro_' + id);
        checkbox.checked = !checkbox.checked;
        updateCounter();
        updateCardStyle(id);
    }
}

function updateCardStyle(id) {
    const checkbox = document.getElementById('rubro_' + id);
    const card = checkbox.closest('.rubro-card');
    if (checkbox.checked) {
        card.classList.add('selected');
    } else {
        card.classList.remove('selected');
    }
}

function updateCounter() {
    const lang = localStorage.getItem('selectedLanguage') || 'es';
    const t = translations[lang];
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const counter = document.getElementById('counter');
    const count = checkboxes.length;
    
    if (count === 0) {
        counter.textContent = t.noSelection;
        counter.style.background = '#fff3cd';
        counter.style.borderColor = '#ffc107';
        counter.style.color = '#856404';
    } else if (count === 1) {
        counter.textContent = t.selectedOne;
        counter.style.background = '#d1e7dd';
        counter.style.borderColor = '#10b981';
        counter.style.color = '#0f5132';
    } else {
        counter.textContent = t.selectedMany.replace('{n}', count);
        counter.style.background = '#d1e7dd';
        counter.style.borderColor = '#10b981';
        counter.style.color = '#0f5132';
    }
}

function validarSeleccion() {
    const lang = localStorage.getItem('selectedLanguage') || 'es';
    const t = translations[lang];
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    if (checkboxes.length === 0) {
        alert(t.validRubro);
        return false;
    }
    return true;
}

// Búsqueda en tiempo real
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();
        const cards = document.querySelectorAll('.rubro-card');
        
        cards.forEach(card => {
            const text = card.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});
</script>
</body>
</html>
EOFHTML


