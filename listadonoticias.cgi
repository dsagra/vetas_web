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
	$titulo_pagina="Noticias";
	$subtitulo_pagina="Nacionales e Internacionales";
	$leer_noticia="Leer noticia";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
	$tm="TITULO_EN";
	$cm="COPETE_EN";
	$titulo_pagina="News";
	$subtitulo_pagina="National and International";
	$leer_noticia="Read news";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
	$tm="TITULO_BR";
	$cm="COPETE_BR";
	$titulo_pagina="Not&iacute;cias";
	$subtitulo_pagina="Nacionais e Internacionais";
	$leer_noticia="Ler not&iacute;cia";
  }


$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);

$id=0;
$id=$formulario{id};

print <<EOFHTML;
<style>
  :root {
    --vetas-primary: #72bf44;
    --vetas-dark: #2c5f2d;
    --vetas-light: #e8f5e0;
    --text-dark: #2c3e50;
    --text-light: #6c757d;
  }

  .news-list-card {
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    margin-bottom: 2rem;
    transition: all 0.3s ease;
  }

  .news-list-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(114, 191, 68, 0.2);
  }

  .news-list-card .row {
    align-items: center;
  }

  .news-list-image {
    aspect-ratio: 1 / 1;
    overflow: hidden;
  }

  .news-list-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }

  .news-list-card:hover .news-list-image img {
    transform: scale(1.1);
  }

  .news-list-content {
    padding: 2rem;
  }

  .news-list-content h4 {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
    line-height: 1.3;
  }

  .news-list-content h4 a {
    color: var(--text-dark);
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .news-list-content h4 a:hover {
    color: var(--vetas-primary);
  }

  .news-date {
    color: var(--text-light);
    font-size: 0.9rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .news-date i {
    color: var(--vetas-primary);
  }

  .news-excerpt {
    color: var(--text-dark);
    line-height: 1.6;
    font-size: 1rem;
    margin-bottom: 1rem;
  }

  .btn-read-news {
    background: linear-gradient(135deg, var(--vetas-primary) 0%, var(--vetas-dark) 100%);
    color: white;
    border: none;
    padding: 0.6rem 1.5rem;
    border-radius: 50px;
    font-weight: 600;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
    font-size: 0.95rem;
  }

  .btn-read-news:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(114, 191, 68, 0.4);
    color: white;
    text-decoration: none;
  }

  .banner-section {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 2rem;
    margin: 3rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  }

  .banner-section .row > div {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .banner-item {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
  }

  .banner-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 16px rgba(114, 191, 68, 0.2);
  }

  .banner-item img {
    width: 100%;
    display: block;
  }

  .pagination {
    margin: 3rem 0;
    gap: 0.5rem;
  }

  .pagination .page-item .page-link {
    border-radius: 4px;
    border: 1px solid #dee2e6;
    color: var(--text-dark);
    font-weight: 500;
    padding: 0.5rem 0.75rem;
    transition: all 0.3s ease;
    min-width: 40px;
    text-align: center;
  }

  .pagination .page-item .page-link:hover {
    background: var(--vetas-primary);
    border-color: var(--vetas-primary);
    color: white;
  }

  .pagination .page-item.active .page-link {
    background: var(--vetas-primary);
    border-color: var(--vetas-primary);
    color: white;
  }

  .pagination .page-item.disabled .page-link {
    color: var(--text-light);
    pointer-events: none;
    background-color: transparent;
    border-color: transparent;
  }

  @media (max-width: 768px) {
    .news-list-content {
      padding: 1.5rem;
    }

    .news-list-content h4 {
      font-size: 1.25rem;
    }

    .banner-section {
      padding: 1rem;
    }
  }
</style>

<main role="main">
<div class="container mt-4">
  <div class="row mb-4">
    <div class="col-md-12 text-center">
      <h1 class="display-4">$titulo_pagina</h1>
      <p class="lead text-muted">$subtitulo_pagina</p>
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
            <div class="news-list-card">
              <div class="row g-0">
                <div class="col-md-4">
                  <div class="news-list-image">
                    <img src="$fot" alt="$noticias->{$t}">
                  </div>
                </div>
                <div class="col-md-8">
                  <div class="news-list-content">
                    <h4><a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">$noticias->{$t}</a></h4>
                    <div class="news-date">
                      <i class="fa fa-calendar"></i> $noticias->{FECHANOT}
                    </div>
                    <p class="news-excerpt">$noticias->{$c}</p>
                    <a class="btn-read-news" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">
                      $leer_noticia <i class="fa fa-arrow-right"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
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
            <div class="news-list-card">
              <div class="row g-0">
                <div class="col-md-4">
                  <div class="news-list-image">
                    <img src="$fot" alt="$noticias->{$t}">
                  </div>
                </div>
                <div class="col-md-8">
                  <div class="news-list-content">
                    <h4><a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">$noticias->{$t}</a></h4>
                    <div class="news-date">
                      <i class="fa fa-calendar"></i> $noticias->{FECHANOT}
                    </div>
                    <p class="news-excerpt">$noticias->{$c}</p>
                    <a class="btn-read-news" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">
                      $leer_noticia <i class="fa fa-arrow-right"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
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
            <div class="news-list-card">
              <div class="row g-0">
                <div class="col-md-4">
                  <div class="news-list-image">
                    <img src="$fot" alt="$noticias->{$t}">
                  </div>
                </div>
                <div class="col-md-8">
                  <div class="news-list-content">
                    <h4><a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">$noticias->{$t}</a></h4>
                    <div class="news-date">
                      <i class="fa fa-calendar"></i> $noticias->{FECHANOT}
                    </div>
                    <p class="news-excerpt">$noticias->{$c}</p>
                    <a class="btn-read-news" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">
                      $leer_noticia <i class="fa fa-arrow-right"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
        );
        }
      }
&renglonbanner;


$proximo=$id+9;
$anterior=$id-9;
$anterior=0 if ($anterior<0);

print <<EOFHTML;
      <!-- Pagination -->
      <div class="row mt-5 mb-4">
        <div class="col-md-12">
          <ul class="pagination justify-content-center">
            <li class="page-item">
              <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=$anterior" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
EOFHTML

use POSIX qw(ceil);
$stm = $dbh->prepare("select count(ID) as cont from NOTAS where PUBLICADA=0 and ESPECIAL=0 and NOESP=0");
$stm->execute();
$noticias=$stm->fetchrow_hashref;
$total_noticias = $noticias->{cont};
$total_paginas = ceil($total_noticias / 9);

# Calcular página actual
$pagina_actual = int($id / 9);

# Definir rango de páginas a mostrar (mostrar 9 páginas: 4 antes, actual, 4 después)
$rango = 4;
$inicio = $pagina_actual - $rango;
$inicio = 0 if $inicio < 0;
$fin = $pagina_actual + $rango;
$fin = $total_paginas - 1 if $fin >= $total_paginas;

# Mostrar "..." al inicio si hay páginas antes del rango
if ($inicio > 0) {
  print qq(
            <li class="page-item">
              <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=0">1</a>
            </li>
  );
  if ($inicio > 1) {
    print qq(
            <li class="page-item disabled">
              <span class="page-link">...</span>
            </li>
    );
  }
}

# Mostrar páginas en el rango
for ($i=$inicio; $i<=$fin; $i++) { 
  $a=$i+1;
  $go=$i*9;
  $active_class = ($go == $id) ? "active" : "";
print qq(
            <li class="page-item $active_class">
              <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=$go">$a</a>
            </li>
        );
}

# Mostrar "..." al final si hay páginas después del rango
if ($fin < $total_paginas - 1) {
  if ($fin < $total_paginas - 2) {
    print qq(
            <li class="page-item disabled">
              <span class="page-link">...</span>
            </li>
    );
  }
  $ultima_pag = ($total_paginas - 1) * 9;
  print qq(
            <li class="page-item">
              <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=$ultima_pag">$total_paginas</a>
            </li>
  );
}

print <<EOFHTML;
            <li class="page-item">
              <a class="page-link" href="listadonoticias.cgi?i=$idioma&id=$proximo" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </div>
      </div>

    </div>
</main>

EOFHTML

open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}



 sub renglonbanner{
print qq(
<div class="banner-section">
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div class="banner-item">);
      &banne(174);
    print qq(</div>
        <div class="banner-item">);
      &banne(174);
    print qq(</div>
      </div>
      <div class="col-md-4">
        <div class="banner-item">);
      &banne(174);
    print qq(</div>
        <div class="banner-item">);
      &banne(174);
    print qq(</div>
      </div>
      <div class="col-md-4">
        <div class="banner-item">);
      &banne(174);
    print qq(</div>
        <div class="banner-item">);
      &banne(174);
    print qq(</div>
      </div>
    </div>
  </div>
</div>);
} 


  sub banne{
($ancho,$alpe)=@_;
$stm13 = $dbh->prepare("select *, B.ID as IDBAN from BANNERS as B, USUARIOS as U  where B.ANCHO=$ancho and B.ACTIVO=1 and B.CLIENTE=U.ID and B.VETAS=1 and (U.ACTIVO_REVISTA!=0 or U.REVISTA='$config->{MUEBLE}' or U.ACTIVO_GUIA!=0 or U.ACTIVO=1) order by  B.EXPO, B.ORDEN,  RAND() limit 0,6");
$stm13->execute();
    $banners=$stm13->fetchrow_hashref;
print qq(<a href="empresa.cgi?cliente=$banners->{CLIENTE}&i=$idioma&c=BANNERS_CLICKS"><img src="../banners/$banners->{ARCHIVO}" alt="$banners->{EMPRESA}"></a> ) if ($banners->{ENLACE} eq "");
print qq(<a href="$banners->{ENLACE}"><img src="../banners/$banners->{ARCHIVO}" alt="$banners->{EMPRESA}"></a> ) if ($banners->{ENLACE} ne "");
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