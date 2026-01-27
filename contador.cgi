sub contar {
($cliente,$accion,$alpe)=@_;
use DBI;
$database="vetas_VETAS2";
$hostname="localhost";
$port="";
$driver = "mysql";
$dsn = "DBI:$driver:database=$database;host=$hostname;port=$port";
$dbh = DBI->connect($dsn, vetas_user, ghewrp54);
use Entrada;
&Entrada;


use CGI::Session;
use CGI;
my $cgi= new CGI;
my $session= new CGI::Session;
$session -> load();
my @autenticar = $session->param;


use ConectarDB;
$dbh=ConectarDB->connectWeb();

$usuario="9999";
if (@autenticar ne 0)
{ 
$u=$session->param("usuario");
#$stm42 = $dbh->prepare("select * from USER where USER='$u'");
#$stm42->execute();
#$user=$stm42->fetchrow_hashref;
$usuario=$u;
}


if ($ENV{'HTTP_USER_AGENT'} =~ /bot/  or $ENV{'HTTP_USER_AGENT'} =~ /spider/  or $ENV{'HTTP_USER_AGENT'} =~ /AhrefsBot/ or $ENV{'HTTP_USER_AGENT'} =~ /SemrushBot/ or $ENV{'HTTP_USER_AGENT'} =~ /crawl/ or $ENV{'HTTP_USER_AGENT'} =~ /slurp/ or $ENV{'HTTP_USER_AGENT'} =~ /mediapartners/ or $ENV{'HOST'} =~ /msnbot/)
{
}
else
{

$stm6 = $dbh->prepare("select * from CONTA_CLIENTES where FECHA=CURRENT_DATE() and ID_CLIENTE=$cliente");
$stm6->execute();
if ($a=$stm6->fetchrow_hashref)
	{
	$cant=$a->{$accion}+1;
	$sql = "update CONTA_CLIENTES set $accion='$cant' where ID = $a->{ID}";
	$dbh->do($sql);

	}
else
	{
	$cant=1;
	$dbh->do("insert into CONTA_CLIENTES(FECHA,ID_CLIENTE,$accion) values (CURRENT_DATE(),$cliente,'$cant')");
	}

fi;

$dbh->do("insert into CLIENTES_CONTADOR(ID_CLIENTE,FECHA,ACTIVIDAD,ID_USER,IDIOMA,TIMEZONE,HTTP_USER_AGENT,REMOTE_ADDR) values ('$cliente',now(),'$accion','$usuario','$formulario{i}','$ENV{timezone}','$ENV{HTTP_USER_AGENT}','$ENV{REMOTE_ADDR}')");
}




}
sub contarbanner {
($banner,$alpe)=@_;
use DBI;
$database="vetas_VETAS2";
$hostname="localhost";
$port="";
$driver = "mysql";
$dsn = "DBI:$driver:database=$database;host=$hostname;port=$port";
$dbh = DBI->connect($dsn, vetas_user, ghewrp54);
use Entrada;
&Entrada;

$stm6 = $dbh->prepare("select * from BANNERS where ID=$banner");
$stm6->execute();
if ($a=$stm6->fetchrow_hashref)
	{
	$cant=$a->{EXPOSICIONES}+1;
	$cant=0 if ($cant>10);
	$sql = "update BANNERS set EXPOSICIONES='$cant' where ID = $a->{ID}";
	$dbh->do($sql);
	}
fi;
$dbh->disconnect;
}
1;
