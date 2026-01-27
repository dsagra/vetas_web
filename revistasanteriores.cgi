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
  $sp="SP";
  $rev="Revista VETAS";
  $mes="MES";
  }
if ($idioma eq "en")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  $sp="EN";
  $rev="VETAS Magazine";
  $mes="MES_EN";
  }
if ($idioma eq "br")
  {
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  $sp="BR";
  $rev="Revista VETAS";
  $mes="MES_BR";
  }


$FOOTER="footer.html";

require "menu.cgi";
&menu($MENU);

print <<EOFHTML;

<style>
.container.mt-4 {
  margin-top: 1.5rem !important;
}

.display-4 {
  font-size: 3.5rem;
  font-weight: 300;
  line-height: 1.2;
}

.lead {
  font-size: 1.25rem;
  font-weight: 300;
}

.text-muted {
  color: #6c757d !important;
}

.revistas-header {
  margin-bottom: 3rem;
}

.revista-card {
  transition: all 0.3s ease;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  background: white;
  height: 100%;
}

.revista-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

.revista-card .card-body {
  padding: 1.5rem;
}

.revista-card h4 {
  color: #2c3e50;
  font-weight: bold;
  margin-bottom: 0.75rem;
  font-size: 1.4rem;
}

.revista-card h4 a {
  color: #2c3e50;
  text-decoration: none;
  transition: color 0.3s ease;
}

.revista-card h4 a:hover {
  color: #72bf44;
}

.fecha-revista {
  color: #6c757d;
  font-size: 0.95rem;
  font-weight: 500;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
}

.fecha-revista::before {
  content: "\\1F4C5";
  margin-right: 0.5rem;
}

.revista-notas {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.titvetas {
  text-decoration: none;
  font-size: 0.9rem;
  color: #495057;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  padding: 0.4rem 0.6rem;
  border-radius: 8px;
  background: #f8f9fa;
}

.titvetas:hover {
  text-decoration: none;
  color: #72bf44;
  background: #e8f5e9;
  padding-left: 1rem;
  transform: translateX(4px);
}

.titvetas .glyphicon {
  margin-right: 0.5rem;
  color: #72bf44;
}

.revista-cover {
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transition: transform 0.3s ease;
  flex-shrink: 0;
}

.revista-card:hover .revista-cover {
  transform: scale(1.05);
}

.revista-cover img {
  width: 100px;
  height: 140px;
  display: block;
  object-fit: cover;
}

.revista-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(500px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

@media (max-width: 768px) {
  .revista-grid {
    grid-template-columns: 1fr;
  }
  
  .display-4 {
    font-size: 2.5rem;
  }
  
  .revista-cover img {
    width: 80px;
    height: 112px;
  }
}

.loading-indicator {
  text-align: center;
  padding: 2rem;
  color: #6c757d;
}
</style>

  <main role="main">
    <div class="container mt-4">
      <!-- Header Section -->
      <div class="row mb-4">
        <div class="col-md-12 text-center revistas-header">
          <h1 class="display-4">Ediciones Anteriores</h1>
          <p class="lead text-muted">Explora nuestra colecci&oacute;n de revistas VETAS</p>
        </div>
      </div>

      <div class="revista-grid">
EOFHTML
$x=0;
$stm2 = $dbh->prepare("select * from REVISTAS_CONFIG order by REVISTA desc limit 0,22");
$stm2->execute();
while ($revista=$stm2->fetchrow_hashref)
  {
$x++;
print <<EOFHTML;
        <div class="col">
          <div class="revista-card">
            <div class="d-flex flex-column flex-md-row h-100">
              <div class="card-body d-flex flex-column justify-content-between flex-grow-1">
                <div>
                  <h4>
                    <a href="maga.cgi?revista=$revista->{REVISTA}&paginas=$revista->{PAGINAS}&i=$idioma">$rev N&deg; $revista->{REVISTA}</a>
                  </h4>
                  <div class="fecha-revista">$revista->{$mes}</div>
                  <div class="revista-notas">
EOFHTML

$stm3 = $dbh->prepare("select * from REVISTAS where REVISTA=$revista->{REVISTA}  order by PAGINA");
$stm3->execute();
$c=1;
while ($notas=$stm3->fetchrow_hashref)
	{
	print qq(<a href="maga.cgi?revista=$notas->{REVISTA}&paginas=$revista->{PAGINAS}&pag=$notas->{PAGINA}&i=$idioma" class="titvetas"><span class="glyphicon glyphicon-star" aria-hidden="true"></span> $notas->{$sp}</a>)
	}
 

      print <<EOFHTML;
                  </div>
                </div>
              </div>
              <div class="revista-cover align-self-center m-3">
                <a href="maga.cgi?revista=$revista->{REVISTA}&paginas=$revista->{PAGINAS}&i=$idioma">
                  <img src="revista/$revista->{REVISTA}/1g.jpg" alt="Revista VETAS N°$revista->{REVISTA}">
                </a>
              </div>
            </div>
          </div>
        </div>
EOFHTML

}


print <<EOFHTML;
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