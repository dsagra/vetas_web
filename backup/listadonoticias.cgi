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
	$tm="TITULO";
	$cm="COPETE";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
	$tm="TITULO_EN";
	$cm="COPETE_EN";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
	$tm="TITULO_BR";
	$cm="COPETE_BR";
  }


$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);

$id=0;
$id=$formulario{id};

print <<EOFHTML;
<div class="container">
<div class="row">
<h1 >Noticias
        <small>Nacionales e Internacionales</small>
      </h1>
</div>
</div>
EOFHTML
$stm = $dbh->prepare("select  * from NOTAS where PUBLICADA=0 and ESPECIAL=0 and NOESP=0 ORDER BY FECHANOT desc,ID desc limit $id,9");
$stm->execute();
$cont=0;
while ($cont<3)
  {
    if ($noticias=$stm->fetchrow_hashref)
      {
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
            <div class="card container">
   <div class="row ">
          <div class="col-md-4">
              <img src="$fot" class="img-fluid" alt="Responsive image">
          </div>
          <div class="col-md-8">
            <h4 >
                <a  href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">$noticias->{$t}</a>
              </h4>
              <div class="text-muted">$noticias->{FECHANOT}</div>
               <p>$noticias->{$c}</p>
               
          </div>
          </div>
          </div>
          <p>
        );
        }
      }

&renglonbanner;

$cont=0;
while ($cont<3)
  {
    if ($noticias=$stm->fetchrow_hashref)
      {
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
            <div class="card container">
   <div class="row">
          <div class="col-md-4">
              <img src="$fot" class="img-fluid" alt="Responsive image">
          </div>
          <div class="col-md-8">
            <h4 >
                <a  href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">$noticias->{$t}</a>
              </h4>
              <div class="text-muted">$noticias->{FECHANOT}</div>
               <p>$noticias->{$c}</p>
               
          </div>
          </div>
          </div>
          <p>
        );
        }
      }
&renglonbanner;
$cont=0;
while ($cont<3)
  {
    if ($noticias=$stm->fetchrow_hashref)
      {
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
            <div class="card container">
   <div class="row ">
          <div class="col-md-4">
              <img src="$fot" class="img-fluid" alt="Responsive image">
          </div>
          <div class="col-md-8">
            <h4 >
                <a  href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">$noticias->{$t}</a>
              </h4>
              <div class="text-muted">$noticias->{FECHANOT}</div>
               <p>$noticias->{$c}</p>
               </div>
          </div>
          </div>
          <p>
        );
        }
      }
&renglonbanner;


$proximo=$id+9;
$anterior=$id-9;

print <<EOFHTML;
      <!-- Page Heading -->
      
      <!-- /.row -->

      <!-- Pagination -->
      <ul class="pagination justify-content-center">
        <li class="page-item">
          <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=$anterior" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
            <span class="sr-only">Previous</span>
          </a>
        </li>
EOFHTML
$stm = $dbh->prepare("select  *, count(ID) as cont from NOTAS where PUBLICADA=0 and ESPECIAL=0 and NOESP=0 ORDER BY FECHANOT ");
$stm->execute();
$noticias=$stm->fetchrow_hashref;
$total=($noticias->{cont}/9)-1;        
$a=0;
for ($i=0; $i<$total; $i++) { 
  $a=$i+1;
  $go=$i*9;
print qq(
        <li class="page-item">
          <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=$go">$a</a>
        </li>
        );
}
print <<EOFHTML;
        <li class="page-item">
          <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=$proximo" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
            <span class="sr-only">Next</span>
          </a>
        </li>
      </ul>

    </div>

EOFHTML

open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}



 sub renglonbanner{
print qq(
<div class="container">
  <div class="row">
    <div class="col-md-4">);
      &banne(174);
      &banne(174);
    print qq(<p></div>
        <div class="col-md-4">);

      &banne(174);
      &banne(174);
    print qq(<p></div>
        <div class="col-md-4">);
      &banne(174);
      &banne(174);
    print qq(<p></div>

  </div>

</div>);

} 


  sub banne{
($ancho,$alpe)=@_;
$stm13 = $dbh->prepare("select *, B.ID as IDBAN from BANNERS as B, USUARIOS as U  where B.ANCHO=$ancho and B.ACTIVO=1 and B.CLIENTE=U.ID and B.VETAS=1 and (U.ACTIVO_REVISTA!=0 or U.REVISTA='$config->{MUEBLE}' or U.ACTIVO_GUIA!=0 or U.ACTIVO=1) order by  B.EXPO, B.ORDEN,  RAND() limit 0,6");
$stm13->execute();
    $banners=$stm13->fetchrow_hashref;
print qq(<a href="empresa.cgi?cliente=$banners->{CLIENTE}&i=$idioma&c=BANNERS_CLICKS"><img src="../banners/$banners->{ARCHIVO}" alt="$banners->{EMPRESA}" width="49%"></a> ) if ($banners->{ENLACE} eq "");
print qq(<a href="$banners->{ENLACE}"><img src="../banners/$banners->{ARCHIVO}" alt="$banners->{EMPRESA}" width="49%"></a> ) if ($banners->{ENLACE} ne "");
        &contarbanner ($banners->{IDBAN});
}
    


sub contarbanner {
($banner,$alpe)=@_;
$stm6 = $dbh->prepare("select * from BANNERS where ID=$banner");
$stm6->execute();
if ($a=$stm6->fetchrow_hashref)
  {
  $cant=$a->{EXPO}+1;
  $cant=0 if ($cant>100);
  $sql = "update BANNERS set EXPO='$cant' where ID = $a->{ID}";
  $dbh->do($sql);
  }
fi;
}

$dbh->disconnect;