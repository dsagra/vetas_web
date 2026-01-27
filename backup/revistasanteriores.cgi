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
  $sp="SP";
  $rev="Revista VETAS";
  $mes="MES";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  $sp="EN";
  $rev="VETAS Magazine";
  $mes="MES_EN";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  $sp="BR";
  $rev="Revista VETAS";
  $mes="MES_BR";
  }


$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);

print <<EOFHTML;

  <main role="main">

    <div class="container">
EOFHTML
$x=0;
$stm2 = $dbh->prepare("select * from REVISTAS_CONFIG order by REVISTA desc limit 0,22");
$stm2->execute();
while ($revista=$stm2->fetchrow_hashref)
  {
print qq(<div class="row mb-2">) if ($x==0);
$x++;
print <<EOFHTML;
    
        <div class="col-md-6">
          <div class="card flex-md-row mb-4 box-shadow h-md-250">
            <div class="card-body d-flex flex-column align-items-start">
              <h4 class="mb-0">
                <a class="text-dark" href="maga.cgi?revista=$revista->{REVISTA}&paginas=$revista->{PAGINAS}&i=$idioma">$rev Nº$revista->{REVISTA}</a>
              </h4>
              <div class="mb-1 text-muted">$revista->{$mes}</div>
EOFHTML

$stm3 = $dbh->prepare("select * from REVISTAS where REVISTA=$revista->{REVISTA}  order by PAGINA");
$stm3->execute();
$c=1;
while ($notas=$stm3->fetchrow_hashref)
	{
	print qq(<a href="maga.cgi?revista=$notas->{REVISTA}&paginas=$revista->{PAGINAS}&pag=$notas->{PAGINA}&i=$idioma" class="titvetas" ><span class="glyphicon glyphicon-star"  aria-hidden="true"></span> $notas->{$sp}</a>)
	}
 

      print <<EOFHTML;
       
      
               
            </div>
           <a class="text-dark"  href="maga.cgi?revista=$revista->{REVISTA}&paginas=$revista->{PAGINAS}&i=$idioma"> <img class="card-img-right flex-auto d-none d-lg-block" src="revista/$revista->{REVISTA}/1g.jpg" width="150px" height="210px" alt="Card image cap"></a>
          </div>
        </div>
EOFHTML


if ($x==2)
  {
    $x=0;
    print qq(</div>);
  }
}


print <<EOFHTML;


  </main>


EOFHTML

open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}