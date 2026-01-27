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
<style>
  :root {
    --vetas-primary: #72bf44;
    --vetas-dark: #2c5f2d;
    --vetas-light: #e8f5e0;
    --text-dark: #2c3e50;
    --text-light: #6c757d;
  }

  .news-article {
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    padding: 2rem;
    margin-bottom: 2rem;
    transition: all 0.3s ease;
  }

  .news-article:hover {
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    transform: translateY(-2px);
  }

  .news-header-section {
    margin-bottom: 2rem;
  }

  .news-header {
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
  }

  .news-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 1rem;
    line-height: 1.2;
  }

  .news-meta {
    display: flex;
    align-items: center;
    gap: 1rem;
    color: var(--text-light);
    font-size: 0.95rem;
    flex-wrap: wrap;
  }

  .news-meta i {
    color: var(--vetas-primary);
  }

  .news-image-featured {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    margin-bottom: 0;
    width: 100%;
    aspect-ratio: 1 / 1;
  }

  .news-image-featured img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
  }

  .news-image-featured:hover img {
    transform: scale(1.05);
  }

  .news-company-logo {
    text-align: left;
    padding: 1rem;
    background: linear-gradient(135deg, #f8f9fa 0%, var(--vetas-light) 100%);
    border-radius: 12px;
    margin-bottom: 1rem;
  }

  .news-company-logo img {
    max-width: 150px;
    height: auto;
  }

  .news-lead {
    font-size: 1.25rem;
    font-weight: 500;
    color: var(--text-dark);
    line-height: 1.6;
    margin-bottom: 1.5rem;
    padding: 1.5rem;
    background: var(--vetas-light);
    border-left: 4px solid var(--vetas-primary);
    border-radius: 8px;
  }

  .news-content {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--text-dark);
  }

  .news-content p {
    margin-bottom: 1.5rem;
  }

  .news-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }

  .news-gallery-item {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    aspect-ratio: 1 / 1;
  }

  .news-gallery-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 24px rgba(114, 191, 68, 0.3);
  }

  .news-gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .share-section {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
    margin-top: 1rem;
  }

  .related-news-section {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 2px solid #e9ecef;
  }

  .section-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 3px solid var(--vetas-primary);
    display: inline-block;
  }

  .news-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
  }

  .news-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(114, 191, 68, 0.2);
  }

  .news-card-img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
  }

  .news-card-body {
    padding: 1.5rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }

  .news-card-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-dark);
    margin-bottom: 1rem;
    line-height: 1.4;
  }

  .news-card-text {
    color: var(--text-light);
    margin-bottom: 1.5rem;
    flex-grow: 1;
    font-size: 0.95rem;
    line-height: 1.6;
  }

  .btn-read-more {
    background: linear-gradient(135deg, var(--vetas-primary) 0%, var(--vetas-dark) 100%);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 50px;
    font-weight: 600;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
    align-self: flex-start;
  }

  .btn-read-more:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(114, 191, 68, 0.4);
    color: white;
    text-decoration: none;
  }

  .sidebar-banners {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  }

  .banner-item {
    margin-bottom: 1.5rem;
    text-align: center;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
  }

  .banner-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 16px rgba(114, 191, 68, 0.2);
  }

  .banner-item:last-child {
    margin-bottom: 0;
  }

  .banner-item img {
    width: 100%;
    height: auto;
    display: block;
  }

  @media (max-width: 768px) {
    .news-title {
      font-size: 1.5rem;
    }

    .news-article {
      padding: 1.5rem;
    }

    .news-header-section .row {
      flex-direction: column;
    }

    .news-image-featured {
      margin-bottom: 1.5rem;
      max-width: 300px;
      margin-left: auto;
      margin-right: auto;
    }

    .news-company-logo {
      text-align: center;
    }

    .news-lead {
      font-size: 1.1rem;
      padding: 1rem;
    }

    .news-content {
      font-size: 1rem;
    }

    .news-gallery {
      grid-template-columns: 1fr;
    }
  }
</style>

 <main role="main">

     <div class="container">
      <div class="row">
    <div class="col-md-8">
       <article class="news-article">
         <!-- Meta Tags -->
         <meta property="og:url" content="https://www.vetas.com/noticias.cgi?i=es&noticia=$noticias->{ID}" />
         <meta property="og:type" content="website" />
         <meta property="og:title" content="$noticias->{$t}" />
         <meta property="og:description" content="$noticias->{$c}" />
         <meta property="og:image" content="$fot" />
         <title>$noticias->{$t}</title>
         
         <!-- Article Header with Image -->
         <div class="news-header-section">
           <div class="row align-items-center">
             <div class="col-md-4">
               <div class="news-image-featured">
                 <img src="$fot" alt="$noticias->{$t}" class="img-fluid">
               </div>
             </div>
             <div class="col-md-8">
EOFHTML
print "<div class=\"news-company-logo\"><a href=\"https://www.vetas.com/empresa.cgi?cliente=$noticias->{ID_CLIENTE}&i=$idioma&c=LOGO_CLICKS\"><img src=\"https://www.vetas.com/clientes/logos/$noticias->{ID_CLIENTE}.jpg\" alt=\"Logo empresa\"></a></div>" if ($noticias->{ID_CLIENTE}ne 0);

print <<EOFHTML;   
               <div class="news-header">
                 <h1 class="news-title">$noticias->{$t}</h1>
                 <div class="news-meta">
                   <span><i class="fa fa-calendar"></i> $noticias->{FECHANOT}</span>
                   <span><i class="fa fa-newspaper-o"></i> $noticias->{FUENTE}</span>
                 </div>
               </div>
             </div>
           </div>
         </div>

         <!-- Social Share -->
         <div class="share-section">
           <div id="fb-root"></div>
           <script>(function(d, s, id) {
             var js, fjs = d.getElementsByTagName(s)[0];
             if (d.getElementById(id)) return;
             js = d.createElement(s); js.id = id;
             js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
             fjs.parentNode.insertBefore(js, fjs);
           }(document, 'script', 'facebook-jssdk'));</script>
           
           <div class="fb-share-button" 
             data-href="https://www.vetas.com/noticias.cgi?i=es&noticia=$noticias->{ID}" 
             data-layout="button" data-size="small">
             <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https://www.vetas.com/noticias.cgi?i=es&noticia=$noticias->{ID};src=sdkpreparse" class="fb-xfbml-parse-ignore">Compartir</a>
           </div>
         </div>
         
         <!-- Lead/Summary -->
         <div class="news-lead">
           $noticias->{$c}
         </div>
         
         <!-- Article Content -->
         <div class="news-content">
           $noticias->{$n}
         </div>
EOFHTML

 print <<EOFHTML;   
         
         <!-- Photo Gallery -->
         <div class="news-gallery">
EOFHTML

        while ($foto=$stm3->fetchrow_hashref)
        {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
             
          print qq(           <div class="news-gallery-item"><img src="$fot" alt="Imagen noticia"></div>\n);
        }
        
print qq(         </div>\n);
print qq(       </article>\n);
print qq(       <br>\n);
 banne2(1200, $dbh, $revi, $idioma);

 print <<EOFHTML;   
       
       <!-- Related News Section -->
       <div class="related-news-section">
         <h3 class="section-title">$notitit</h3>
         <div class="row">
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
          <div class="col-md-4 mb-4">
            <div class="news-card">
              <img class="news-card-img" src="$fot" alt="$noticias->{$t}">
              <div class="news-card-body">
                <h4 class="news-card-title">$noticias->{$t}</h4>
                <p class="news-card-text">$noticias->{$c}</p>
                <a class="btn-read-more" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}&o=1">
                  $leer <i class="fa fa-arrow-right"></i>
                </a>
              </div>
            </div>
          </div>
          );
      }





print <<EOFHTML;        
         </div>
       </div>
     </div>
             
     <!-- Sidebar -->
     <div class="col-md-4">
       <div class="sidebar-banners">
EOFHTML

for (my $i=0; $i <= 10; $i++) {
  print qq(         <div class="banner-item">);
  banne(174, $dbh, $revi, $idioma);
  print qq(         </div>\n);
}


print <<EOFHTML;   
       </div>
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
