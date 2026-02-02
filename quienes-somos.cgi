#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use Entrada;
&Entrada;

use ConectarDB;
$dbh=ConectarDB->connectWeb();
$dbh->do("SET NAMES 'utf8'");
$dbh->do("SET CHARACTER SET utf8");

# Obtener configuración
$stm2 = $dbh->prepare("select * from CONFIG where ID=1");
$stm2->execute();
$revi=$stm2->fetchrow_hashref;

$stm2 = $dbh->prepare("select * from REVISTAS_CONFIG where REVISTA=$revi->{REVISTA}");
$stm2->execute();
$revista=$stm2->fetchrow_hashref;

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

# Textos según idioma
if ($idioma eq "es")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  $page_title="Quienes Somos - VETAS";
  $titulo="Quienes Somos";
  $subtitulo="L&iacute;deres en informaci&oacute;n de la industria maderera";
  $historia_titulo="Nuestra Historia";
  $historia_texto="VETAS es la revista l&iacute;der de la industria de la madera y el mueble en Am&eacute;rica Latina. Desde hace m&aacute;s de tres d&eacute;cadas, conectamos a fabricantes, distribuidores y profesionales del sector con informaci&oacute;n de valor, tendencias del mercado y oportunidades de negocio.";
  $mision_titulo="Nuestra Misi&oacute;n";
  $mision_texto="Ser el puente de informaci&oacute;n y comunicaci&oacute;n entre todos los actores de la cadena productiva de la industria maderera y del mueble, promoviendo el desarrollo sostenible del sector en toda Am&eacute;rica Latina.";
  $vision_titulo="Nuestra Visi&oacute;n";
  $vision_texto="Consolidarnos como la plataforma multimedia de referencia para la industria de la madera y el mueble en Am&eacute;rica Latina, expandiendo nuestro alcance digital y fortaleciendo las conexiones comerciales en la regi&oacute;n.";
  $que_hacemos_titulo="Qu&eacute; Hacemos";
  $revista_titulo="Revista Digital";
  $revista_texto="Publicaci&oacute;n mensual con las &uacute;ltimas noticias, tendencias, entrevistas y art&iacute;culos t&eacute;cnicos del sector maderero y del mueble.";
  $guia_titulo="Gu&iacute;a Maderera";
  $guia_texto="Directorio completo de empresas, productos y servicios de la industria en toda Latinoam&eacute;rica.";
  $noticias_titulo="Portal de Noticias";
  $noticias_texto="Actualizaciones diarias sobre eventos, ferias, lanzamientos de productos y novedades del sector.";
  $eventos_titulo="Cobertura de Eventos";
  $eventos_texto="Presencia en las principales ferias y exposiciones de la industria maderera en Am&eacute;rica Latina.";
  $alcance_titulo="Nuestro Alcance";
  $alcance_texto="Con presencia en m&aacute;s de 15 pa&iacute;ses de Am&eacute;rica Latina, VETAS llega a miles de profesionales del sector cada mes a trav&eacute;s de nuestras plataformas digitales.";
  $contacto_titulo="&iquest;Quieres conocer m&aacute;s?";
  $contacto_texto="Cont&aacute;ctanos para descubrir c&oacute;mo podemos ayudarte a crecer en la industria de la madera y el mueble.";
  $contacto_boton="Contactar";
  $volver_label="Volver al inicio";
  }
elsif ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  $page_title="About Us - VETAS";
  $titulo="About Us";
  $subtitulo="Leaders in wood industry information";
  $historia_titulo="Our History";
  $historia_texto="VETAS is the leading magazine for the wood and furniture industry in Latin America. For over three decades, we have been connecting manufacturers, distributors, and industry professionals with valuable information, market trends, and business opportunities.";
  $mision_titulo="Our Mission";
  $mision_texto="To be the information and communication bridge between all actors in the productive chain of the wood and furniture industry, promoting sustainable development of the sector throughout Latin America.";
  $vision_titulo="Our Vision";
  $vision_texto="To consolidate ourselves as the reference multimedia platform for the wood and furniture industry in Latin America, expanding our digital reach and strengthening commercial connections in the region.";
  $que_hacemos_titulo="What We Do";
  $revista_titulo="Digital Magazine";
  $revista_texto="Monthly publication featuring the latest news, trends, interviews, and technical articles from the wood and furniture sector.";
  $guia_titulo="Wood Directory";
  $guia_texto="Complete directory of companies, products, and services in the industry throughout Latin America.";
  $noticias_titulo="News Portal";
  $noticias_texto="Daily updates on events, trade shows, product launches, and industry news.";
  $eventos_titulo="Event Coverage";
  $eventos_texto="Presence at the main wood industry fairs and exhibitions in Latin America.";
  $alcance_titulo="Our Reach";
  $alcance_texto="With presence in more than 15 Latin American countries, VETAS reaches thousands of industry professionals each month through our digital platforms.";
  $contacto_titulo="Want to know more?";
  $contacto_texto="Contact us to discover how we can help you grow in the wood and furniture industry.";
  $contacto_boton="Contact Us";
  $volver_label="Back to home";
  }
elsif ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  $page_title="Quem Somos - VETAS";
  $titulo="Quem Somos";
  $subtitulo="L&iacute;deres em informa&ccedil;&atilde;o da ind&uacute;stria madeireira";
  $historia_titulo="Nossa Hist&oacute;ria";
  $historia_texto="VETAS &eacute; a revista l&iacute;der da ind&uacute;stria da madeira e do m&oacute;vel na Am&eacute;rica Latina. H&aacute; mais de tr&ecirc;s d&eacute;cadas, conectamos fabricantes, distribuidores e profissionais do setor com informa&ccedil;&otilde;es de valor, tend&ecirc;ncias do mercado e oportunidades de neg&oacute;cio.";
  $mision_titulo="Nossa Miss&atilde;o";
  $mision_texto="Ser a ponte de informa&ccedil;&atilde;o e comunica&ccedil;&atilde;o entre todos os atores da cadeia produtiva da ind&uacute;stria madeireira e moveleira, promovendo o desenvolvimento sustent&aacute;vel do setor em toda a Am&eacute;rica Latina.";
  $vision_titulo="Nossa Vis&atilde;o";
  $vision_texto="Consolidar-nos como a plataforma multim&iacute;dia de refer&ecirc;ncia para a ind&uacute;stria da madeira e do m&oacute;vel na Am&eacute;rica Latina, expandindo nosso alcance digital e fortalecendo as conex&otilde;es comerciais na regi&atilde;o.";
  $que_hacemos_titulo="O Que Fazemos";
  $revista_titulo="Revista Digital";
  $revista_texto="Publica&ccedil;&atilde;o mensal com as &uacute;ltimas not&iacute;cias, tend&ecirc;ncias, entrevistas e artigos t&eacute;cnicos do setor madeireiro e moveleiro.";
  $guia_titulo="Cadastro Madeireiro";
  $guia_texto="Diret&oacute;rio completo de empresas, produtos e servi&ccedil;os da ind&uacute;stria em toda a Am&eacute;rica Latina.";
  $noticias_titulo="Portal de Not&iacute;cias";
  $noticias_texto="Atualiza&ccedil;&otilde;es di&aacute;rias sobre eventos, feiras, lan&ccedil;amentos de produtos e novidades do setor.";
  $eventos_titulo="Cobertura de Eventos";
  $eventos_texto="Presen&ccedil;a nas principais feiras e exposi&ccedil;&otilde;es da ind&uacute;stria madeireira na Am&eacute;rica Latina.";
  $alcance_titulo="Nosso Alcance";
  $alcance_texto="Com presen&ccedil;a em mais de 15 pa&iacute;ses da Am&eacute;rica Latina, VETAS alcança milhares de profissionais do setor a cada m&ecirc;s atrav&eacute;s de nossas plataformas digitais.";
  $contacto_titulo="Quer saber mais?";
  $contacto_texto="Entre em contato para descobrir como podemos ajud&aacute;-lo a crescer na ind&uacute;stria da madeira e do m&oacute;vel.";
  $contacto_boton="Contato";
  $volver_label="Voltar ao in&iacute;cio";
  }

require "menu.cgi";
&menu($MENU);

print <<EOFHTML;
<title>$page_title</title>

<!-- Meta tags SEO -->
<meta name="description" content="VETAS, la revista líder de la industria de la madera y el mueble en América Latina. Conoce nuestra historia, misión y visión.">
<meta name="keywords" content="VETAS, revista madera, industria maderera, revista mueble, América Latina, quienes somos">

<!-- Open Graph -->
<meta property="og:title" content="$page_title">
<meta property="og:description" content="Conoce más sobre VETAS, la revista líder de la industria de la madera y el mueble en América Latina">
<meta property="og:image" content="https://www.vetas.com/images/logo_vetas.png">
<meta property="og:type" content="website">

<style>
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

  .quienes-somos-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem 1rem;
  }

  .hero-section {
    text-align: center;
    padding: 3rem 1rem;
    background: linear-gradient(135deg, var(--vetas-light) 0%, #ffffff 100%);
    border-radius: 16px;
    margin-bottom: 3rem;
    box-shadow: var(--shadow-sm);
  }

  .hero-section h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--vetas-dark);
    margin-bottom: 1rem;
  }

  .hero-section .subtitulo {
    font-size: 1.25rem;
    color: #5a6c7d;
    font-weight: 400;
  }

  .section-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--vetas-dark);
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

  .content-section {
    margin-bottom: 4rem;
  }

  .content-card {
    background: white;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    height: 100%;
  }

  .content-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-4px);
  }

  .content-card h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--vetas-dark);
    margin-bottom: 1rem;
  }

  .content-card p {
    color: #5a6c7d;
    line-height: 1.8;
    font-size: 1rem;
  }

  .icon-card {
    text-align: center;
    padding: 2rem;
    background: linear-gradient(135deg, #ffffff 0%, var(--vetas-light) 100%);
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    height: 100%;
    border-left: 4px solid var(--vetas-primary);
  }

  .icon-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-4px);
  }

  .icon-card .icon {
    font-size: 3rem;
    color: var(--vetas-primary);
    margin-bottom: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80px;
  }

  .icon-card .icon svg {
    width: 60px;
    height: 60px;
    fill: var(--vetas-primary);
  }

  .icon-card h4 {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--vetas-dark);
    margin-bottom: 1rem;
  }

  .icon-card p {
    color: #5a6c7d;
    font-size: 0.95rem;
    line-height: 1.6;
  }

  .cta-section {
    background: linear-gradient(135deg, var(--vetas-primary) 0%, var(--vetas-dark) 100%);
    color: white;
    text-align: center;
    padding: 3rem 2rem;
    border-radius: 16px;
    margin-top: 4rem;
    margin-bottom: 3rem;
    box-shadow: var(--shadow-lg);
  }

  .cta-section h2 {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
  }

  .cta-section p {
    font-size: 1.1rem;
    margin-bottom: 2rem;
    opacity: 0.95;
  }

  .btn-cta {
    display: inline-block;
    background: white;
    color: var(--vetas-primary);
    padding: 1rem 2.5rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.1rem;
    text-decoration: none;
    transition: var(--transition);
    box-shadow: var(--shadow-md);
  }

  .btn-cta:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-lg);
    color: var(--vetas-dark);
    text-decoration: none;
  }

  .stats-section {
    background: var(--vetas-light);
    padding: 3rem 2rem;
    border-radius: 16px;
    margin: 3rem 0;
  }

  @media (max-width: 768px) {
    .hero-section h1 {
      font-size: 2rem;
    }

    .hero-section .subtitulo {
      font-size: 1.1rem;
    }

    .section-title {
      font-size: 1.5rem;
    }

    .content-card {
      margin-bottom: 1.5rem;
    }
  }
</style>

<main role="main">
  <div class="quienes-somos-container">
    
    <!-- Hero Section -->
    <div class="hero-section">
      <h1>$titulo</h1>
      <p class="subtitulo">$subtitulo</p>
    </div>

    <!-- Historia -->
    <div class="content-section">
      <div class="row">
        <div class="col-md-12">
          <div class="content-card">
            <h2 class="section-title">$historia_titulo</h2>
            <p>$historia_texto</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Misión y Visión -->
    <div class="content-section">
      <div class="row">
        <div class="col-md-6 mb-4">
          <div class="content-card">
            <h3>$mision_titulo</h3>
            <p>$mision_texto</p>
          </div>
        </div>
        <div class="col-md-6 mb-4">
          <div class="content-card">
            <h3>$vision_titulo</h3>
            <p>$vision_texto</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Qué Hacemos -->
    <div class="content-section">
      <h2 class="section-title">$que_hacemos_titulo</h2>
      <div class="row">
        <div class="col-md-3 col-sm-6 mb-4">
          <div class="icon-card">
            <div class="icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
              </svg>
            </div>
            <h4>$revista_titulo</h4>
            <p>$revista_texto</p>
          </div>
        </div>
        <div class="col-md-3 col-sm-6 mb-4">
          <div class="icon-card">
            <div class="icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/>
              </svg>
            </div>
            <h4>$guia_titulo</h4>
            <p>$guia_texto</p>
          </div>
        </div>
        <div class="col-md-3 col-sm-6 mb-4">
          <div class="icon-card">
            <div class="icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
              </svg>
            </div>
            <h4>$noticias_titulo</h4>
            <p>$noticias_texto</p>
          </div>
        </div>
        <div class="col-md-3 col-sm-6 mb-4">
          <div class="icon-card">
            <div class="icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M17 12h-5v5h5v-5zM16 1v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-1V1h-2zm3 18H5V8h14v11z"/>
              </svg>
            </div>
            <h4>$eventos_titulo</h4>
            <p>$eventos_texto</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Alcance -->
    <div class="stats-section">
      <div class="row">
        <div class="col-md-12">
          <h2 class="section-title">$alcance_titulo</h2>
          <p style="font-size: 1.1rem; line-height: 1.8; color: #2c3e50;">$alcance_texto</p>
        </div>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="cta-section">
      <h2>$contacto_titulo</h2>
      <p>$contacto_texto</p>
      <a href="contacto.cgi?i=$idioma" class="btn-cta">$contacto_boton</a>
    </div>

  </div>
</main>

EOFHTML

$FOOTER="footer.html";
open FOOTER;
while (<FOOTER>) 
{
  $linea = $_;
  print "$linea";
}
close FOOTER;

$dbh->disconnect;
