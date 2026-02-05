#!/usr/bin/perl
package ProductosDestacados;

use strict;
use warnings;

# Subrutina para mostrar el carrusel de productos destacados
# Parámetros: $dbh (database handle), $idioma (es/en/br)
sub mostrar_carousel {
    my ($dbh, $idioma) = @_;
    
    # Textos según idioma
    my $featured_title = "Productos Destacados";
    $featured_title = "Featured Products" if ($idioma eq "en");
    $featured_title = "Produtos em Destaque" if ($idioma eq "br");
    
    my $view_product = "Ver producto";
    $view_product = "View product" if ($idioma eq "en");
    $view_product = "Ver produto" if ($idioma eq "br");
    
    my @carousel_products = ();
    
    # 1. Primera Prioridad: Clientes activos con fotos destacadas (DESTACADO=1)
    my @featured_products = ();
    my %seen_clients = ();
    
    # Obtener fotos destacadas
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
    
    # 2. Segunda Prioridad: Clientes activos SIN fotos destacadas
    my @regular_products = ();
    
    # Obtener pool aleatorio de fotos regulares para llenar el resto
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
    
    # Combinar listas: Destacados primero, luego Regulares
    # Nota: NO mezclamos la lista final porque queremos que los destacados aparezcan primero
    @carousel_products = (@featured_products, @regular_products);
    
    # Generar HTML del carrusel
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
            
            # Escapar comillas para HTML
            $p_title =~ s/"/&quot;/g;
            my $empresa_safe = $prod->{EMPRESA_NAME};
            $empresa_safe =~ s/"/&quot;/g;
            
            # Lógica del enlace
            my $prod_link = "empresa.cgi?cliente=$prod->{CLIENTE_ID}&i=$idioma";
    
            # URL del logo de la empresa
            my $logo_url = "https://www.vetas.com/clientes/logos/$prod->{CLIENTE_ID}.jpg";
            
            print qq(
                <div class="product-card">
                     <a href="$prod_link">
                        <img src="$img_url" alt="$p_title" loading="lazy" class="product-image">
                     </a>
                    <div class="company-logo-wrapper">
                        <a href="$prod_link">
                            <img src="$logo_url" alt="$empresa_safe" class="company-logo" onerror="this.style.display='none'">
                        </a>
                    </div>
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
}

# Subrutina para generar los estilos CSS del carrusel
# Esta función puede ser llamada para incluir los estilos en el <head>
sub estilos_css {
    return qq(
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

  .company-logo-wrapper {
    text-align: center;
    margin: 0;
    padding: 0.75rem 0;
    background: #f8f9fa;
    border-bottom: 1px solid #eee;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .company-logo {
    width: 100%;
    max-height: 50px;
    height: auto;
    object-fit: contain;
    padding: 0 1rem;
    transition: var(--transition);
  }

  .company-logo:hover {
    transform: scale(1.05);
  }

  .product-card .product-image {
    transition: var(--transition);
  }

  .product-card:hover .product-image {
    transform: scale(1.05);
  }
    );
}

1; # Retornar verdadero para que el módulo se cargue correctamente
