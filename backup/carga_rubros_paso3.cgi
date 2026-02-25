#!/usr/bin/perl
use cPanelUserConfig;
use Entrada;
&Entrada;

use DBI;
$database1="vetas_VETAS2";
$hostname1="webmail.vetas.com";
$port1="";
$driver1 = "mysql";
$dsn1 = "DBI:$driver1:database=$database1;host=$hostname1;port=$port1";
$dbh1 = DBI->connect ($dsn1, vetas_admin, 45104510);
print "Content-Type: TEXT/HTML\n\n";


@keys = keys %formulario;
foreach $key (sort(keys %formulario)) {
	if ($key != 'cliente' or $key != 'Submit')
		{ 
$dbh1->do("insert into GUIA_CLIENTES_CLIRUB(CLIENTE,RUBRO) values ('$formulario{cliente}',$key)");
		}
		}



print <<EOFHTML;
<head>
<title>Untitled Document</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css">
<!--
body {
	background-color: #000000;
}
-->
</style></head>
<body>
<table width="800">
<tr align="center"><td>
<img src="logoguia.jpg" width="800" height="166">
</td></tr><tr><td>
<table align="center" border="1" bgcolor="white" >
<form name="form1" method="post" action="carga_rubros_finalizar.cgi">

EOFHTML
print "<tr><td colspan=\"2\" align=\"center\"><b>Seleccione su categoria para cada uno de sus rubros</b></td></tr><tr bgcolor=\"green\"><td><font color=\"white\">CATEGORIA</td><td><font color=\"white\">RUBRO</font></td></tr>";
$stm0 = $dbh1->prepare("select *,C.ID as rubro from GUIA_CLIENTES_CLIRUB as C, RUBROS as R where C.CLIENTE=$formulario{cliente} and C.RUBRO=R.ID order by R.RUBRO_ES");
$stm0->execute();

while ($r=$stm0->fetchrow_hashref)
	{
	print "<tr><td> <select name=\"$r->{rubro}\"><option value=\"D\">Distribuidor</option>    <option value=\"I\">Importador</option>
    <option value=\"E\">Exportador</option>
    <option value=\"F\">Fabricante</option>
<option value=\"P\">Productor</option>
    <option value=\"R\">Representante</option></select></td><td>$r->{RUBRO_ES}</td></tr>";
	}

print "<tr><td align=\"center\" colspan=\"2\"><input type=\"submit\" name=\"Submit\" value=\"Finalizar\"></td></tr>";



print "</form></table></td></tr></table></body>";


