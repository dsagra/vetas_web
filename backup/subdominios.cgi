#!/usr/bin/perl
use cPanelUserConfig;
use DBI;
use Entrada;
&Entrada;

$sitio=$formulario{url};

if ($sitio eq "alta")
	{
        print "Location: https://www.vetas.com/alta/cliente_alta.cgi?i=es\n\n";
	}
elsif ($sitio eq "guia")
        {
        print "Location: https://www.vetas.com/guia.cgi?i=es\n\n";
        }
elsif ($sitio eq "altaguia")
        {
        print "Location: https://www.vetas.com/guia/carga_rubros_paso1.cgi?i=es\n\n";
        }
elsif ($sitio eq "interguia")
        {
        print "Location: https://www.vetas.com/guia/solicita_info_guia.cgi?i=es\n\n";
        }
elsif ($sitio eq "interbr")
        {
        print "Location: https://www.vetas.com/guia/solicita_info_guia.cgi?i=br\n\n";
        }
elsif ($sitio eq "interar")
        {
        print "Location: https://www.vetas.com/guia/solicita_info_guia.cgi?i=ar\n\n";
        }

else
	{

$database2="vetas_VETAS2";
$hostname2="webmail.vetas.com";
$port2="";
$driver2 = "mysql";
$dsn2 = "DBI:$driver2:database=$database2;host=$hostname2;port=$port2";
$dbh2 = DBI->connect($dsn2, vetas_user, ghewrp54);

$stm6 = $dbh2->prepare("select ID,SUBDOMINIO from USUARIOS where SUBDOMINIO='$sitio'");
$stm6->execute();
if ($cl = $stm6->fetchrow_hashref) 
	{
        print "Location: https://www.vetas.com/empresa.cgi?i=es&cliente=$cl->{ID}&c=SUBDOMINIO\n\n";
        }
else
	{
        print "Location: https://www.vetas.com/\n\n";

	}
}

$dbh2->disconnect;