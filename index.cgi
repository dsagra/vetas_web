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
  $vermasferias="Ver m&aacute;s ferias";
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
  $vermasferias="View more fairs";
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
  $leer="Ler not&iacute;cia";
  $ivideo="TITULO_BR";
  $fertxt="Feiras";
  $vermasferias="Ver mais feiras";
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

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
{
  "\@context": "https://schema.org",
  "\@type": "Magazine",
  "name": "VETAS",
  "url": "https://www.vetas.com",
  "logo": "https://www.vetas.com/images/logo_vetas.png",
  "description": "La revista l&iacute;der de la industria de la madera y el mueble en Am&eacute;rica Latina",
  "publisher": {
    "\@type": "Organization",
    "name": "VETAS",
    "logo": {
      "\@type": "ImageObject",
      "url": "https://www.vetas.com/images/logo_vetas.png"
    },
    "address": {
      "\@type": "PostalAddress",
      "addressLocality": "Buenos Aires",
      "addressCountry": "AR"
    },
    "contactPoint": [
      {
        "\@type": "ContactPoint",
        "telephone": "+54-11-4803-9650",
        "contactType": "customer service",
        "areaServed": "LATAM",
        "availableLanguage": ["Spanish", "English", "Portuguese"]
      },
      {
        "\@type": "ContactPoint",
        "telephone": "+1-305-968-3936",
        "contactType": "customer service",
        "areaServed": "US",
        "availableLanguage": ["English", "Spanish"]
      }
    ]
  },
  "sameAs": [
    "https://www.facebook.com/vetascom",
    "https://twitter.com/vetascom",
    "https://www.instagram.com/vetascom"
  ],
  "inLanguage": ["es", "en", "pt-BR"]
}
</script>

<style>
  /* Modern UI Improvements */
  :root {
    --vetas-primary: #72bf44;
    --vetas-dark: #2c5f2d;
    --vetas-light: #e8f5e3;
    --vetas-accent: #f39c12;
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.08);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.12);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.15);
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .hero-banner {
    margin-bottom: 2rem;
    overflow: hidden;
  }

  .section-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 1.5rem;
    position: relative;
    padding-bottom: 0.75rem;
  }

  .section-title::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 60px;
    height: 4px;
    background: linear-gradient(to right, var(--vetas-primary), var(--vetas-accent));
    border-radius: 2px;
  }

  .modern-card {
    border: none;
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    overflow: hidden;
    height: 100%;
    background: white;
  }

  .modern-card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-lg);
  }

  .modern-card .card-img-top {
    border-radius: 0;
    height: 200px;
    object-fit: cover;
    transition: var(--transition);
  }

  .modern-card:hover .card-img-top {
    transform: scale(1.05);
  }

  .modern-card .card-body {
    padding: 1.5rem;
  }

  .modern-card h2 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 0.75rem;
    line-height: 1.4;
  }

  .modern-card p {
    color: #5a6c7d;
    font-size: 0.95rem;
    line-height: 1.6;
  }

  .btn-modern {
    background: linear-gradient(135deg, var(--vetas-primary), var(--vetas-dark));
    border: none;
    border-radius: 8px;
    padding: 0.625rem 1.5rem;
    font-weight: 600;
    color: white;
    transition: var(--transition);
    text-decoration: none;
    display: inline-block;
  }

  .btn-modern:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
    color: white;
    background: linear-gradient(135deg, var(--vetas-dark), var(--vetas-primary));
  }

  .magazine-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border-radius: 12px;
    box-shadow: var(--shadow-md);
    padding: 2rem;
    height: 100%;
    transition: var(--transition);
    border-left: 4px solid var(--vetas-primary);
  }

  .magazine-card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateX(4px);
  }

  .magazine-card h4 {
    color: var(--vetas-dark);
    font-weight: 700;
    margin-bottom: 0.5rem;
  }

  .magazine-card .text-muted {
    color: #6c757d !important;
    font-size: 0.9rem;
    margin-bottom: 1rem;
  }

  .magazine-link {
    display: block;
    padding: 0.5rem 0;
    color: #495057;
    text-decoration: none;
    transition: var(--transition);
    font-size: 0.95rem;
  }

  .magazine-link:hover {
    color: var(--vetas-primary);
    padding-left: 0.5rem;
    text-decoration: none;
  }

  .magazine-link .glyphicon {
    color: var(--vetas-accent);
    margin-right: 0.5rem;
  }

  .banner-section {
    margin: 3rem 0;
    padding: 2rem 0;
    background: linear-gradient(to bottom, transparent, var(--vetas-light), transparent);
  }

  .video-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
  }

  .video-card:hover {
    box-shadow: var(--shadow-md);
  }

  .video-card .embed-responsive {
    border-radius: 12px 12px 0 0;
  }

  .video-card p {
    padding: 1rem;
    margin: 0;
  }

  .events-widget {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
  }

  .event-item {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
  }

  .event-item:hover {
    transform: translateX(4px);
    box-shadow: var(--shadow-md);
  }

  .event-link {
    color: var(--vetas-dark);
    font-weight: 600;
    text-decoration: none;
    font-size: 1rem;
  }

  .event-link:hover {
    color: var(--vetas-primary);
  }

  .event-date {
    color: #6c757d;
    font-size: 0.85rem;
    margin-top: 0.25rem;
  }

  .ad-card {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    background: white;
    padding: 0.5rem;
  }

  .ad-card:hover {
    box-shadow: var(--shadow-md);
    transform: scale(1.02);
  }

  .ad-card img {
    border-radius: 8px;
  }

  .container-spacing {
    margin-top: 3rem;
    margin-bottom: 3rem;
  }

  .magazine-cover {
    border-radius: 8px;
    box-shadow: var(--shadow-md);
    transition: var(--transition);
  }

  .magazine-cover:hover {
    transform: scale(1.05) rotate(2deg);
    box-shadow: var(--shadow-lg);
  }

  /* Carousel CSS */
  .scrolling-wrapper {
    -webkit-overflow-scrolling: touch;
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    padding-bottom: 20px;
    padding-top: 10px;
    padding-left: 5px;
    padding-right: 5px;
    gap: 20px;
    scrollbar-width: thin;
  }
  
  .scrolling-wrapper::-webkit-scrollbar {
    height: 8px;
  }
  
  .scrolling-wrapper::-webkit-scrollbar-track {
    background: #f1f1f1; 
    border-radius: 4px;
  }
  
  .scrolling-wrapper::-webkit-scrollbar-thumb {
    background: #ccc; 
    border-radius: 4px;
  }
  
  .scrolling-wrapper::-webkit-scrollbar-thumb:hover {
    background: #999; 
  }

  .product-card {
    flex: 0 0 auto;
    width: 260px;
    background: white;
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(0,0,0,0.05);
  }

  .product-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
  }

  .product-card img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-bottom: 1px solid #eee;
  }

  .product-card .card-body {
    padding: 1rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }

  .product-card h5 {
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--vetas-dark);
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    height: 2.6em; /* fixed height for 2 lines */
  }

  .product-card .company-name {
    font-size: 0.8rem;
    color: var(--vetas-accent);
    margin-bottom: 0.5rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .product-card .btn-view {
    margin-top: auto;
    font-size: 0.85rem;
    padding: 0.5rem 1rem;
    background: var(--vetas-light);
    color: var(--vetas-dark);
    border: none;
    border-radius: 50px;
    width: 100%;
    text-align: center;
    transition: var(--transition);
    text-decoration: none;
    font-weight: 600;
  }

  .product-card .btn-view:hover {
    background: var(--vetas-primary);
    color: white;
  }

</style>

  <main role="main">

 <div class="container">

  <div class="row">
    <div class="col-md-12 hero-banner">
EOFHTML
       &banne2(1200, $dbh, $revi, $idioma);

# Preparar textos del buscador según idioma
my $search_placeholder = "";
my $search_button = "";
if ($idioma eq "es") {
    $search_placeholder = "Buscar productos, empresas, noticias...";
    $search_button = "Buscar";
} elsif ($idioma eq "en") {
    $search_placeholder = "Search products, companies, news...";
    $search_button = "Search";
} else {
    $search_placeholder = "Pesquisar produtos, empresas, not&iacute;cias...";
    $search_button = "Pesquisar";
}

print <<EOFHTML;
    </div>
  </div>

</div>

<!-- Search Section -->
<div class="container mt-4">
  <div class="row justify-content-center">
    <div class="col-md-8">
      <form action="search.cgi" method="get" class="search-form-modern">
        <input type="hidden" name="i" value="$idioma">
        <div class="input-group input-group-lg">
          <input type="text" name="producto" class="form-control search-input-modern" placeholder="$search_placeholder" aria-label="$search_button" required>
          <div class="input-group-append">
            <button class="btn btn-search-modern" type="submit">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
              </svg>
              $search_button
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>

<style>
  .search-form-modern {
    margin: 1.5rem 0;
  }

  .search-input-modern {
    border: 2px solid #e9ecef;
    border-right: none;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    border-radius: 50px 0 0 50px !important;
    transition: all 0.3s ease;
  }

  .search-input-modern:focus {
    border-color: #72bf44;
    box-shadow: 0 0 0 0.2rem rgba(114, 191, 68, 0.15);
    outline: none;
  }

  .btn-search-modern {
    background: linear-gradient(135deg, #72bf44 0%, #5fa835 100%);
    border: 2px solid #72bf44;
    color: white;
    padding: 0.75rem 2rem;
    font-weight: 600;
    border-radius: 0 50px 50px 0 !important;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .btn-search-modern:hover {
    background: linear-gradient(135deg, #5fa835 0%, #4d8c2a 100%);
    border-color: #5fa835;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(114, 191, 68, 0.4);
  }

  .btn-search-modern svg {
    width: 18px;
    height: 18px;
  }

  @media (max-width: 768px) {
    .search-input-modern {
      font-size: 0.9rem;
      padding: 0.625rem 1rem;
    }

    .btn-search-modern {
      padding: 0.625rem 1.25rem;
    }
  }
</style>

<div class="container container-spacing">
    <div class="row mb-4">
        <div class="col-md-6 mb-3">
          <div class="magazine-card d-flex flex-column flex-md-row">
            <div class="flex-grow-1">
              <h4>
                <a href="maga.cgi?i=$idioma&revista=$revi->{REVISTA}&paginas=$revista->{PAGINAS}&indice=$revista->{INDICE}" style="text-decoration: none; color: inherit;">$vet N&deg;$revi->{REVISTA}</a>
              </h4>
              <div class="text-muted">$revi->{$mes}</div>
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

	print qq(<a href="maga.cgi?i=$idioma&revista=$notas->{REVISTA}&indice=$revista->{INDICE}&paginas=$revista->{PAGINAS}&pag=$notas->{PAGINA}" class="magazine-link"><span class="glyphicon glyphicon-star" aria-hidden="true"></span> $notas->{$idi}</a>)
	}

print <<EOFHTML;
               
          <a href="revistasanteriores.cgi?i=$idioma" class="btn-modern mt-3">$edi</a>
               
            </div>
            <a href="maga.cgi?i=$idioma&revista=$revi->{REVISTA}&indice=$revista->{INDICE}&paginas=$guiaCantPaginas&pag=1" class="ml-md-3 mt-3 mt-md-0"><img class="magazine-cover d-none d-lg-block" src="revista/$revista->{REVISTA}/1g.jpg" width="150px" height="210px" alt="$vet"></a>
          </div>
        </div>

        <div class="col-md-6 mb-3">
          <div class="magazine-card d-flex flex-column flex-md-row">
            <div class="flex-grow-1">
              <h4>
                <a href="maga.cgi?revista=$revi->{GUIA}&paginas=$guiaCantPaginas" target="_blank" style="text-decoration: none; color: inherit;">$guia</a>
              </h4>
              <div class="text-muted">$guiaMes</div>
EOFHTML

$stm3 = $dbh->prepare("select * from REVISTAS where REVISTA=$revi->{GUIA}  order by PAGINA");
$stm3->execute();
$c=1;
while ($notas=$stm3->fetchrow_hashref)
  {
    print qq(<a href="maga.cgi?revista=$revi->{GUIA}&paginas=$guiaCantPaginas&pag=$notas->{PAGINA}" class="magazine-link"><span class="glyphicon glyphicon-star" aria-hidden="true"></span> $notas->{$idi}</a>)
  }

print <<EOFHTML;
  
            </div>
            <a href="maga.cgi?revista=$revi->{GUIA}&paginas=$guiaCantPaginas" class="ml-md-3 mt-3 mt-md-0"><img class="magazine-cover d-none d-lg-block" src="revista/$revi->{GUIA}/1g.jpg" width="150px" height="210px" alt="$guia"></a>
          </div>
        </div>
    </div>
    </div>
EOFHTML

# FEATURED PRODUCTS CAROUSEL START
my $featured_title = "Productos Destacados";
$featured_title = "Featured Products" if ($idioma eq "en");
$featured_title = "Produtos em Destaque" if ($idioma eq "br");

my $view_product = "Ver producto";
$view_product = "View product" if ($idioma eq "en");
$view_product = "Ver produto" if ($idioma eq "br");

my @carousel_products = ();

# 1. First Priority: Active clients with Featured (DESTACADO=1) photos
my @featured_products = ();
my %seen_clients = ();

# Fetch potential featured photos
my $sth_feat = $dbh->prepare("
    SELECT F.ID, F.ARCHIVO, F.DESCRIPT, F.DESCRIPT_EN, F.DESCRIPT_BR, U.EMPRESA, U.ID as CLIENTE_ID
    FROM FOTOS F
    JOIN USUARIOS U ON F.CLIENTE = U.ID
    WHERE F.DESTACADO=1
      AND (U.ACTIVO=1 OR U.ACTIVO_REVISTA!=0 OR U.ACTIVO_GUIA!=0)
      AND (F.FECHAVENCE='' OR F.FECHAVENCE > NOW())
    ORDER BY RAND()
");
$sth_feat->execute();

while (my $prod = $sth_feat->fetchrow_hashref) {
    next if $seen_clients{$prod->{CLIENTE_ID}};
    $seen_clients{$prod->{CLIENTE_ID}} = 1;
    $prod->{EMPRESA_NAME} = $prod->{EMPRESA};
    push @featured_products, $prod;
}

# 2. Second Priority: Active clients WITHOUT featured photos (or at least, not yet shown)
my @regular_products = ();

# Fetch random pool of regular photos to fill in the rest
# We prioritize photos that aren't featured, but technically we just want 'a photo' for the remaining clients
my $sth_reg = $dbh->prepare("
    SELECT F.ID, F.ARCHIVO, F.DESCRIPT, F.DESCRIPT_EN, F.DESCRIPT_BR, U.EMPRESA, U.ID as CLIENTE_ID
    FROM FOTOS F
    JOIN USUARIOS U ON F.CLIENTE = U.ID
    WHERE (U.ACTIVO=1 OR U.ACTIVO_REVISTA!=0 OR U.ACTIVO_GUIA!=0)
      AND (F.FECHAVENCE='' OR F.FECHAVENCE > NOW())
    ORDER BY RAND()
    LIMIT 300
");
$sth_reg->execute();

while (my $prod = $sth_reg->fetchrow_hashref) {
    next if $seen_clients{$prod->{CLIENTE_ID}};
    $seen_clients{$prod->{CLIENTE_ID}} = 1;
    $prod->{EMPRESA_NAME} = $prod->{EMPRESA};
    push @regular_products, $prod;
}

# Combine lists: Featured first, then Regular
# Note: We do NOT shuffle the final list because we want Featured to appear first
@carousel_products = (@featured_products, @regular_products);


if (@carousel_products > 0) {
    print qq(
    <div class="container container-spacing">
        <div class="row">
            <div class="col-md-12">
                <h3 class="section-title">$featured_title</h3>
            </div>
        </div>
        <div class="scrolling-wrapper">
    );

    foreach my $prod (@carousel_products) {
        my $foto = $prod->{ARCHIVO};
        $foto = "$prod->{ID}.jpg" if ($foto eq "");
        
        my $img_url = "https://www.vetas.com/clientes/fotos/$foto";
        
        my $p_title = $prod->{DESCRIPT};
        if ($idioma eq "en" && $prod->{DESCRIPT_EN}) { $p_title = $prod->{DESCRIPT_EN}; }
        if ($idioma eq "br" && $prod->{DESCRIPT_BR}) { $p_title = $prod->{DESCRIPT_BR}; }
        $p_title = "Producto" if ($p_title eq "");
        
        # Escape quotes for HTML
        $p_title =~ s/"/&quot;/g;
        my $empresa_safe = $prod->{EMPRESA_NAME};
        $empresa_safe =~ s/"/&quot;/g;
        
        # Link logic
        my $prod_link = "empresa.cgi?cliente=$prod->{CLIENTE_ID}&i=$idioma";

        print qq(
            <div class="product-card">
                 <a href="$prod_link">
                    <img src="$img_url" alt="$p_title" loading="lazy">
                 </a>
                <div class="card-body">
                    <div class="company-name" title="$empresa_safe">$prod->{EMPRESA_NAME}</div>
                    <h5 title="$p_title">$p_title</h5>
                    <a href="$prod_link" class="btn-view">$view_product</a>
                </div>
            </div>
        );
    }

    print qq(
        </div>
    </div>
    );
}
# FEATURED PRODUCTS CAROUSEL END

print <<EOFHTML;

<div class="container container-spacing">
  <div class="row">
    <div class="col-md-12">
      <h3 class="section-title">$notitit</h3>
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
          <div class="col-md-4 mb-4">
            <div class="modern-card">
              <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">
                <img class="card-img-top" src="$fot" alt="$noticias->{$t}">
              </a>
              <div class="card-body">
                <h2>$noticias->{$t}</h2>
                <p>$noticias->{$c}</p>
                <a class="btn-modern" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a>
              </div>
            </div>
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
</div>

<div class="banner-section">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
      </div>
    </div>
  </div>
</div>

<div class="container container-spacing">
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
          <div class="col-md-4 mb-4">
            <div class="modern-card">
              <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">
                <img class="card-img-top" src="$fot" alt="$noticias->{$t}">
              </a>
              <div class="card-body">
                <h2>$noticias->{$t}</h2>
                <p>$noticias->{$c}</p>
                <a class="btn-modern" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a>
              </div>
            </div>
          </div>
          );
      }

print <<EOFHTML;
          
          <div class="col-md-4 mb-4">
            <div class="events-widget">
              <h3 class="section-title">$fertxt</h3>
EOFHTML
$stm32 = $dbh->prepare("SELECT * FROM `FERIAS` WHERE FIN >NOW() order by INICIO limit 0,6");
$stm32->execute();
while ($feria=$stm32->fetchrow_hashref)
  {

print qq(
          <div class="event-item">
            <a href="https://$feria->{SITE}" target="_blank" class="event-link">$feria->{NOMBRE}</a>
            <div class="event-date">$feria->{PAIS} - $feria->{INICIO}/$feria->{FIN}</div>
          </div>
          );

  }

print qq(
              <a href="ferias.cgi?i=$idioma" class="btn-modern mt-3 d-block text-center">$vermasferias</a>
          );

    
 print <<EOFHTML;    
            </div>     
          </div>
  </div>
</div>
<div class="banner-section">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
      </div>
    </div>
  </div>
</div>

<div class="container container-spacing">
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
          <div class="col-md-4 mb-4">
            <div class="modern-card">
              <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">
                <img class="card-img-top" src="$fot" alt="$noticias->{$t}">
              </a>
              <div class="card-body">
                <h2>$noticias->{$t}</h2>
                <p>$noticias->{$c}</p>
                <a class="btn-modern" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a>
              </div>
            </div>
          </div>
          );

$stm5 = $dbh->prepare("select  * from ORDEN as O, FOTOS AS F where O.REVISTA=$avisorevista and F.CLIENTE=O.ID_CLIENTE and F.REVISTA=$avisorevista and (F.FORMATO='PAGINA' or F.FORMATO='CUARTO') order by RAND()");
$stm5->execute();
$aviso=$stm5->fetchrow_hashref;
$fot="https://www.vetas.com/clientes/fotos/".$aviso->{ARCHIVO};
print <<EOFHTML;         
           <div class="col-md-4 mb-4">
              <a href="empresa.cgi?cliente=$aviso->{ID_CLIENTE}&i=$idioma&c=AVISO_CLICKS">
                <img class="imgaviso" src="$fot" width="100%" alt="Anuncio">
              </a>
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
          <div class="col-md-4 mb-4">
            <div class="modern-card">
              <a href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">
                <img class="card-img-top" src="$fot" alt="$noticias->{$t}">
              </a>
              <div class="card-body">
                <h2>$noticias->{$t}</h2>
                <p>$noticias->{$c}</p>
                <a class="btn-modern" href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}" role="button">$leer &raquo;</a>
              </div>
            </div>
          </div>
          );

print <<EOFHTML; 
  </div>
</div>
<div class="banner-section">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       #&banne(174);
print <<EOFHTML;
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       #&banne(174);

print <<EOFHTML;      
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
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

<div class="container container-spacing">
  <div class="row">
    <div class="col-md-12">
      <h3 class="section-title">Videos</h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-4 mb-4">
      <div class="video-card">
        <div class="embed-responsive embed-responsive-16by9">
          <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/$video1->{VIDEO}?rel=0" allowfullscreen></iframe>
        </div>
        <p><strong>$video1->{$ivideo}</strong></p>
        <p style="padding: 0 1rem 1rem;"><a class="btn-modern" href="empresa.cgi?cliente=$video1->{CLIENTE}&i=$idioma&c=VIDEO_CLICKS" role="button">$verempresa &raquo;</a></p>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="video-card">
        <div class="embed-responsive embed-responsive-16by9">
          <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/$video2->{VIDEO}?rel=0" allowfullscreen></iframe>
        </div>
        <p><strong>$video2->{$ivideo}</strong></p>
        <p style="padding: 0 1rem 1rem;"><a class="btn-modern" href="empresa.cgi?cliente=$video2->{CLIENTE}&i=$idioma&c=VIDEO_CLICKS" role="button">$verempresa &raquo;</a></p>
      </div>
    </div>
EOFHTML
$stm5 = $dbh->prepare("select  * from ORDEN as O, FOTOS AS F where O.REVISTA=$avisorevista and F.CLIENTE=O.ID_CLIENTE and F.REVISTA=$avisorevista and (F.FORMATO='OCTAVO' or F.FORMATO='MEDIA') order by RAND()");
$stm5->execute();
$aviso=$stm5->fetchrow_hashref;
$fot="https://www.vetas.com/clientes/fotos/".$aviso->{ARCHIVO};
print <<EOFHTML;         
    <div class="col-md-4 mb-4">
        <a href="empresa.cgi?cliente=$aviso->{ID_CLIENTE}&i=$idioma&c=AVISO_CLICKS">
          <img class="imgaviso" src="$fot" width="100%" alt="Anuncio">
        </a>
    </div>
  </div>
</div>
<div class="banner-section">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
      </div>
      <div class="col-md-4 col-sm-6 mb-3">
EOFHTML
       &banne(174, $dbh, $revi, $idioma);
print <<EOFHTML;      
      </div>
    </div>
  </div>
</div>

EOFHTML

# Incluir la sección de suscripción según el idioma
if ($idioma eq "es") {
    open SUSCRIPCION, "components/seccion-suscripcion.html" or warn "No se pudo abrir seccion-suscripcion.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}
elsif ($idioma eq "en") {
    open SUSCRIPCION, "components/seccion-suscripcion-en.html" or warn "No se pudo abrir seccion-suscripcion-en.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
}
elsif ($idioma eq "br") {
    open SUSCRIPCION, "components/seccion-suscripcion-br.html" or warn "No se pudo abrir seccion-suscripcion-br.html: $!";
    while (<SUSCRIPCION>) {
        print $_;
    }
    close SUSCRIPCION;
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




$dbh->disconnect;