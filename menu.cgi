sub menu {
	($MENU,$alpe)=@_;
	use ConectarDB;
	$dbh=ConectarDB->connectWeb();
	open MENU;

$env="$ENV{REQUEST_URI}";
if ($env =~ m/i=/) {
    
}
else
  {
    if ($env =~ m/\?/) {
      $env=$env."&i=es";
    }
    else
      {
        $env=$env."?i=es";
      }
  
}

$envarreglado=$env; 

use CGI::Session;
use CGI;
my $cgi= new CGI;
my $session= new CGI::Session;
$session -> load();
my @autenticar = $session->param;
if (@autenticar ne 0)
{ 

}
else
{

$stm43 = $dbh->prepare("select * from RESTRINGIR where WEB='$env'");
$stm43->execute();
 if ($rest=$stm43->fetchrow_hashref)
	{
	print "Location: login.cgi?premium=1&i=$idioma&&vol=$envarreglado\n\n";
	}
}






print "Content-Type: TEXT/HTML\n\n";


while (<MENU>) 
  {
  $linea = $_;
  if (/<REVISTAVETAS>/)
    {
      print qq(maga.cgi?revista=$revi->{REVISTA}&indice=$revista->{INDICE}&paginas=$revista->{PAGINAS}&i=$idioma);
    }
  elsif (/<REVISTAMUEBLE>/)
    {
      print qq(maga.cgi?revista=$revi->{MUEBLE}&indice=$revista->{INDICE}&paginas=$revista->{PAGINAS}&i=$idioma);
    }
  elsif (/<VOLVER>/)
    {
      print qq($volver);
    }
  elsif (/<VOLVER2>/)
    {
      print qq($volver2);
    }
  elsif (/<REGISTRO>/)
    {


if (@autenticar ne 0)
{ 
$u=$session->param("usuario");
$stm42 = $dbh->prepare("select * from USER where USER='$u'");
$stm42->execute();
$user=$stm42->fetchrow_hashref;

print qq(<span class="text-white text-left">Bienvenido ),$user->{CONTACTO};
print qq( | <a href="privado.cgi?salir=1&i=$idioma" class="text-white text-left">Salir</a>);
}
else
{
# Temporalmente deshabilitado - no funciona
# print qq(
# <a class="text-white text-left"  href="https://www.vetas.com/registro.cgi?i=$idioma&&vol=$env">Registrese</a> | <a class="text-white text-right"  href="https://www.vetas.com/login.cgi?i=$idioma&&vol=$env">Ingrese</a>
# );
}
}


  else
    {
  print "$linea";
    }
  }
$dbh->disconnect;
}
1;
