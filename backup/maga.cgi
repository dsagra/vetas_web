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

$pagina=0;

$rev=$formulario{revista};
$pagina=$formulario{pag} if ($formulario{pag}!=0);
$paginastotal=$formulario{paginas};

if ($pagina == "0")
  {
  $pagina=1;
  }
$anterior=$pagina-1;
$proxima=$pagina+1;
if ($anterior == "0")
  {
  $anterior=1;
  }
if ($proxima == $paginastotal+1)
  {
  $proxima=$paginastotal;
  }

$stm10 = $dbh->prepare("select * from REVISTAS where REVISTA=$formulario{revista} and PAGINA=$pagina");
    $stm10->execute();
    if ($cont=$stm10->fetchrow_hashref)
      {  

      $co=$formulario{f};
      $co="CONTADOR" if ($co eq "");
      $contador=$cont->{$co}+1;

    $sql = "update REVISTAS set $co='$contador' where ID = $cont->{ID}";
    $dbh->do($sql);    
      }
      if ($formulario{orden}!=0)
      {
      $sql2= "update ORDEN set VISTO=1 where ID_ORDEN=$formulario{orden}";
      $dbh->do($sql2);
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
  $notitit="TE PUEDE INTERESAR";
    $leer="Leer noticia";
    $txtrevi="Revista VETAS";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
   $notitit="IT MAY INTEREST YOU";
     $leer="Read news";
     $txtrevi="VETAS Magazine";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
   $notitit="PODE LHE INTERESSAR";
     $leer="Ler not�cia";
     $txtrevi="Revista VETAS";
  }



$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);



$pag="./revista/".$rev."/".$pagina.".htm";


$pagprimera="maga.cgi?revista=".$rev."\&pag=1\&paginas=".$paginastotal."&i=".$idioma;
$paganterior="maga.cgi?revista=".$rev."\&pag=".$anterior."\&paginas=".$paginastotal."&i=".$idioma;
$pagproxima="maga.cgi?revista=".$rev."\&pag=".$proxima."\&paginas=".$paginastotal."&i=".$idioma;
$pagultima="maga.cgi?revista=".$rev."\&pag=".$paginastotal."\&paginas=".$paginastotal."&i=".$idioma;

print <<EOFHTML;

 <main role="main">

     <div class="container">

<div class="card">
  <div class="card-header">
  <div class="row"><div class="col-md-12 text-center"><h3>$txtrevi N$rev - $pagina/$paginastotal</h3></div></div>
 

<nav aria-label="Page navigation example" class="table-responsive mb-2">
  <ul class="pagination mb-0">
    <li class="page-item">
      <a class="page-link" href="$paganterior" tabindex="-1"><i class="fa fa-angle-left" aria-hidden="true"></i></a>
    </li>

EOFHTML

for (my $i=1; $i <= $paginastotal; $i++) {
  $pagnum="maga.cgi?revista=".$rev."\&pag=".$i."\&paginas=".$paginastotal."&i=".$idioma;
  $ch="./revista/$rev/".$i."c.jpg";
  $active="";
  $active=" active" if($pagina==$i);
print qq(    <li class="page-item $active" ><a class="page-link" href="$pagnum" ><img src="$ch"></a></li>\n);
}


$pagProximaTxt="Proxima";
$pagProximaTxt="Next" if ($idioma eq "en");
$pagProximaTxt="Proxima" if ($idioma eq "br");

$pagAnteriorTxt="Anterior";
$pagAnteriorTxt="Previous" if ($idioma eq "en");
$pagAnteriorTxt="Anterior" if ($idioma eq "br");



print <<EOFHTML;  
    <li class="page-item">
      <a class="page-link" href="$pagproxima"><i class="fa fa-angle-right" aria-hidden="true"></i></a>
    </li>
  </ul>
</nav>



  </div>
  <div class="container pt-3"><div class="row">
  <div class="col"><a class="btn btn-success btn-sm" href="$paganterior"><i class="fa fa-angle-left" aria-hidden="true"></i> $pagAnteriorTxt</a></div>
 <div class="col text-right" ><a class="btn btn-success btn-sm" href="$pagproxima">$pagProximaTxt <i class="fa fa-angle-right" aria-hidden="true"></i></a></div></div></div>
  <div class="card-body"> 
  
  <div class="center-block">
  <script>
  window.onload = function () {
    var ImageMap = function (map, img) {
            var n,
                areas = map.getElementsByTagName('area'),
                len = areas.length,
                coords = [],
                previousWidth = 621;
            for (n = 0; n < len; n++) {
                coords[n] = areas[n].coords.split(',');
            }
            this.resize = function () {
                var n, m, clen,
                    x = img.offsetWidth / previousWidth;
                for (n = 0; n < len; n++) {
                    clen = coords[n].length;
                    for (m = 0; m < clen; m++) {
                        coords[n][m] *= x;
                    }
                    areas[n].coords = coords[n].join(',');
                }
                previousWidth = img.offsetWidth;
                return true;
            };
            window.onresize = this.resize;
        },
        imageMap = new ImageMap(document.getElementById('map_ID'), document.getElementById('img_ID'));
    imageMap.resize();
    return;
}
</script>

EOFHTML



open pag;
  while (<pag>) 
    {
        $cliext="";
    if (/href="ID#(.+?)"/) {     
       $cliext = $1;
        $stm = $dbh->prepare("select * from USUARIOS where ID=$cliext"); 
        $stm->execute();
        if ($cliente=$stm->fetchrow_hashref)
          {
            $cemp=$cliente->{EMPRESA};      
          }
    }

    $link="https://www.vetas.com/empresa.cgi?c=REVISTA_CLICKS&i=$idioma&utm_source=web&utm_medium=revista&utm_campaign=$cemp&cliente=";
    $link="https://www.vetas.com/empresa.cgi?c=REVISTA_CLICKS&i=$idioma&utm_source=web&utm_medium=revista&utm_campaign=$cemp&cliente=" if ($formulario{rev} eq "DECO");
    $_ =~ s/<img src=\"/"<img id=\"img_ID\" src=\".\/revista\/$rev\/"/eg;
    $_ =~ s/<a /"<a target=\"_parent\" "/eg;
    $_ =~ s/<area/"<area target=\"_parent\" "/eg;
    $_ =~ s/ID#/"$link"/eg;
    $_ =~ s/\"621\"/"\"100\%\""/eg;
    $_ =~ s/height=\"855\"//eg;
    $_ =~ s/height=\"854\"//eg;
    $_ =~ s/<body>//eg;
      $_ =~ s/<map /"<map id=\"map_ID\""/eg;
    $_ =~ s/<html>//eg;
    $_ =~ s/<head>//eg;
    $_ =~ s/..\/imagenes\/vetas.jpg//eg;
   $_ =~ s/<title>Descargue Gratis la Revista VETAS<\/title>/"<title>$txtrevi Nº$rev<\/title>"/eg;


    
    print "$_";
    }



print <<EOFHTML;   
</div>
  
  </div>
<div class="container pb-3"><div class="row">
  <div class="col"><a class="btn btn-success btn-sm" href="$paganterior"><i class="fa fa-angle-left" aria-hidden="true"></i> $pagAnteriorTxt</a></div>
 <div class="col text-right" ><a class="btn btn-success btn-sm" href="$pagproxima">$pagProximaTxt <i class="fa fa-angle-right" aria-hidden="true"></i></a></div></div></div>
  <div class="card-footer">
<nav aria-label="Page navigation example" class="table-responsive mb-2">
  <ul class="pagination mb-0">
    <li class="page-item">
      <a class="page-link" href="$paganterior" tabindex="-1"><i class="fa fa-angle-left" aria-hidden="true"></i></a>
    </li>

EOFHTML

for (my $i=1; $i <= $paginastotal; $i++) {
  $pagnum="maga.cgi?revista=".$rev."\&pag=".$i."\&paginas=".$paginastotal."&i=".$idioma;
print qq(    <li class="page-item"><a class="page-link" href="$pagnum">$i</a></li>);
}


    


print <<EOFHTML;  
    <li class="page-item">
      <a class="page-link" href="$pagproxima"><i class="fa fa-angle-right" aria-hidden="true"></i></a>
    </li>
  </ul>
</nav>



   
</div>

</div>
       <br>
    </div>
    <!-- /container -->
  </main>


EOFHTML

open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}

$dbh->disconnect;