#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use Entrada;
&Entrada;

use Banners;

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


$avisorevista=$revi->{REVISTA};
$avisorevista=$revi->{GUIA} if ($revi->{GUIA}>$revi->{REVISTA});
$idioma="es";
$idioma=$formulario{i} if ($formulario{i} eq "br" or $formulario{i} eq "en" );
if ($idioma eq "es")
  {
  $MENU="menu.html";
  $vet= "Revista VETAS";
  $mes= "REVISTAMES";
  $idi="SP";
  $notitit="Noticias";
  $leer="Leer noticia";
  $ivideo="TITULO_ES";
  $guia="Guia Maderera";
  $fertxt="Ferias y Eventos";
    $verempresa="Ver empresa";
$tm="TITULO";
$cm="COPETE";
  $volver="$envi";
  $volver2="$envi";
$volver3="$envi";
  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  }
if ($idioma eq "en")
  {
  $MENU="menu_en.html";
  $vet= "VETAS Magazine";
  $mes= "REVISTAMES_EN";
  $idi="EN";
  $notitit="News";
  $guia="Wood Directory";
  $leer="Read news";
  $ivideo="TITULO_EN";
  $fertxt="Fairs and Exhibitions";
   $verempresa="View company";
$tm="TITULO_EN";
$cm="COPETE_EN";
  $volver="$envi";
  $volver2="$envi";
$volver3="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  }
if ($idioma eq "br")
  {
  $MENU="menu_br.html";
  $vet= "Revista VETAS";
  $mes= "REVISTAMES_BR";
  $guia="Cadastro Madeireiro";
  $idi="BR";
  $notitit="Novidades";
  $leer="Ler not�cia";
  $ivideo="TITULO_BR";
  $fertxt="Feiras";
  $verempresa="Ver empresa";
$tm="TITULO_BR";
$cm="COPETE_BR";
  $volver="$envi";
  $volver2="$envi";
$volver3="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  }


require "menu.cgi";
&menu($MENU);


if ($idioma eq "es")
  {
  	$edi="Ver ediciones anteriores";
  print qq(  <title>VETAS - El mundo de la madera y el mueble</title>);
  }
if ($idioma eq "en")
  {
$edi="See previous editions";
  print qq(  <title>VETAS - The world of wood and furniture</title>);
  }
if ($idioma eq "br")
  {
$edi="Veja as edi��es anteriores";
  print qq(  <title>VETAS - El mundo de la madera y el mueble</title>);
  }
require "contador.cgi";

$FOOTER="footer.html";



print <<EOFHTML;



  <main role="main">

 <div class="container">

  <div class="row"">
    <div class="col-md-12">
EOFHTML
       &banne2(1200, $dbh, $revi, $idioma);
print <<EOFHTML;
    </div>
        

  </div>

</div>
       <p>
      </div>
    <div class="container">
    <div class="row mb-2">
        <div class="col-md-6">
          <div class="card flex-md-row mb-4 box-shadow h-md-250">
            <div class="card-body d-flex flex-column align-items-start">
              <h4 class="mb-0">
                <a class="text-dark"  href="maga.cgi?i=$idioma&revista=$revi->{REVISTA}&paginas=$revista->{PAGINAS}&indice=$revista->{INDICE}">$vet N$revi->{REVISTA}</a>
              </h4>
              <div class="mb-1 text-muted">$revi->{$mes}</div>
EOFHTML

$stm3 = $dbh->prepare("select * from REVISTAS where REVISTA=$revi->{REVISTA}  order by PAGINA");
$stm3->execute();
$c=1;

$guiaMes="Febrero 2025";
$guiaMes="February 2025" if ($idioma eq "en");
$guiaMes="Fevereiro 2025" if ($idioma eq "br");
$guiaCantPaginas=72;

while ($notas=$stm3->fetchrow_hashref)
	{

	print qq(<a href="maga.cgi?i=$idioma&revista=$notas->{REVISTA}&indice=$revista->{INDICE}&paginas=$revista->{PAGINAS}&pag=$notas->{PAGINA}" class="titvetas" ><span class="glyphicon glyphicon-star"  aria-hidden="true"></span> $notas->{$idi}</a>)
	}

print <<EOFHTML;
               
          <a href="revistasanteriores.cgi?i=$idioma">$edi</a>
               
            </div>
            <a href="maga.cgi?i=$idioma&revista=$revi->{REVISTA}&indice=$revista->{INDICE}&paginas=$guiaCantPaginas&pag=1" class="titvetas" ><img class="card-img-right flex-auto d-none d-lg-block" src="revista/$revista->{REVISTA}/1g.jpg" width="150px" height="210px" alt="Card image cap"></a>
          </div>
        </div>

        <div class="col-md-6">
          <div class="card flex-md-row mb-4 box-shadow h-md-250">
            <div class="card-body d-flex flex-column align-items-start">
              <h4 class="mb-0">
                <a class="text-dark" href="maga.cgi?revista=$revi->{GUIA}&paginas=$guiaCantPaginas" target="_blank">$guia</a>
              </h4>
              <div class="mb-1 text-muted">$guiaMes</div>
EOFHTML

$stm3 = $dbh->prepare("select * from REVISTAS where REVISTA=$revi->{GUIA}  order by PAGINA");
$stm3->execute();
$c=1;
while ($notas=$stm3->fetchrow_hashref)
  {
    print qq(<a href="maga.cgi?revista=$revi->{GUIA}&paginas=$guiaCantPaginas&pag=$notas->{PAGINA}" class="titvetas" ><span class="glyphicon glyphicon-star"  aria-hidden="true"></span> $notas->{$idi}</a>)
  }

print <<EOFHTML;
  
            </div>
            <a class="text-dark" href="maga.cgi?revista=$revi->{GUIA}&paginas=$guiaCantPaginas" ><img class="card-img-right flex-auto d-none d-lg-block" src="revista/$revi->{GUIA}/1g.jpg" width="150px" height="210px" alt="Card image cap"></a>
          </div>
        </div>
              </div>
    </div>

<div class="container">
        <!-- Example row of columns -->
          <div class="row">
 <div class="col-md-12">
          <h3 class="pb-3 mb-4 font-italic border-bottom">
            $notitit
          </h3>
      </div>
    </div>
        <div class="row">
EOFHTML


$cont=0;
$stm = $dbh->prepare("select  * from NOTAS where PUBLICADA=0 and ESPECIAL=0 and NOESP=0  and SLIDER=0  and HOMEPAGE=0 ORDER BY FECHANOT desc,ID desc limit 0,9");
$stm->execute();
while ($cont<3)
		{


    $noticias=$stm->fetchrow_hashref;  
	$t=$tm;
	$c=$cm;
	$t="TITULO" if ($noticias->{$t} eq "");
	$c="COPETE" if ($noticias->{$c} eq "");
		$cont++;
		$stm3 = $dbh->prepare("select  * from NOTAS_FOTOS where ID_NOTAS=$noticias->{ID} and SLIDER=0");
		$stm3->execute();
        $fot="https://www.vetas.com/notas/fotos/$noticias->{'ID'}_1.jpg";
        if ($foto=$stm3->fetchrow_hashref)
          {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
          }

          print qq(



          <div class="col-md-4">
            <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" ><img class="card-img-top" src="$fot" alt="Card image cap"></a>
            <h2>$noticias->{$t}</h2>
            <p>$noticias->{$c}</p>
            <p><a class="btn btn-secondary" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a></p>
          </div>
          );
      }


     #  print qq(


#
 #         <div class="col-md-4">
  #          <a href="expovetasdigital/index.cgi?i=$idioma" ><img class="card-img-top" src="./VETAS.jpg" alt="Card image cap"></a>
   #          </div>
    #      );

print <<EOFHTML;

        </div>

  <p>

      </div>
<div class="container">
  <div class="row"">
    <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;
    </div>
        <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
    </div>
        <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
    </div>

  </div>

</div>

<div class="container" >
        <!-- Example row of columns -->

        <div class="row">

EOFHTML
$cont=0;

while ($cont<2)
		{
      $noticias=$stm->fetchrow_hashref;
	$t=$tm;
	$c=$cm;
	$t="TITULO" if ($noticias->{$t} eq "");
	$c="COPETE" if ($noticias->{$c} eq "");
		$cont++;
		$stm3 = $dbh->prepare("select  * from NOTAS_FOTOS where ID_NOTAS=$noticias->{ID} and SLIDER=0");
		$stm3->execute();
        $fot="https://www.vetas.com/notas/fotos/$noticias->{'ID'}_1.jpg";
        if ($foto=$stm3->fetchrow_hashref)
          {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
          }

          print qq(

          <div class="col-md-4">
            <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" ><img class="card-img-top" src="$fot" alt="Card image cap"></a>
            <h2>$noticias->{$t}</h2>
            <p>$noticias->{$c}</p>
            <p><a class="btn btn-secondary" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a></p>
          </div>
          );
      }

print <<EOFHTML;
          
          <div class="col-md-4">
            <div class="container grisclaro">
          <h3 class="pb-3 mb-4 font-italic border-bottom">
            $fertxt
          </h3>

EOFHTML
$stm32 = $dbh->prepare("SELECT * FROM `FERIAS` WHERE FIN >NOW() order by INICIO limit 0,6");
$stm32->execute();
while ($feria=$stm32->fetchrow_hashref)
  {

print qq(
          <div class="container row mb-2">
            <div class="mb-0"><a href="https://$feria->{SITE}" target="_blank" class="titferias">$feria->{NOMBRE}</a></div>
            <div class="mb-1 text-muted feriasfecha">$feria->{PAIS} - $feria->{INICIO}/$feria->{FIN}</div>
          </div>
          );

  }


    
 print <<EOFHTML;    
          </div>     
          </div>
        </div>

  <p>

      </div>
<div class="container">
  <div class="row"">
    <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;
    </div>
        <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
    </div>
        <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
    </div>

  </div>

</div>

<div class="container">
        <!-- Example row of columns -->
         <div class="row">

EOFHTML

$noticias=$stm->fetchrow_hashref;
	$t=$tm;
	$c=$cm;
	$t="TITULO" if ($noticias->{$t} eq "");
	$c="COPETE" if ($noticias->{$c} eq "");
    $stm3 = $dbh->prepare("select  * from NOTAS_FOTOS where ID_NOTAS=$noticias->{ID} and SLIDER=0");
    $stm3->execute();
        $fot="https://www.vetas.com/notas/fotos/$noticias->{'ID'}_1.jpg";
        if ($foto=$stm3->fetchrow_hashref)
          {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
          }

          print qq(

          <div class="col-md-4">
            <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" ><img class="card-img-top" src="$fot" alt="Card image cap"></a>
            <h2>$noticias->{$t}</h2>
            <p>$noticias->{$c}</p>
            <p><a class="btn btn-secondary" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a></p>
          </div>
          );

$stm5 = $dbh->prepare("select  * from ORDEN as O, FOTOS AS F where O.REVISTA=$avisorevista and F.CLIENTE=O.ID_CLIENTE and F.REVISTA=$avisorevista and (F.FORMATO='PAGINA' or F.FORMATO='CUARTO') order by RAND()");
$stm5->execute();
$aviso=$stm5->fetchrow_hashref;
$fot="https://www.vetas.com/clientes/fotos/".$aviso->{ARCHIVO};
print <<EOFHTML;         
          
           <div class="col-md-4">
            <a href="empresa.cgi?cliente=$aviso->{ID_CLIENTE}&i=$idioma&c=AVISO_CLICKS"><img class="imgaviso" src="$fot" width="100%"></a>
          </div>
EOFHTML

$noticias=$stm->fetchrow_hashref;
	$t=$tm;
	$c=$cm;
	$t="TITULO" if ($noticias->{$t} eq "");
	$c="COPETE" if ($noticias->{$c} eq "");
    $stm3 = $dbh->prepare("select  * from NOTAS_FOTOS where ID_NOTAS=$noticias->{ID} and SLIDER=0");
    $stm3->execute();
        $fot="https://www.vetas.com/notas/fotos/$noticias->{'ID'}_1.jpg";
        if ($foto=$stm3->fetchrow_hashref)
          {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
          }

          print qq(

          <div class="col-md-4">
            <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" ><img class="card-img-top" src="$fot" alt="Card image cap"></a>
            <h2>$noticias->{$t}</h2>
            <p>$noticias->{$c}</p>
            <p><a class="btn btn-secondary" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a></p>
          </div>
          );

print <<EOFHTML; 

        </div>

   <p>

      </div>
<div class="container">
  <div class="row"">
    <div class="col-md-4">
EOFHTML
       #&banne(174);
print <<EOFHTML;
    </div>
        <div class="col-md-4">


EOFHTML
       #&banne(174);

print <<EOFHTML;      
    </div>
        <div class="col-md-4">
EOFHTML
       #&banne(174);

$stm40 = $dbh->prepare("select * from USUARIOS as U, VIDEOS AS V where U.ID=V.CLIENTE and (U.ACTIVO_REVISTA!=0  or U.ACTIVO_GUIA!=0 or U.ACTIVO=1) and V.TIPO=0 order by RAND()"); 


$stm40->execute();
$video1=$stm40->fetchrow_hashref;
$video2=$stm40->fetchrow_hashref;
    


print <<EOFHTML;      
    </div>

  </div>

</div>

<div class="container">
        <!-- Example row of columns -->
          <div class="row">
 <div class="col-md-8">
          <h3 class="pb-3 mb-4 font-italic border-bottom">
            Videos
          </h3>
      </div>
    </div>
        <div class="row">
          <div class="col-md-4">
            <div class="embed-responsive embed-responsive-16by9">
             <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/$video1->{VIDEO}?rel=0" allowfullscreen></iframe>
            </div>
            <p><strong>$video1->{$ivideo}</strong></p>
            <p><a class="btn btn-secondary" href="empresa.cgi?cliente=$video1->{CLIENTE}&i=$idioma&c=VIDEO_CLICKS" role="button">$verempresa &raquo;</a></p>
          </div>
          <div class="col-md-4">
            <div class="embed-responsive embed-responsive-16by9">
             <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/$video2->{VIDEO}?rel=0" allowfullscreen></iframe>
            </div>
            <p><strong>$video2->{$ivideo}</strong></p>
            <p><a class="btn btn-secondary" href="empresa.cgi?cliente=$video2->{CLIENTE}&i=$idioma&c=VIDEO_CLICKS" role="button">$verempresa &raquo;</a></p>
          </div>
EOFHTML
$stm5 = $dbh->prepare("select  * from ORDEN as O, FOTOS AS F where O.REVISTA=$avisorevista and F.CLIENTE=O.ID_CLIENTE and F.REVISTA=$avisorevista and (F.FORMATO='OCTAVO' or F.FORMATO='MEDIA') order by RAND()");
$stm5->execute();
$aviso=$stm5->fetchrow_hashref;
$fot="https://www.vetas.com/clientes/fotos/".$aviso->{ARCHIVO};
print <<EOFHTML;         
          
           <div class="col-md-4">
            <a href="empresa.cgi?cliente=$aviso->{ID_CLIENTE}&i=$idioma&c=AVISO_CLICKS"><img class="imgaviso" src="$fot" width="100%"></a>
          </div>


   <p>

      </div>
<div class="container">
  <div class="row"">
    <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;
    </div>
        <div class="col-md-4">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
    </div>
        <div class="col-md-4">

EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
    </div>

  </div>

</div>








EOFHTML

open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}




$dbh->disconnect;