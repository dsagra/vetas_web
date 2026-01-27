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
.card-block {max-height:300px;overflow:auto;}

.search-form-modern {
    margin: 2rem 0;
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

  .no-results-container {
    text-align: left;
    padding: 3rem 2.5rem;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 16px;
    margin: 2rem 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border: 1px solid #dee2e6;
  }

  .no-results-icon {
    color: #72bf44;
    margin-bottom: 1.5rem;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .no-results-icon svg {
    width: 64px;
    height: 64px;
  }

  .no-results-title {
    font-size: 1.8rem;
    color: #343a40;
    margin-bottom: 1rem;
    font-weight: 700;
    text-align: center;
  }

  .no-results-message {
    color: #495057;
    font-size: 1.15rem;
    margin-bottom: 2rem;
    text-align: center;
  }

  .suggestions-list {
    list-style: none;
    padding: 0;
    margin: 0;
    max-width: 600px;
    margin: 0 auto;
  }

  .suggestions-list li {
    padding: 0.75rem 1rem;
    margin-bottom: 0.75rem;
    background: white;
    border-left: 4px solid #72bf44;
    border-radius: 8px;
    color: #495057;
    font-size: 1rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
  }

  .suggestions-list li:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 8px rgba(114, 191, 68, 0.2);
  }

  .suggestions-list li strong {
    color: #343a40;
  }

  .suggestions-list li a {
    color: #72bf44;
    text-decoration: none;
    font-weight: 600;
    border-bottom: 2px solid transparent;
    transition: border-color 0.3s ease;
  }

  .suggestions-list li a:hover {
    border-bottom-color: #72bf44;
  }

  .search-query {
    color: #72bf44;
    font-weight: 600;
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
<main>
<div class="container">
  <!-- Search Section -->
  <div class="row justify-content-center mt-4">
    <div class="col-md-8">
      <form action="search.cgi" method="get" class="search-form-modern">
        <input type="hidden" name="i" value="$idioma">
        <div class="input-group input-group-lg">
          <input type="text" name="producto" class="form-control search-input-modern" placeholder="$search_placeholder" value="$formulario{producto}" aria-label="$search_button" required>
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

print <<EOFHTML;
<div class="row">
EOFHTML

# Contador de items realmente mostrados en pantalla
my $items_displayed = 0;
my $header_shown = 0;

$a="(";
$c=0;
foreach my $n (@palabras) {
  $a=$a." or " if ($c==1);
 $a=$a."R.$rub like '%$n%' ";
 $c=1;
}
$a=$a.")";

# Mostrar resultados de productos
foreach my $cli (@resultados_productos)
    {
      # Mostrar encabezado solo la primera vez que hay un resultado
      if ($header_shown == 0) {
          print qq(</div><div class="row justify-content-center"><div class="col-md-8"><h4 class="mb-4">$results_found: <span class="search-query">"$formulario{producto}"</span></h4></div></div><div class="row">);
          $header_shown = 1;
      }
      
      $items_displayed++;
      print qq(
           <div class="col-md-3">
              <div class="card mb-3  shadow-sm">

);
$tama="col-md-3";


    if ($cli->{fotoarchivo} eq "")
      {
    print qq(

<a href="empresa.cgi?cliente=$cli->{ID}&i=$idioma&c=BUSCADOR_CLICKS&utm_source=web&utm_medium=buscador&utm_campaign=$cli->{EMPRESA}">  <img class="card-img-top" src="https://www.vetas.com/clientes/fotos/$cli->{fot}.jpg" alt="Card image cap"></a>

  );
  }
else
   {
    print qq(

<a href="empresa.cgi?cliente=$cli->{ID}&i=$idioma&c=BUSCADOR_CLICKS&utm_source=web&utm_medium=buscador&utm_campaign=$cli->{EMPRESA}">  <img class="card-img-top" src="https://www.vetas.com/clientes/fotos/$cli->{fotoarchivo}" alt="Card image cap"></a>

  );
  }



  print qq(


<div class="card-body  card-block">
<a href="empresa.cgi?cliente=$cli->{ID}&i=$idioma&c=BUSCADOR_CLICKS&utm_source=web&utm_medium=buscador&utm_campaign=$cli->{EMPRESA}" onclick="gtag('event', 'clic', {'event_category': 'Click buscador', 'event_label': 'cliente=$cli->{ID}', 'value': '1'});"><b>$cli->{$rub}</b></a><br>
) if ($cli->{SINDINAMICA}==0);

print qq(


<div class="card-body  card-block">
<a target="_blank" href="https://$cli->{SITE}"><b>$cli->{EMPRESA}</b></a><br>
) if ($cli->{SINDINAMICA}==1);

if ($cli->{$fdesc})
  {
        my $string = $cli->{$fdesc};
        my $str = substr($string,0,150);

        print $str;
	print "...."        if (length($string)>=150);

  }
#  else
#    {
#      if ($cli->{fotodesc} eq "")
#        {
#        my $string = $cli->{DESCRIPT};
#        my $str = substr($string,0,150);
#        print $str;
#	print "...."        if (length($string)>=150);
#        }
#      else
#        {
#        my $string = $cli->{fotodesc};
#        my $str = substr($string,0,150);
#        print $str;
#	print "...."        if (length($string)>=150);
#
#    }
#    }

print qq(
<style>
 .card-img{
width: 50%;
}
</style>
<br>
  <a href="empresa.cgi?cliente=$cli->{ID}&i=$idioma&c=BUSCADOR_CLICKS&utm_source=web&utm_medium=buscador&utm_campaign=$cli->{EMPRESA}"><img class="card-img center-block" src="https://www.vetas.com/clientes/logos/$cli->{idcliente}.jpg" alt="Card image cap"></a>
  </div>




</div>
</div>
);
    }
print qq(</div></div>
<div class="container">
<div class="row">
  );

# Mostrar resultados de noticias
$cont=0;
foreach my $noticias (@resultados_noticias)
  {
    # Mostrar encabezado solo la primera vez que hay un resultado
    if ($header_shown == 0) {
        print qq(</div><div class="row justify-content-center"><div class="col-md-8"><h4 class="mb-4">$results_found: <span class="search-query">"$formulario{producto}"</span></h4></div></div><div class="row">);
        $header_shown = 1;
    }
   
    $items_displayed++;
    $cont++;
    $stm3 = $dbh->prepare("select  * from NOTAS_FOTOS where ID_NOTAS=$noticias->{ID} and SLIDER=0");
    $stm3->execute();
        $fot="https://www.vetas.com/notas/fotos/$noticias->{'ID'}_1.jpg";
        if ($foto=$stm3->fetchrow_hashref)
          {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
          }
          print qq(
           <div class="col-md-3">
              <div class="card mb-3  shadow-sm">
<div class="card-header  text-muted">
    Noticia
  </div>
 <img class="card-img-top" src="$fot"  alt="Responsive image">
<div class="card-body  card-block">
             
            <h4 >
                <a  href="noticias.cgi?noticia=$noticias->{ID}&i=$idioma&s=1">$noticias->{TITULO}</a>
              </h4>
              <div class="text-muted">$noticias->{FECHANOT}</div>
               <p>$noticias->{COPETE}</p>
               
          </div>
          </div>
          </div>
          <p>
        );
        
      }

$a="(";
$c=0;
foreach my $n (@palabras) {
  $a=$a." or " if ($c==1);
 $a=$a."$sp like '%$n%' ";
 $c=1;
}
$a=$a.")";

# Mostrar resultados de revistas
$cont=0;
foreach my $noticias (@resultados_revistas)
  {
    # Mostrar encabezado solo la primera vez que hay un resultado
    if ($header_shown == 0) {
        print qq(</div><div class="row justify-content-center"><div class="col-md-8"><h4 class="mb-4">$results_found: <span class="search-query">"$formulario{producto}"</span></h4></div></div><div class="row">);
        $header_shown = 1;
    }
   
$items_displayed++;
$stm2 = $dbh->prepare("select * from REVISTAS_CONFIG where REVISTA=$noticias->{REVISTA}");
$stm2->execute();
$revista=$stm2->fetchrow_hashref;

        $fot="revista/$noticias->{'REVISTA'}/$noticias->{PAGINA}g.jpg";
        
          print qq(
            <div class="col-md-4 mb-3">
              <div class="card h-100 shadow-sm">
                <div class="row no-gutters h-100">
                  <div class="col-md-5">
                    <img src="$fot" class="img-fluid h-100" style="object-fit: cover;" alt="Responsive image">
                  </div>
                  <div class="col-md-7">
                    <div class="card-body">
                      <h5>
                        <a href="https://www.vetas.com/maga.cgi?revista=$noticias->{REVISTA}&i=$idioma&paginas=$revista->{PAGINAS}&pag=$noticias->{PAGINA}">$noticias->{$sp}</a>
                      </h5>
                      <div class="text-muted">$revivetas N&deg;$noticias->{REVISTA}</div>
                      <p>$noticias->{$copete}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        );
        
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
