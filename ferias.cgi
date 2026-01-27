#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use Entrada;
&Entrada;


use ConectarDB;
$dbh=ConectarDB->connectWeb();
$dbh->do("SET NAMES 'utf8'");
$dbh->do("SET CHARACTER SET utf8");

$stm2 = $dbh->prepare("select * from CONFIG where ID=1");
$stm2->execute();
$revi=$stm2->fetchrow_hashref;

$stm2 = $dbh->prepare("select * from REVISTAS_CONFIG where REVISTA=$revi->{REVISTA}");
$stm2->execute();
$revista=$stm2->fetchrow_hashref;
$stm2 = $dbh->prepare("select * from REVISTAS_CONFIG where REVISTA=$revi->{MUEBLE}");
$stm2->execute();
$mueble=$stm2->fetchrow_hashref;

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
        $envi=$envi."?id=0&i=es";
      }
  }

# Asegurar que la URL tenga el parámetro id ANTES de definir volver y volver2
if ($envi !~ m/id=/) {
  if ($envi =~ m/\?/) {
    $envi=$envi."&id=0";
  }
  else
    {
      $envi=$envi."?id=0";
    }
}

$idioma="es";
$idioma=$formulario{i} if ($formulario{i} eq "br" or $formulario{i} eq "en" );
$MENU="menu.html";
$MENU="menu_en.html" if ($idioma eq "en") ;
$MENU="menu_br.html" if ($idioma eq "br") ;

# Títulos según idioma
if ($idioma eq "es")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  $titulo="Ferias";
  $subtitulo="Calendario de Ferias Internacionales";
  $nombre_label="Nombre";
  $pais_label="Pa&iacute;s";
  $fecha_label="Fecha";
  $sitio_label="Sitio Web";
  $buscar_label="Buscar";
  $buscar_placeholder="Buscar por nombre o pa&iacute;s...";
  $limpiar_label="Limpiar";
  $no_resultados="No se encontraron ferias que coincidan con tu b&uacute;squeda.";
  $intenta_nuevo="Intenta con otro t&eacute;rmino de b&uacute;squeda.";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  $titulo="Trade Shows";
  $subtitulo="International Trade Shows Calendar";
  $nombre_label="Name";
  $pais_label="Country";
  $fecha_label="Date";
  $sitio_label="Website";
  $buscar_label="Search";
  $buscar_placeholder="Search by name or country...";
  $limpiar_label="Clear";
  $no_resultados="No trade shows found matching your search.";
  $intenta_nuevo="Try a different search term.";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  $titulo="Feiras";
  $subtitulo="Calend&aacute;rio de Feiras Internacionais";
  $nombre_label="Nome";
  $pais_label="Pa&iacute;s";
  $fecha_label="Data";
  $sitio_label="Site";
  $buscar_label="Pesquisar";
  $buscar_placeholder="Pesquisar por nome ou pa&iacute;s...";
  $limpiar_label="Limpar";
  $no_resultados="Nenhuma feira encontrada correspondente &agrave; sua pesquisa.";
  $intenta_nuevo="Tente um termo de pesquisa diferente.";
  }


$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);

$id=0;
$id=$formulario{id} if ($formulario{id} ne "");
$id=0 if ($id eq "" || $id < 0);

# Obtener término de búsqueda
$busqueda = $formulario{buscar} || "";
$busqueda =~ s/^\s+|\s+$//g; # Trim espacios

print <<EOFHTML;
<div class="container mt-4">
<div class="row mb-4">
  <div class="col-md-12 text-center">
    <h1 class="display-4">$titulo</h1>
    <p class="lead text-muted">$subtitulo</p>
  </div>
</div>

<!-- Buscador -->
<div class="row mb-4">
  <div class="col-md-12">
    <div class="card shadow-sm">
      <div class="card-body">
        <form method="get" action="ferias.cgi" class="form-inline justify-content-center">
          <input type="hidden" name="i" value="$idioma">
          <input type="hidden" name="id" value="0">
          <div class="input-group" style="max-width: 800px; width: 100%;">
            <input type="text" class="form-control form-control-lg" name="buscar" value="$busqueda" placeholder="$buscar_placeholder">
            <div class="input-group-append">
              <button class="btn btn-lg" type="submit" style="background-color: #72bf44; color: white; border-color: #72bf44;">
                <i class="fas fa-search"></i> $buscar_label
              </button>
              <a href="ferias.cgi?i=$idioma&id=0" class="btn btn-outline-secondary btn-lg">
                <i class="fas fa-times"></i> $limpiar_label
              </a>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>

</div>

<div class="container mb-5">
EOFHTML

# Construir consulta SQL con filtro de búsqueda
$sql_where = "WHERE INICIO >= CURDATE()";
if ($busqueda ne "") {
    $busqueda_escaped = $dbh->quote("%$busqueda%");
    $sql_where .= " AND (NOMBRE LIKE $busqueda_escaped OR PAIS LIKE $busqueda_escaped)";
}

# Consulta para obtener las ferias futuras ordenadas por fecha de inicio
$stm = $dbh->prepare("select * from FERIAS $sql_where ORDER BY INICIO ASC limit $id,9");
$stm->execute();
$cont=0;
$hay_resultados=0;

while ($feria=$stm->fetchrow_hashref)
  {
    $hay_resultados=1;
    # Formatear fechas
    $fecha_inicio = $feria->{INICIO};
    $fecha_fin = $feria->{FIN};
    
    # Convertir formato de fecha si es necesario
    if ($fecha_inicio =~ /(\d{4})-(\d{2})-(\d{2})/) {
        $fecha_inicio_format = "$3/$2/$1";
    }
    if ($fecha_fin =~ /(\d{4})-(\d{2})-(\d{2})/) {
        $fecha_fin_format = "$3/$2/$1";
    }
    
    $fecha_display = "$fecha_inicio_format - $fecha_fin_format";
    
    # Preparar el enlace al sitio web
    $sitio_web = $feria->{SITE};
    $sitio_link = "";
    if ($sitio_web ne "" && $sitio_web ne "NULL") {
        # Asegurar que el enlace tenga http:// o https://
        if ($sitio_web !~ /^https?:\/\//) {
            $sitio_web = "http://" . $sitio_web;
        }
        $sitio_link = qq(<a href="$sitio_web" target="_blank" class="btn btn-sm" style="background-color: #72bf44; color: white; border-color: #72bf44;"><i class="fas fa-external-link-alt"></i> $sitio_label</a>);
    }
    
    print qq(
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-md-8">
                        <h4 class="card-title mb-3"><i class="fas fa-calendar-alt text-primary"></i> $feria->{NOMBRE}</h4>
                        <p class="card-text mb-2">
                            <i class="fas fa-map-marker-alt text-danger"></i> 
                            <strong>$pais_label:</strong> $feria->{PAIS}
                        </p>
                        <p class="card-text mb-2">
                            <i class="fas fa-clock text-success"></i> 
                            <strong>$fecha_label:</strong> $fecha_display
                        </p>
                    </div>
                    <div class="col-md-4 text-right">
                        $sitio_link
                    </div>
                </div>
            </div>
        </div>
    );
  }

# Mostrar mensaje si no hay resultados
if ($hay_resultados == 0) {
    print qq(
        <div class="row">
            <div class="col-md-12">
                <div class="alert alert-warning text-center" role="alert">
                    <h4 class="alert-heading"><i class="fas fa-exclamation-triangle"></i> $no_resultados</h4>
                    <p class="mb-0">$intenta_nuevo</p>
                </div>
            </div>
        </div>
    );
}


$proximo=$id+9;
$anterior=$id-9;
$anterior=0 if ($anterior<0);
$buscar_param = $busqueda ne "" ? "&buscar=$busqueda" : "";

print <<EOFHTML;
      <!-- Pagination -->
      <div class="row mt-5 mb-4">
        <div class="col-md-12">
          <ul class="pagination justify-content-center">
            <li class="page-item">
              <a class="page-link" href="ferias.cgi?i=$idioma&id=$anterior$buscar_param" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
EOFHTML

use POSIX qw(ceil);
$stm = $dbh->prepare("select count(ID) as cont from FERIAS $sql_where");
$stm->execute();
$feria=$stm->fetchrow_hashref;
$total_ferias = $feria->{cont};
$total_paginas = ceil($total_ferias / 9);

for ($i=0; $i<$total_paginas; $i++) { 
  $a=$i+1;
  $go=$i*9;
  $active_class = ($go == $id) ? "active" : "";
  $buscar_param = $busqueda ne "" ? "&buscar=$busqueda" : "";
print qq(
            <li class="page-item $active_class">
              <a class="page-link" href="ferias.cgi?i=$idioma&id=$go$buscar_param">$a</a>
            </li>
        );
}
print <<EOFHTML;
            <li class="page-item">
              <a class="page-link" href="ferias.cgi?i=$idioma&id=$proximo$buscar_param" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </div>
      </div>

    </div>

EOFHTML

open FOOTER, $FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}
close FOOTER;

$dbh->disconnect;
