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

<style>
  :root {
    --vetas-primary: #72bf44;
    --vetas-dark: #2c5f2d;
    --vetas-light: #e8f5e0;
  }

  .magazine-viewer {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 16px;
    padding: 2rem;
    margin-top: 2rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
  }

  .magazine-header {
    text-align: center;
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 3px solid var(--vetas-primary);
  }

  .magazine-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--vetas-dark);
    margin-bottom: 0.5rem;
  }

  .page-counter {
    display: inline-block;
    background: linear-gradient(135deg, var(--vetas-primary) 0%, var(--vetas-dark) 100%);
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.1rem;
  }

  .magazine-content {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin: 2rem 0;
  }

  .nav-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 1.5rem 0;
    gap: 1rem;
  }

  .nav-btn {
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
    box-shadow: 0 4px 12px rgba(114, 191, 68, 0.3);
  }

  .nav-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(114, 191, 68, 0.4);
    color: white;
    text-decoration: none;
  }

  .nav-btn:active {
    transform: translateY(0);
  }

  .nav-btn i {
    font-size: 1.2rem;
  }

  .thumbnail-nav {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    position: relative;
  }

  .pagination-modern {
    display: flex;
    flex-wrap: nowrap;
    gap: 0.75rem;
    justify-content: flex-start;
    align-items: center;
    padding: 0.5rem 0;
    margin: 0;
    list-style: none;
    overflow-x: auto;
    overflow-y: hidden;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: thin;
    scrollbar-color: var(--vetas-primary) #f1f1f1;
  }

  /* Estilo del scrollbar para Chrome/Safari */
  .pagination-modern::-webkit-scrollbar {
    height: 8px;
  }

  .pagination-modern::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
  }

  .pagination-modern::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, var(--vetas-primary) 0%, var(--vetas-dark) 100%);
    border-radius: 10px;
  }

  .pagination-modern::-webkit-scrollbar-thumb:hover {
    background: var(--vetas-dark);
  }

  .pagination-modern .page-item {
    margin: 0;
    flex-shrink: 0;
  }

  .pagination-modern .page-link {
    border: 2px solid #e9ecef;
    border-radius: 8px;
    padding: 0.25rem;
    transition: all 0.3s ease;
    background: white;
    overflow: hidden;
    display: block;
  }

  .pagination-modern .page-link img {
    width: 70px;
    height: 95px;
    object-fit: cover;
    display: block;
    border-radius: 4px;
    transition: all 0.3s ease;
  }

  .pagination-modern .page-link:hover {
    border-color: var(--vetas-primary);
    transform: scale(1.08);
    box-shadow: 0 4px 12px rgba(114, 191, 68, 0.3);
    z-index: 10;
  }

  .pagination-modern .page-item.active .page-link {
    border-color: var(--vetas-primary);
    border-width: 3px;
    box-shadow: 0 0 0 3px rgba(114, 191, 68, 0.2);
  }

  .pagination-modern .page-item.active .page-link img {
    transform: scale(1.05);
  }

  .pagination-arrow {
    background: linear-gradient(135deg, var(--vetas-primary) 0%, var(--vetas-dark) 100%);
    border: none !important;
    color: white !important;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50% !important;
    padding: 0 !important;
  }

  .pagination-arrow:hover {
    transform: scale(1.1);
    box-shadow: 0 4px 12px rgba(114, 191, 68, 0.4);
  }

  .magazine-image-container {
    text-align: center;
    position: relative;
    background: #f8f9fa;
    border-radius: 8px;
    padding: 1rem;
  }

  .scroll-hint {
    text-align: center;
    color: #6c757d;
    font-size: 0.875rem;
    margin-top: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }

  .scroll-hint i {
    animation: slideLeft 1.5s ease-in-out infinite;
  }

  @keyframes slideLeft {
    0%, 100% { transform: translateX(0); }
    50% { transform: translateX(-5px); }
  }

  .thumbnail-scroll-wrapper {
    position: relative;
    padding: 0 50px;
  }

  .thumbnail-scroll-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: linear-gradient(135deg, var(--vetas-primary) 0%, var(--vetas-dark) 100%);
    border: none;
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }

  .thumbnail-scroll-btn:hover {
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 6px 20px rgba(114, 191, 68, 0.4);
  }

  .thumbnail-scroll-btn:active {
    transform: translateY(-50%) scale(0.95);
  }

  .thumbnail-scroll-btn.left {
    left: 0;
  }

  .thumbnail-scroll-btn.right {
    right: 0;
  }

  .thumbnail-scroll-btn:disabled {
    opacity: 0.3;
    cursor: not-allowed;
  }

  .thumbnail-scroll-btn:disabled:hover {
    transform: translateY(-50%) scale(1);
  }

  @media (max-width: 768px) {
    .thumbnail-scroll-wrapper {
      padding: 0;
    }

    .thumbnail-scroll-btn {
      display: none;
    }
  }

  @media (max-width: 768px) {
    .magazine-viewer {
      padding: 1rem;
    }

    .magazine-title {
      font-size: 1.5rem;
    }

    .nav-buttons {
      flex-direction: column;
    }

    .nav-btn {
      width: 100%;
      justify-content: center;
    }

    .pagination-modern .page-link img {
      width: 55px;
      height: 75px;
    }

    .thumbnail-nav {
      padding: 1rem;
    }
  }
</style>

<main role="main">
  <div class="container">
    <div class="magazine-viewer">
      
      <!-- Header -->
      <div class="magazine-header">
        <h1 class="magazine-title">$txtrevi N&deg;$rev</h1>
        <span class="page-counter">$pagina / $paginastotal</span>
      </div>

      <!-- Navigation Buttons Top -->
      <div class="nav-buttons">
        <a class="nav-btn" href="$paganterior">
          <i class="fa fa-angle-left"></i> $pagAnteriorTxt
        </a>
        <a class="nav-btn" href="$pagproxima">
          $pagProximaTxt <i class="fa fa-angle-right"></i>
        </a>
      </div>

      <!-- Thumbnail Navigation -->
      <div class="thumbnail-nav">
        <div class="scroll-hint">
          <i class="fa fa-arrows-h"></i> Desliza para ver m&aacute;s p&aacute;ginas
        </div>
        <div class="thumbnail-scroll-wrapper">
          <button class="thumbnail-scroll-btn left" id="scrollLeft" onclick="scrollThumbnails('left')">
            <i class="fa fa-chevron-left"></i>
          </button>
          <nav aria-label="Page navigation">
            <ul class="pagination-modern" id="thumbnailContainer">
              <li class="page-item">
                <a class="page-link pagination-arrow" href="$paganterior" tabindex="-1">
                  <i class="fa fa-angle-left"></i>
                </a>
              </li>

EOFHTML

for (my $i=1; $i <= $paginastotal; $i++) {
  $pagnum="maga.cgi?revista=".$rev."\&pag=".$i."\&paginas=".$paginastotal."&i=".$idioma;
  $ch="./revista/$rev/".$i."c.jpg";
  $active="";
  $active=" active" if($pagina==$i);
print qq(            <li class="page-item$active"><a class="page-link" href="$pagnum"><img src="$ch" alt="P&aacute;gina $i"></a></li>\n);
}


$pagProximaTxt="Proxima";
$pagProximaTxt="Next" if ($idioma eq "en");
$pagProximaTxt="Proxima" if ($idioma eq "br");

$pagAnteriorTxt="Anterior";
$pagAnteriorTxt="Previous" if ($idioma eq "en");
$pagAnteriorTxt="Anterior" if ($idioma eq "br");



print <<EOFHTML;  
            <li class="page-item">
              <a class="page-link pagination-arrow" href="$pagproxima">
                <i class="fa fa-angle-right"></i>
              </a>
            </li>
          </ul>
        </nav>
        <button class="thumbnail-scroll-btn right" id="scrollRight" onclick="scrollThumbnails('right')">
          <i class="fa fa-chevron-right"></i>
        </button>
      </div>
      </div>

      <!-- Magazine Content -->
      <div class="magazine-content">
        <div class="magazine-image-container">
          <script>
          // Thumbnail scroll functionality
          function scrollThumbnails(direction, position) {
            const containerId = position === 'bottom' ? 'thumbnailContainerBottom' : 'thumbnailContainer';
            const container = document.getElementById(containerId);
            const scrollAmount = 300; // pixels to scroll
            
            if (direction === 'left') {
              container.scrollBy({
                left: -scrollAmount,
                behavior: 'smooth'
              });
            } else {
              container.scrollBy({
                left: scrollAmount,
                behavior: 'smooth'
              });
            }
            
            // Update button states after scroll
            setTimeout(() => updateScrollButtons(position), 300);
          }
          
          function updateScrollButtons(position) {
            if (position === 'bottom') {
              const container = document.getElementById('thumbnailContainerBottom');
              const leftBtn = document.getElementById('scrollLeftBottom');
              const rightBtn = document.getElementById('scrollRightBottom');
              
              if (!container || !leftBtn || !rightBtn) return;
              
              // Disable left button if at start
              if (container.scrollLeft <= 0) {
                leftBtn.disabled = true;
              } else {
                leftBtn.disabled = false;
              }
              
              // Disable right button if at end
              const maxScroll = container.scrollWidth - container.clientWidth;
              if (container.scrollLeft >= maxScroll - 5) { // -5 for tolerance
                rightBtn.disabled = true;
              } else {
                rightBtn.disabled = false;
              }
            } else {
              const container = document.getElementById('thumbnailContainer');
              const leftBtn = document.getElementById('scrollLeft');
              const rightBtn = document.getElementById('scrollRight');
              
              if (!container || !leftBtn || !rightBtn) return;
              
              // Disable left button if at start
              if (container.scrollLeft <= 0) {
                leftBtn.disabled = true;
              } else {
                leftBtn.disabled = false;
              }
              
              // Disable right button if at end
              const maxScroll = container.scrollWidth - container.clientWidth;
              if (container.scrollLeft >= maxScroll - 5) { // -5 for tolerance
                rightBtn.disabled = true;
              } else {
                rightBtn.disabled = false;
              }
            }
          }
          
          // Initialize on load
          document.addEventListener('DOMContentLoaded', function() {
            updateScrollButtons('top');
            updateScrollButtons('bottom');
            
            // Update buttons on scroll for both containers
            const containerTop = document.getElementById('thumbnailContainer');
            if (containerTop) {
              containerTop.addEventListener('scroll', () => updateScrollButtons('top'));
            }
            
            const containerBottom = document.getElementById('thumbnailContainerBottom');
            if (containerBottom) {
              containerBottom.addEventListener('scroll', () => updateScrollButtons('bottom'));
            }
          });
          
          // Image map resize functionality
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

      <!-- Navigation Buttons Bottom -->
      <div class="nav-buttons">
        <a class="nav-btn" href="$paganterior">
          <i class="fa fa-angle-left"></i> $pagAnteriorTxt
        </a>
        <a class="nav-btn" href="$pagproxima">
          $pagProximaTxt <i class="fa fa-angle-right"></i>
        </a>
      </div>

      <!-- Numeric Page Navigation -->
      <div class="thumbnail-nav">
        <div class="thumbnail-scroll-wrapper">
          <button class="thumbnail-scroll-btn left" id="scrollLeftBottom" onclick="scrollThumbnails('left', 'bottom')">
            <i class="fa fa-chevron-left"></i>
          </button>
          <nav aria-label="Page navigation">
            <ul class="pagination-modern" id="thumbnailContainerBottom">
              <li class="page-item">
                <a class="page-link pagination-arrow" href="$paganterior" tabindex="-1">
                  <i class="fa fa-angle-left"></i>
                </a>
              </li>

EOFHTML

for (my $i=1; $i <= $paginastotal; $i++) {
  $pagnum="maga.cgi?revista=".$rev."\&pag=".$i."\&paginas=".$paginastotal."&i=".$idioma;
  $active="";
  $active=" active" if($pagina==$i);
  print qq(            <li class="page-item$active"><a class="page-link" href="$pagnum" style="padding: 0.5rem 0.75rem; min-width: 40px; text-align: center; font-weight: 600;">$i</a></li>\n);
}


    


print <<EOFHTML;  
            <li class="page-item">
              <a class="page-link pagination-arrow" href="$pagproxima">
                <i class="fa fa-angle-right"></i>
              </a>
            </li>
          </ul>
        </nav>
        <button class="thumbnail-scroll-btn right" id="scrollRightBottom" onclick="scrollThumbnails('right', 'bottom')">
          <i class="fa fa-chevron-right"></i>
        </button>
      </div>
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

$dbh->disconnect;