#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use Entrada;
&Entrada;


use ConectarDB;
$dbh=ConectarDB->connectWeb();

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
        $envi=$envi."?i=es";
      }
  }

$idioma="es";
$idioma=$formulario{i} if ($formulario{i} eq "br" or $formulario{i} eq "en" );
$MENU="menu.html";
$MENU="menu_en.html" if ($idioma eq "en") ;
$MENU="menu_br.html" if ($idioma eq "br") ;
if ($idioma eq "es")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  $titulo="Guía Internacional de la Industria Maderera";
  $subtitulo="Equipos, Herrajes, Herramientas, Materiales, Maderas y Máquinas";
  $subtitulo2="Busque los datos (teléfono, fax, e-mail, dirección) de proveedores de productos o servicios.";
  $rub="RUBRO_ES";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
    $titulo="International Wood Industry Directory";
  $subtitulo="Equipments, Hardware, machinery, Materials, Tooling and Woods";
  $subtitulo2="Use our search engine to find a company or product in the directory.";
  $rub="RUBRO_EN";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
    $titulo="Cadastro Internacional da Industria Madeireira";
  $subtitulo="Equipas, Herrajes, Ferramentas, Materiais, Madeiras e Maquinas";
  $subtitulo2="Procure os dados (telefono, fax, e-mail, direccion) de provedores de produtos ou serviços.";
  $rub="RUBRO_BR";
  }


$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);


print <<EOFHTML;
 <main role="main" class="bg-negro">
        <div class="container">
          <h2 class="text-center text-guia"><b>$titulo</b></h2>
          <h4 class="text-center text-guia">$subtitulo</h4>
          <p class="text-center text-white">$subtitulo2</p>
        </div>
        <div class="container">
        <!-- Example row of columns -->
EOFHTML

$stm = $dbh->prepare("select * from RUBROS_NUEVO where SALE_EN_GUIA=1 ORDER BY CODIGO,$rub");
$stm->execute();
$marca=0;
while ($rubro=$stm->fetchrow_hashref)
  {

  if ($rubro->{'CODIGO'} =~ /000/)
    {
    if ($marca==1)
      {
        $marca=0;
        print qq(</div>
        <p>);
      }
    $codigo=$rubro->{'CODIGO'};
    $codigo=~ (s/000//);
    
    print qq(
        <div class="row border shadow">
          <div class="col-md-12">
            <h3 class="text-center text-white "><a href="guiaresultados.cgi?COD=$codigo&r=$rubro->{$rub}&i=$idioma" class="titguia">$rubro->{$rub}</a></h3>
          </div>
          );    
    $marca=1;
    }
  elsif ($rubro->{'CODIGO'} =~ /00/)
    {
    $codigo=$rubro->{'CODIGO'};
    $codigo=~ (s/00//);
$foto="https://www.vetas.com/guia/fotos/".$rubro->{ID}.".jpg";
    
    print qq(
          <div class="col-md-2">
            <a   href="guiaresultados.cgi?COD=$codigo&r=$rubro->{$rub}&i=$idioma"><img class="rounded" src="$foto" width="100%"></a>
            <p class="text-center text-white"><a href="guiaresultados.cgi?COD=$codigo&r=$rubro->{$rub}&i=$idioma" class="titguia">$rubro->{$rub}</a></p>
          </div>
          );
    }
  fi;

  }
        print qq(</div>
        <p>);

        

print <<EOFHTML;    

      </div> <!-- /container -->

    </main>
EOFHTML

open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}

$dbh->disconnect;
