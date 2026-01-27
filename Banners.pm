package Banners;

use strict;
use warnings;
use Exporter qw(import);

our @EXPORT = qw(banne banne2 contarbanner contar);

# Banner functionality - optimized version
# Compatible with older Perl versions

# Main banner display functions - public interface
sub banne2 {
    my ($ancho, $dbh, $revi, $idioma) = @_;
    return _display_banner($ancho, $dbh, $revi, $idioma, 2);
}

sub banne {
    my ($ancho, $dbh, $revi, $idioma) = @_;
    return _display_banner($ancho, $dbh, $revi, $idioma, 1);
}

# Internal optimized banner display function
sub _display_banner {
    my ($ancho, $dbh, $revi, $idioma, $config_id) = @_;
    
    # Basic parameter validation
    return unless defined $ancho && defined $dbh && defined $revi && defined $idioma;
    return unless $config_id == 1 || $config_id == 2;
    
    # Get banner configuration
    my $bandera = _get_banner_flag($dbh, $config_id);
    return unless defined $bandera;
    
    # Build appropriate query based on config_id
    my $sql;
    my @params;
    
    if ($config_id == 1) {
        # Original banne() logic
        $sql = "select *, B.ID as IDBAN from BANNERS as B, USUARIOS as U where (B.ANCHO=? or B.ANCHO=348) and B.ACTIVO=1 and B.CLIENTE=U.ID and B.VETAS=1 and (U.ACTIVO_REVISTA!=0 or U.REVISTA=? or U.ACTIVO_GUIA=? or U.ACTIVO=1) and B.BANDERA=? order by B.EXPO, B.ORDEN";
        @params = ($ancho, $revi->{MUEBLE}, $revi->{GUIA}, $bandera);
    } else {
        # Original banne2() logic  
        $sql = "select *, B.ID as IDBAN from BANNERS as B, USUARIOS as U where (B.ANCHO=?) and B.ACTIVO=1 and B.CLIENTE=U.ID and B.VETAS=1 and (U.ACTIVO_REVISTA!=0 or U.REVISTA=? or U.ACTIVO_GUIA!=0 or U.ACTIVO=1) and B.BANDERA=? order by B.EXPO, B.ORDEN";
        @params = ($ancho, $revi->{MUEBLE}, $bandera);
    }
    
    my $sth = $dbh->prepare($sql);
    return unless $sth;
    
    return unless $sth->execute(@params);
    
    my $banner = $sth->fetchrow_hashref;
    $sth->finish;
    
    my $new_flag = _toggle_flag($bandera);
    
    if ($banner) {
        # Found a banner - display it and update flag
        _update_banner_flag($dbh, $banner->{IDBAN}, $new_flag);
        _render_banner_html($banner, $idioma);
        
        # Update counters
        contarbanner($banner->{IDBAN}, $dbh);
        contar($banner->{CLIENTE}, "BANNERS_EXPO", $dbh);
    } else {
        # No banner found - toggle global flag and retry once
        _update_config_flag($dbh, $config_id, $new_flag);
        
        # Simple retry mechanism to prevent infinite recursion
        our $retry_flag;
        unless ($retry_flag) {
            $retry_flag = 1;
            _display_banner($ancho, $dbh, $revi, $idioma, $config_id);
            $retry_flag = 0;
        }
    }
}

# Internal helper functions

sub _get_banner_flag {
    my ($dbh, $config_id) = @_;
    
    my $sth = $dbh->prepare("select BANDERA from BANNERS_CONFIG where ID=?");
    return unless $sth;
    return unless $sth->execute($config_id);
    
    my $row = $sth->fetchrow_hashref;
    $sth->finish;
    
    return $row ? $row->{BANDERA} : undef;
}

sub _toggle_flag {
    my ($flag) = @_;
    return $flag ? 0 : 1;
}

sub _update_banner_flag {
    my ($dbh, $banner_id, $new_flag) = @_;
    
    my $sql = "update BANNERS set BANDERA=? where ID=?";
    $dbh->do($sql, undef, $new_flag, $banner_id);
}

sub _update_config_flag {
    my ($dbh, $config_id, $new_flag) = @_;
    
    my $sql = "update BANNERS_CONFIG set BANDERA=? where ID=?";
    $dbh->do($sql, undef, $new_flag, $config_id);
}

sub _render_banner_html {
    my ($banner, $idioma) = @_;
    
    if ($banner->{ENLACE} eq "") {
        print qq(<a href="empresa.cgi?cliente=$banner->{CLIENTE}&i=$idioma&c=BANNERS_CLICKS&utm_source=web&utm_medium=banner&utm_campaign=$banner->{EMPRESA}"><img src="../banners/$banner->{ARCHIVO}" alt="$banner->{EMPRESA}" width="100%"></a><p>);
    } else {
        print qq(<a href="banner_ir.cgi?web=$banner->{ENLACE}&cliente=$banner->{CLIENTE}&i=$idioma&c=BANNERS_CLICKS"><img src="../banners/$banner->{ARCHIVO}" alt="$banner->{EMPRESA}" width="100%"></a><p>);
    }
}

sub contarbanner {
    my ($banner, $dbh) = @_;
    
    my $stm6 = $dbh->prepare("select * from BANNERS where ID=?");
    $stm6->execute($banner);
    
    if (my $a = $stm6->fetchrow_hashref) {
        my $cant = $a->{EXPO} + 1;
        $cant = 0 if ($cant >= 100);
        my $sql = "update BANNERS set EXPO=? where ID=?";
        $dbh->do($sql, undef, $cant, $a->{ID});
    }
    $stm6->finish;
}

sub contar {
    my ($cliente, $tipo, $dbh) = @_;
    
    # Declarar variables locales
    my ($stm6, $a, $cant, $sql);
    
    # Usar placeholders para evitar inyección SQL
    $stm6 = $dbh->prepare("select * from CONTA_CLIENTES where FECHA=CURRENT_DATE() and ID_CLIENTE=?");
    $stm6->execute($cliente);
    
    if ($a = $stm6->fetchrow_hashref) {
        # Usar $tipo en lugar de $accion (variable no definida)
        $cant = ($a->{$tipo} || 0) + 1;
        $sql = "update CONTA_CLIENTES set $tipo=? where ID=?";
        $dbh->do($sql, undef, $cant, $a->{ID});
    } else {
        $cant = 1;
        $dbh->do("insert into CONTA_CLIENTES(FECHA,ID_CLIENTE,$tipo) values (CURRENT_DATE(),?,?)", 
                 undef, $cliente, $cant);
    }
    
    # Logging de actividad - usando variables correctas y valores por defecto
    my $usuario = "9999";  # Usuario por defecto
    our %formulario;       # Acceso a variable global del formulario
    my $idioma = $formulario{i} || '';
    my $timezone = $ENV{timezone} || '';
    my $user_agent = $ENV{HTTP_USER_AGENT} || '';
    my $remote_addr = $ENV{REMOTE_ADDR} || '';
    
    # Insertar log de actividad con placeholders seguros
    $dbh->do("INSERT INTO CLIENTES_CONTADOR(ID_CLIENTE,FECHA,ACTIVIDAD,ID_USER,IDIOMA,TIMEZONE,HTTP_USER_AGENT,REMOTE_ADDR) VALUES (?,NOW(),?,?,?,?,?,?)", 
             undef, $cliente, $tipo, $usuario, $idioma, $timezone, $user_agent, $remote_addr);
    
    $stm6->finish;
}

1;