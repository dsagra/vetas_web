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
	$sql = "update GUIA_CLIENTES_CLIRUB set CLASE='$formulario{$key}' where ID = $key";
	$dbh1->do($sql);
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
<tr><td>Gracias todo tus datos fueron completados con exito. <br>
Muchas gracias.<br><br>Cualquier duda nos comunicaremos con Usted.</td></tr>

EOFHTML



print "</form></table></td></tr></table></body>";


