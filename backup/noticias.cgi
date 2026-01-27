#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use Entrada;
&Entrada;



use ConectarDB;
use Banners;
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
$tm="TITULO";
$cm="COPETE";
$nm="NOTA";
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  $notitit="TE PUEDE INTERESAR";
    $leer="Leer noticia";
  }
if ($idioma eq "en")
  {
$tm="TITULO_EN";
$cm="COPETE_EN";
$nm="NOTA_EN";
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
   $notitit="IT MAY INTEREST YOU";
     $leer="Read news";
  }
if ($idioma eq "br")
  {
$tm="TITULO_BR";
$cm="COPETE_BR";
$nm="NOTA_BR";
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
   $notitit="PODE LHE INTERESSAR";
     $leer="Ler notícia";
  }


$FOOTER="footer.html";
require "contador.cgi";
require "menu.cgi";
&menu($MENU);


$stm = $dbh->prepare("select  * from NOTAS where PUBLICADA=0 and ESPECIAL=0 and NOESP=0 and ID=$formulario{noticia} ORDER BY FECHANOT desc,ID desc limit 0,9");
$stm->execute();
$noticias=$stm->fetchrow_hashref;
	$t=$tm;
	$c=$cm;
	$n=$nm;
	$t="TITULO" if ($noticias->{$t} eq "");
	$c="COPETE" if ($noticias->{$c} eq "");
	$n="NOTA" if ($noticias->{$n} eq "");

$stm3 = $dbh->prepare("select  * from NOTAS_FOTOS where ID_NOTAS=$noticias->{ID} and SLIDER=0");
$stm3->execute();
$fot="https://www.vetas.com/notas/fotos/$noticias->{'ID'}_1.jpg";
if ($foto=$stm3->fetchrow_hashref)
  {
  $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
  }
if($formulario{NEWS}==1)
      {
      $contador=$noticias->{'NEWSLETTER'}+1;
      $sql = "update NOTAS set NEWSLETTER='$contador' where ID = $formulario{noticia}";
      }
    elsif($formulario{FACE}==1)
      {
      $contador=$noticias->{'FACEBOOK'}+1;
      $sql = "update NOTAS set FACEBOOK='$contador' where ID = $formulario{noticia}";
      }
    elsif($formulario{o}==1)
      {
      $contador=$noticias->{'OTRA'}+1;
      $sql = "update NOTAS set OTRA='$contador' where ID = $formulario{noticia}";
      }
          elsif($formulario{s}==1)
      {
      $contador=$noticias->{'SEARCH'}+1;
      $sql = "update NOTAS set SEARCH='$contador' where ID = $formulario{noticia}";
      }
    else
      {
      $contador=$noticias->{'CONTADOR'}+1;
      $sql = "update NOTAS set CONTADOR='$contador' where ID = $formulario{noticia}";
      }
    $dbh->do($sql);

print <<EOFHTML;

 <main role="main">

     <div class="container">
      <div class="row">
    <div class="col-md-8">
       <div class="row">        
        <div class="col-md-6">
         <img src="$fot" width="100%" class="img-fluid">
       </div>
       <div class="col-md-6">
           <div class="blog-post">
EOFHTML
print "<h1 align=\"center\"><a href=\"https://www.vetas.com/empresa.cgi?cliente=$noticias->{ID_CLIENTE}&i=$idioma&c=LOGO_CLICKS\"><img src=\"https://www.vetas.com/clientes/logos/$noticias->{ID_CLIENTE}.jpg\"></a></h1>" if ($noticias->{ID_CLIENTE}ne 0);

print <<EOFHTML;   
 <meta property="og:url"           content="https://www.vetas.com/noticias.cgi?i=es&noticia=$noticias->{ID}" />
  <meta property="og:type"          content="website" />
<meta property="og:title" content="$noticias->{$t}" />
<meta property="og:description" content="$noticias->{$c}" />
<meta property="og:image" content="$fot" />
<title>$noticias->{$t}</title>
            <h2 class="blog-post-title">$noticias->{$t}</h2>
            <p class="blog-post-meta">$noticias->{FECHANOT} - $noticias->{FUENTE}




 <div id="fb-root"></div>
  <script>(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));</script>

  <!-- Your share button code -->
  <div class="fb-share-button" 
    data-href="https://www.vetas.com/noticias.cgi?i=es&noticia=$noticias->{ID}" 
    data-layout="button" data-size="small"><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https://www.vetas.com/noticias.cgi?i=es&noticia=$noticias->{ID};src=sdkpreparse" class="fb-xfbml-parse-ignore">Compartir</a>
  </div>
            </p> 
            
          </div>
        </div>
        <div class="col-md-12">
 <div class="blog-post">
 <h4 class="blog-post-subtitle">$noticias->{$c}</h4>
            $noticias->{$n}
          </div>
EOFHTML

 print <<EOFHTML;   
</div>



   
<div class="row">
EOFHTML

        while ($foto=$stm3->fetchrow_hashref)
        {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
             
          print qq(<div class="col-md-6"><img src="$fot" width="100%" class="img-fluid"> </div>);
        }
print qq(</div><br>);
 banne2(1200, $dbh, $revi, $idioma);

 print <<EOFHTML;   
<p>
<div class="row">

 <div class="col-md-12">
          <h3 class="pb-3 mb-4 font-italic border-bottom">
            $notitit
          </h3>
      </div>
EOFHTML
$cont=0;
$stm = $dbh->prepare("select * from (select * from NOTAS as N where N.PUBLICADA=0 and N.ESPECIAL=0 and N.NOESP=0 and N.SLIDER=0  and N.ID<>$formulario{noticia} ORDER BY N.FECHANOT desc,N.ID desc limit 0,9) as F order by RAND()");
$stm->execute();
while ($cont<3)
    {
    $noticias=$stm->fetchrow_hashref; 
	$t=$tm;
	$c=$cm;
	$n=$nm;
	$t="TITULO" if ($noticias->{$t} eq "");
	$c="COPETE" if ($noticias->{$c} eq "");
	$n="NOTA" if ($noticias->{$n} eq ""); 
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
            <img class="card-img-top" src="$fot" alt="Card image cap">
            <b>$noticias->{$t}</b>
            <p>$noticias->{$c}</p>
            <p><a class="btn btn-secondary" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}&o=1" role="button">$leer &raquo;</a></p>


          </div>
          );
      }





print <<EOFHTML;        

      </div>

     </div>
    </div>
             <div class="col-md-4">
EOFHTML

for (my $i=0; $i <= 10; $i++) {

print qq(<div class="row"><div class="col-md-6">);
          banne(174, $dbh, $revi, $idioma);
print qq(</div><div class="col-md-6">);
         banne(174, $dbh, $revi, $idioma);
print qq(</div></div><p><p>);
}


print <<EOFHTML;   
        </div>
      </div>
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
