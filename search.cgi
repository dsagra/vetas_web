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

  $volver="$envi";
  $volver2="$envi";
$idioma="es";
$idioma=$formulario{i} if ($formulario{i} eq "br" or $formulario{i} eq "en" );
$MENU="menu.html";
$MENU="menu_en.html" if ($idioma eq "en") ;
$MENU="menu_br.html" if ($idioma eq "br") ;

# Preservar el parámetro de búsqueda en los enlaces de idioma
if ($formulario{producto}) {
    # Si volver ya tiene el parámetro producto, solo cambiar el idioma
    # Si no lo tiene, agregarlo
    if ($volver !~ m/producto=/) {
        if ($volver =~ m/\?/) {
            $volver .= "&producto=$formulario{producto}";
            $volver2 .= "&producto=$formulario{producto}";
        } else {
            $volver .= "?producto=$formulario{producto}";
            $volver2 .= "?producto=$formulario{producto}";
        }
    }
}

if ($idioma eq "es")
  {

  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  $rub="RUBRO_ES";

  $noticias="Noticias";
  $sp="SP";
  $revivetas="Revista VETAS";
  $copete="SP_COPETE";
  $desc="DESCRIPT";
  $fdesc="fotodesc";
  }
if ($idioma eq "en")
  {

  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  $rub="RUBRO_EN";
  $noticias="News";
  $sp="EN";
  $revivetas="VETAS Magazine";
  $copete="EN_COPETE";
  $desc="DESCRIPT_EN";
  $fdesc="fotodesc_en";
  }
if ($idioma eq "br")
  {
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  $rub="RUBRO_BR";
  $noticias="Noticias";
  $sp="BR";
  $revivetas="Revista VETAS";
  $copete="BR_COPETE";
  $desc="DESCRIPT_BR";
  $fdesc="fotodesc_br";
  }


$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);

$letra="%".$formulario{producto}."%";

$pro=$formulario{producto};

$pro=~ s/ de / /g;
$pro=~ s/ para / /g;
$pro=~ s/ en / /g;
$pro=~ s/ la / /g;
$pro=~ s/ las / /g;


$pro =~ s/s\s*$//;




@palabras = split(/[\s+]/,$pro);





#print "<b>$pro</b>";


if ( $pro =~ / /)
    {
$stm = $dbh->prepare("SELECT *, F.DESCRIPT as fotodesc, F.DESCRIPT_EN as fotodesc_en, F.DESCRIPT_BR as fotodesc_br, F.ARCHIVO as fotoarchivo,U.ID as idcliente, F.ID as fot from FOTOS as F, RUBROS_NUEVO  AS R, USUARIOS AS U where MATCH(F.BUSCADOR) AGAINST('$pro') and R.ID=F.RUBRO and F.SLIDER=0 and  F.CLIENTE=U.ID and (F.FECHAVENCE='' or F.FECHAVENCE > now())  and   (U.ACTIVO!=0 or U.ACTIVO_REVISTA!=0 or U.ACTIVO_GUIA=$revi->{GUIA}) ");

$stm2 = $dbh->prepare("SELECT *, F.DESCRIPT as fotodesc,F.DESCRIPT_EN as fotodesc_en, F.DESCRIPT_BR as fotodesc_br, F.ARCHIVO as fotoarchivo,U.ID as idcliente, F.ID as fot from FOTOS as F, RUBROS_NUEVO  AS R, USUARIOS AS U where MATCH(U.BUSCADOR) AGAINST('$pro') and R.ID=F.RUBRO and (F.FECHAVENCE='' or F.FECHAVENCE > now()) and F.CLIENTE=U.ID and (U.ACTIVO!=0 or U.ACTIVO_REVISTA!=0 or U.ACTIVO_GUIA=$revi->{GUIA}) ");


#     $stm = $dbh->prepare("select *, F.DESCRIPT as fotodesc, F.ARCHIVO as fotoarchivo,U.ID as idcliente, F.ID as fot ,MATCH (U.BUSCADOR) AGAINST ('$pro') as puntuacion from FOTOS as F, RUBROS AS R , USUARIOS AS U where  MATCH (U.BUSCADOR) AGAINST ('$pro')  and F.RUBRO=R.ID and F.REVISTA=0 and F.CLIENTE=U.ID and (U.ACTIVO_REVISTA!=0 or U.ACTIVO_GUIA!=0) order by puntuacion desc");
#    $stm = $dbh->prepare("SELECT *, MATCH (BUSCADOR) AGAINST ('$formulario{producto}') as puntuacion FROM  USUARIOS WHERE (ACTIVO_REVISTA!=0 or ACTIVO_GUIA!=0 or ACTIVO=1) and MATCH (BUSCADOR) AGAINST ('$formulario{producto}') order by puntuacion desc"); 
    }
  else
    {

$stm = $dbh->prepare("SELECT *, F.DESCRIPT as fotodesc, F.DESCRIPT_EN as fotodesc_en, F.DESCRIPT_BR as fotodesc_br,F.ARCHIVO as fotoarchivo,U.ID as idcliente, F.ID as fot ,MATCH (F.BUSCADOR) AGAINST ('$pro') as puntuacion from FOTOS as F, RUBROS_NUEVO  AS R, USUARIOS AS U where F.BUSCADOR like '$letra' and R.ID=F.RUBRO and (F.FECHAVENCE='' or F.FECHAVENCE > now()) and F.SLIDER=0 and F.CLIENTE=U.ID and (U.ACTIVO!=0 or U.ACTIVO_REVISTA!=0 or U.ACTIVO_GUIA=$revi->{GUIA}) order by puntuacion desc" );

$stm2 = $dbh->prepare("SELECT *, F.DESCRIPT as fotodesc,F.DESCRIPT_EN as fotodesc_en, F.DESCRIPT_BR as fotodesc_br, F.ARCHIVO as fotoarchivo,U.ID as idcliente, F.ID as fot ,MATCH (U.BUSCADOR) AGAINST ('$pro') as puntuacion from FOTOS as F, RUBROS_NUEVO  AS R, USUARIOS AS U where U.BUSCADOR like '$letra' and R.ID=F.RUBRO and (F.FECHAVENCE='' or F.FECHAVENCE > now()) and F.CLIENTE=U.ID and (U.ACTIVO!=0 or U.ACTIVO_REVISTA!=0 or U.ACTIVO_GUIA=$revi->{GUIA}) order by puntuacion desc" );



#     $stm = $dbh->prepare("select *, F.DESCRIPT as fotodesc, F.ARCHIVO as fotoarchivo,U.ID as idcliente, F.ID as fot ,MATCH (U.BUSCADOR) AGAINST ('$pro') as puntuacion from FOTOS as F, RUBROS AS R , USUARIOS AS U where MATCH (U.BUSCADOR) AGAINST ('$pro')  and F.RUBRO=R.ID and F.REVISTA=0 and F.CLIENTE=U.ID and (U.ACTIVO_REVISTA!=0 or U.ACTIVO_GUIA!=0)  order by puntuacion desc");
#     $stm = $dbh->prepare("select *, MATCH (BUSCADOR) AGAINST ('$formulario{producto}') as puntuacion from USUARIOS where BUSCADOR like '$letra' and ( ACTIVO_REVISTA !=0 or ACTIVO_GUIA!=0 or ACTIVO=1) order by puntuacion desc");
    }

  $stm->execute();


  $stm2->execute();

# Preparar textos del buscador según idioma
my $search_placeholder = "";
my $search_button = "";
my $no_results_title = "";
my $no_results_msg = "";
my $no_results_suggestions = "";
my $results_found = "";

if ($idioma eq "es") {
    $search_placeholder = "Buscar productos, empresas, noticias...";
    $search_button = "Buscar";
    $no_results_title = "No se encontraron resultados";
    $no_results_msg = "No encontramos ning&uacute;n resultado para tu b&uacute;squeda.";
    $no_results_suggestions = "<ul class='suggestions-list'>
        <li><strong>Verifica la ortograf&iacute;a</strong> de las palabras de b&uacute;squeda</li>
        <li><strong>Intenta con palabras m&aacute;s generales</strong> o sin&oacute;nimos</li>
        <li><strong>Usa menos palabras</strong> para ampliar la b&uacute;squeda</li>
        <li><strong>Navega por categor&iacute;as</strong> desde el <a href='index.cgi?i=es'>inicio</a></li>
        <li><strong>Explora la Gu&iacute;a de Proveedores</strong> en el men&uacute;</li>
    </ul>";
    $results_found = "Resultados de b&uacute;squeda para";
} elsif ($idioma eq "en") {
    $search_placeholder = "Search products, companies, news...";
    $search_button = "Search";
    $no_results_title = "No results found";
    $no_results_msg = "We couldn't find any results for your search.";
    $no_results_suggestions = "<ul class='suggestions-list'>
        <li><strong>Check the spelling</strong> of your search terms</li>
        <li><strong>Try more general words</strong> or synonyms</li>
        <li><strong>Use fewer words</strong> to broaden your search</li>
        <li><strong>Browse by categories</strong> from the <a href='index.cgi?i=en'>home page</a></li>
        <li><strong>Explore the Suppliers Guide</strong> in the menu</li>
    </ul>";
    $results_found = "Search results for";
} else {
    $search_placeholder = "Pesquisar produtos, empresas, not&iacute;cias...";
    $search_button = "Pesquisar";
    $no_results_title = "Nenhum resultado encontrado";
    $no_results_msg = "N&atilde;o encontramos nenhum resultado para sua pesquisa.";
    $no_results_suggestions = "<ul class='suggestions-list'>
        <li><strong>Verifique a ortografia</strong> das palavras de pesquisa</li>
        <li><strong>Tente palavras mais gerais</strong> ou sin&ocirc;nimos</li>
        <li><strong>Use menos palavras</strong> para ampliar a pesquisa</li>
        <li><strong>Navegue por categorias</strong> na <a href='index.cgi?i=br'>p&aacute;gina inicial</a></li>
        <li><strong>Explore o Guia de Fornecedores</strong> no menu</li>
    </ul>";
    $results_found = "Resultados da pesquisa para";
}

print <<EOFHTML;
<style>     
  :root {
    --primary-color: #72bf44;
    --primary-dark: #5fa835;
    --primary-gradient: linear-gradient(135deg, #72bf44 0%, #5fa835 100%);
    --card-shadow: 0 10px 20px rgba(0,0,0,0.05);
    --card-shadow-hover: 0 15px 30px rgba(114, 191, 68, 0.15);
    --text-dark: #2c3e50;
    --text-muted: #6c757d;
  }

  /* Search Form Styles */
  .search-form-modern {
    margin: 3rem 0;
  }

  .search-input-modern {
    border: 2px solid #e9ecef;
    border-right: none;
    padding: 1rem 1.5rem;
    font-size: 1.1rem;
    border-radius: 50px 0 0 50px !important;
    transition: all 0.3s ease;
    background: #fdfdfd;
  }

  .search-input-modern:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 0.25rem rgba(114, 191, 68, 0.1);
    background: #fff;
    outline: none;
  }

  .btn-search-modern {
    background: var(--primary-gradient);
    border: none;
    color: white;
    padding: 0 2.5rem;
    font-weight: 600;
    font-size: 1.1rem;
    border-radius: 0 50px 50px 0 !important;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .btn-search-modern:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(114, 191, 68, 0.3);
  }

  /* Result Section Headers */
  .section-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 0.5rem;
    position: relative;
    display: inline-block;
  }
  
  .section-title::after {
    content: '';
    display: block;
    width: 60px;
    height: 4px;
    background: var(--primary-color);
    margin-top: 8px;
    border-radius: 2px;
  }

  .section-header-container {
      margin-top: 4rem;
      margin-bottom: 2rem;
  }

  /* Product Cards */
  .result-card {
    border: none;
    border-radius: 16px;
    overflow: hidden;
    background: #fff;
    box-shadow: var(--card-shadow);
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
  }

  .result-card:hover {
    transform: translateY(-8px);
    box-shadow: var(--card-shadow-hover);
  }

  .result-card-img-wrapper {
    position: relative;
    padding-top: 66%; /* 3:2 Aspect Ratio */
    overflow: hidden;
    background: #f8f9fa;
  }

  .result-card-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain; /* Maintain logo aspect correctly */
    padding: 1rem;
    transition: transform 0.5s ease;
  }
  
  .result-card:hover .result-card-img {
    transform: scale(1.05);
  }

  .result-card-body {
    padding: 1.5rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }

  .result-card-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 0.75rem;
    line-height: 1.4;
    text-decoration: none !important;
  }
  
  .result-card-title a {
      color: inherit;
      text-decoration: none;
  }
  
  .result-card-title a:hover {
      color: var(--primary-color);
  }

  .result-card-desc {
    font-size: 0.95rem;
    color: var(--text-muted);
    line-height: 1.6;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-bottom: 1.5rem;
  }
  
  .result-card-footer {
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
  }
  
  .company-logo-small {
      height: 30px;
      width: auto;
      max-width: 80px;
      object-fit: contain;
  }

  .btn-view-more {
      color: var(--primary-color);
      font-weight: 600;
      font-size: 0.9rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: gap 0.2s ease;
  }
  
  .btn-view-more:hover {
      gap: 8px;
      text-decoration: none;
      color: var(--primary-dark);
  }

  /* News Cards */
  .news-card {
      border: none;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: var(--card-shadow);
      transition: all 0.3s ease;
      height: 100%;
      background: white;
  }
  
  .news-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--card-shadow-hover);
  }
  
  .news-img-wrapper {
      height: 200px;
      overflow: hidden;
      position: relative;
  }
  
  .news-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
  }
  
  .news-card:hover .news-img {
      transform: scale(1.05);
  }
  
  .news-card-body {
      padding: 1.25rem;
  }
  
  .news-date {
      font-size: 0.8rem;
      color: #999;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.5rem;
      display: block;
      font-weight: 600;
  }
  
  .news-title {
      font-size: 1.1rem;
      font-weight: 700;
      line-height: 1.4;
      margin-bottom: 0.75rem;
  }
  
  .news-title a {
      color: var(--text-dark);
      text-decoration: none;
      transition: color 0.2s;
  }
  
  .news-title a:hover {
      color: var(--primary-color);
  }

  /* Magazine Cards */
  .magazine-card {
      border: none;
      background: transparent;
      transition: transform 0.3s ease;
  }
  
  .magazine-card:hover {
      transform: translateY(-5px);
  }
  
  .magazine-cover-wrapper {
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 8px 20px rgba(0,0,0,0.15);
      margin-bottom: 1rem;
      position: relative;
      aspect-ratio: 1/1.4; /* Magazine ratio */
  }
  
  .magazine-cover {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: filter 0.3s;
  }
  
  .magazine-card:hover .magazine-cover {
      filter: brightness(1.05);
  }
  
  .magazine-info h5 a {
      color: var(--text-dark);
      font-weight: 700;
      text-decoration: none;
  }
  
  .magazine-info h5 a:hover {
      color: var(--primary-color);
  }
  
  .magazine-number {
      color: var(--primary-color);
      font-weight: 600;
      font-size: 0.9rem;
      margin-bottom: 0.25rem;
  }

  /* No results */
  .no-results-container {
    text-align: center;
    padding: 4rem 2rem;
    background: #fff;
    border-radius: 20px;
    box-shadow: var(--card-shadow);
    max-width: 800px;
    margin: 2rem auto;
  }

  /* Media Queries */
  @media (max-width: 768px) {
    .search-input-modern {
      font-size: 1rem;
      padding: 0.8rem 1rem;
    }

    .btn-search-modern {
      padding: 0.8rem 1.5rem;
    }
    
    .section-title {
        font-size: 1.5rem;
    }
  }
</style>

<main style="background-color: #fcfcfc; min-height: 80vh; padding-bottom: 4rem;">
<div class="container">
  <!-- Search Section -->
  <div class="row justify-content-center">
    <div class="col-lg-8">
      <form action="search.cgi" method="get" class="search-form-modern">
        <input type="hidden" name="i" value="$idioma">
        <div class="input-group">
          <input type="text" name="producto" class="form-control search-input-modern" placeholder="$search_placeholder" value="$formulario{producto}" aria-label="$search_button" required>
          <div class="input-group-append">
            <button class="btn btn-search-modern" type="submit">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
              </svg>
              <span class="d-none d-sm-inline">$search_button</span>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>

EOFHTML

# Primero contar todos los resultados
my $total_results = 0;

# DEBUG: Mostrar información de búsqueda
print "<!-- DEBUG INFO:\n";
print "Palabra original: $formulario{producto}\n";
print "Palabra procesada: $pro\n";
print "Palabras array: " . join(", ", @palabras) . "\n";
print "Idioma: $idioma\n";
print "-->\n";

# Contar resultados de productos/empresas
$stm->execute();
my @resultados_productos = ();
while (my $cli=$stm->fetchrow_hashref) {
    push @resultados_productos, $cli;
    $total_results++;
}

print "<!-- Productos encontrados: " . scalar(@resultados_productos) . " -->\n";

# Preparar consulta de noticias
$a="(";
$c=0;
foreach my $n (@palabras) {
  $a=$a." or " if ($c==1);
 $a=$a."TITULO like '%$n%' or COPETE like '%$n%'";
 $c=1;
}
$a=$a.")";

# Contar resultados de noticias
$id=0;
my $stm_noticias = $dbh->prepare("select  * from NOTAS where PUBLICADA=0 and ESPECIAL=0 and NOESP=0 and ($a) ORDER BY FECHANOT desc,ID desc limit $id,9");
$stm_noticias->execute();
my @resultados_noticias = ();
while (my $noticia=$stm_noticias->fetchrow_hashref) {
    push @resultados_noticias, $noticia;
    $total_results++;
}

print "<!-- Noticias encontradas: " . scalar(@resultados_noticias) . " -->\n";

# Preparar consulta de revistas
$a="(";
$c=0;
foreach my $n (@palabras) {
  $a=$a." or " if ($c==1);
 $a=$a."$sp like '%$n%' ";
 $c=1;
}
$a=$a.")";

# Contar resultados de revistas
$id=0;
my $stm_revistas = $dbh->prepare("select  * from REVISTAS where ($a) ORDER BY REVISTA desc");
$stm_revistas->execute();
my @resultados_revistas = ();
while (my $revista_item=$stm_revistas->fetchrow_hashref) {
    push @resultados_revistas, $revista_item;
    $total_results++;
}

print "<!-- Revistas encontradas: " . scalar(@resultados_revistas) . " -->\n";
print "<!-- TOTAL resultados en BD: $total_results -->\n";

# NO mostrar el encabezado todavía, lo haremos después de verificar si hay algo que mostrar

# NO mostrar el encabezado todavía, lo haremos después de verificar si hay algo que mostrar

# Contador de items realmente mostrados en pantalla
my $items_displayed = 0;

print qq(<div class="results-wrapper pb-5">);

# --- PRODUCTS SECTION ---
if (scalar(@resultados_productos) > 0) {
    print qq(
        <div class="result-section mb-5">
            <div class="section-header-container">
                <h2 class="section-title">$results_found <span style="font-weight:400">"$formulario{producto}"</span></h2>
            </div>
            <div class="row">
    );

    foreach my $cli (@resultados_productos) {
        $items_displayed++;
        
        # Image Logic
        my $img_src = "";
        if ($cli->{fotoarchivo} eq "") {
            $img_src = "https://www.vetas.com/clientes/fotos/$cli->{fot}.jpg";
        } else {
            $img_src = "https://www.vetas.com/clientes/fotos/$cli->{fotoarchivo}";
        }
        
        # Title/Link Logic
        my $link_url = "";
        my $title_text = "";
        my $target = "";
        
        if ($cli->{SINDINAMICA}==0) {
            $link_url = "empresa.cgi?cliente=$cli->{ID}&i=$idioma&c=BUSCADOR_CLICKS&utm_source=web&utm_medium=buscador&utm_campaign=$cli->{EMPRESA}";
            $title_text = $cli->{$rub};
        } else {
            $link_url = "https://$cli->{SITE}";
            $title_text = $cli->{EMPRESA};
            $target = 'target="_blank"';
        }
        
        # Description Logic
        my $desc_text = "";
        my $desc_source = $cli->{$fdesc} || $cli->{DESCRIPT} || ""; # Fallback to DESCRIPT if fdesc empty? (Legacy logic had commented out fallback)
        if ($cli->{$fdesc}) { 
             $desc_source = $cli->{$fdesc};
        }
        
        if ($desc_source ne "") {
            $desc_text = substr($desc_source,0,150);
            $desc_text .= "..." if (length($desc_source)>=150);
        }

        print qq(
        <div class="col-md-6 col-lg-3 mb-4">
            <div class="result-card">
                <div class="result-card-img-wrapper">
                    <a href="$link_url" $target>
                        <img class="result-card-img" src="$img_src" alt="$cli->{EMPRESA}" loading="lazy">
                    </a>
                </div>
                <div class="result-card-body">
                    <h3 class="result-card-title"><a href="$link_url" $target>$title_text</a></h3>
                    <p class="result-card-desc">$desc_text</p>
                    
                    <div class="result-card-footer">
                        <img src="https://www.vetas.com/clientes/logos/$cli->{idcliente}.jpg" class="company-logo-small" alt="Logo" loading="lazy">
                         <a href="$link_url" $target class="btn-view-more">
                            Ver <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/></svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        );
    }
    print qq(</div></div>); # Close row and section
}

# --- NEWS SECTION ---
if (scalar(@resultados_noticias) > 0) {
    print qq(
        <div class="result-section mb-5">
            <div class="section-header-container">
                <h2 class="section-title">$noticias</h2>
            </div>
            <div class="row">
    );

    foreach my $noticia (@resultados_noticias) {
        $items_displayed++;
        
         # Photo logic
        $stm3 = $dbh->prepare("select * from NOTAS_FOTOS where ID_NOTAS=$noticia->{ID} and SLIDER=0");
        $stm3->execute();
        my $fot="https://www.vetas.com/notas/fotos/$noticia->{'ID'}_1.jpg";
        if (my $foto=$stm3->fetchrow_hashref) {
           $fot="https://www.vetas.com/notas/fotos/$noticia->{ID}_$foto->{ID}_$foto->{FOTO}";
        }
        
        print qq(
        <div class="col-md-6 col-lg-3 mb-4">
            <div class="news-card">
                <div class="news-img-wrapper">
                     <a href="noticias.cgi?noticia=$noticia->{ID}&i=$idioma&s=1">
                        <img src="$fot" class="news-img" alt="$noticia->{TITULO}" loading="lazy">
                     </a>
                </div>
                <div class="news-card-body">
                    <span class="news-date">$noticia->{FECHANOT}</span>
                    <h4 class="news-title">
                        <a href="noticias.cgi?noticia=$noticia->{ID}&i=$idioma&s=1">$noticia->{TITULO}</a>
                    </h4>
                    <p class="text-muted small mb-0">$noticia->{COPETE}</p>
                </div>
            </div>
        </div>
        );
    }
    print qq(</div></div>); # Close row and section
}

# --- MAGAZINES SECTION ---
if (scalar(@resultados_revistas) > 0) {
    print qq(
        <div class="result-section mb-5">
            <div class="section-header-container">
                <h2 class="section-title">$revivetas</h2>
            </div>
            <div class="row">
    );

    foreach my $revista_item (@resultados_revistas) {
        $items_displayed++;
        
        $stm2 = $dbh->prepare("select * from REVISTAS_CONFIG where REVISTA=$revista_item->{REVISTA}");
        $stm2->execute();
        my $revista_config=$stm2->fetchrow_hashref;
        
        my $fot="revista/$revista_item->{'REVISTA'}/$revista_item->{PAGINA}g.jpg";
        my $link = "https://www.vetas.com/maga.cgi?revista=$revista_item->{REVISTA}&i=$idioma&paginas=$revista_config->{PAGINAS}&pag=$revista_item->{PAGINA}";

        print qq(
        <div class="col-md-6 col-lg-3 mb-4">
             <div class="magazine-card">
                <div class="magazine-cover-wrapper">
                    <a href="$link">
                        <img src="$fot" class="magazine-cover" alt="Revista" loading="lazy">
                    </a>
                </div>
                <div class="magazine-info">
                    <div class="magazine-number">$revivetas N&deg;$revista_item->{REVISTA}</div>
                    <h5><a href="$link">$revista_item->{$sp}</a></h5>
                </div>
             </div>
        </div>
        );
    }
    print qq(</div></div>); # Close row and section
}

print "<!-- Items MOSTRADOS en pantalla: $items_displayed -->\n";

# Si no se mostró ningún resultado visible, mostrar mensaje
if ($items_displayed == 0) {
    print <<EOFHTML;
    <div class="col-12">
      <div class="no-results-container">
        <div class="no-results-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
          </svg>
        </div>
        <h3 class="no-results-title">$no_results_title</h3>
        <p class="no-results-message">$no_results_msg</p>
        <div class="suggestions-section">
          $no_results_suggestions
        </div>
      </div>
    </div>
EOFHTML
}

print <<EOFHTML;
</div> <!-- Close results-wrapper -->
</div> <!-- Close container -->
</main>

EOFHTML

open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}

$dbh->disconnect;
