#!/usr/bin/perl
use cPanelUserConfig;
use DBI;

use Entrada;
&Entrada;

$database1="vetas_VETAS2";
$hostname1="webmail.vetas.com";
$port1="";
$driver1 = "mysql";
$dsn1 = "DBI:$driver1:database=$database1;host=$hostname1;port=$port1";
$dbh1 = DBI->connect ($dsn1, vetas_admin, 45104510);
print "Content-Type: TEXT/HTML\n\n";

$sql=qq(insert into GUIA_CLIENTES_ALTA(EMPRESA,DIRE,CIUDAD,TEL,FAX,CONTACTO,PROV,CPOSTAL,PAIS,EMAIL,WEB,AVISO,FECHA,FACEBOOK,TWITTER) values ("$formulario{empresa}","$formulario{dire}","$formulario{ciudad}","$formulario{tel}","$formulario{fax}","$formulario{contacto}","$formulario{prov}","$formulario{cpostal}","$formulario{pais}","$formulario{email}","$formulario{site}","$formulario{AVISO}",now(),"$formulario{facebook}","$formulario{twitter}")); 
$dbh1->do($sql);
$stm6 = $dbh1->prepare("select last_insert_id() as id from GUIA_CLIENTES_ALTA");
$stm6->execute();
$id=$stm6->fetchrow_hashref;

$stm0 = $dbh1->prepare("select * from RUBROS where SALE_EN_GUIA=1 order by CODIGO,RUBRO_ES");
$stm0->execute();
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
<img src="logoguia.jpg" width="800" height="166">
<table border="1" bgcolor="white" width="800">
<form name="form1" method="post" action="carga_rubros_paso3.cgi">
<tr><td colspan=\"2\" align=\"center\"><b>Seleccione los rubros que comercializa su empresa</b></td></tr>
EOFHTML

while ($r=$stm0->fetchrow_hashref)
	{
		 if ($r->{MARCA}==1)
			{
			$marca="Solo On-line";
			}
		else
			{
			$marca="Impreso y On-line";
			}
	if ($r->{"CODIGO"} =~ /000/)
		{
		print "<tr bgcolor=\"green\"><td></td><td><font color=\"white\">$r->{RUBRO_ES} - $marca</font></td></tr>";
		}
	elsif ($r->{"CODIGO"} =~ /00/)
		{
		print "<tr><td></td><td><b>$r->{RUBRO_ES} - $marca</b></td></tr>";
		}
	else 
		{

		print "<tr><td><input name=\"$r->{ID}\" type=\"checkbox\" id=\"$r->{ID}\" value=\"ok\"></td><td>$r->{RUBRO_ES} $r->{ID} - $marca</td></tr>";
		}
	fi;

	}
print "<tr><td align=\"center\" colspan=\"2\"><input name=\"cliente\" type=\"hidden\" value=\"$id->{id}\"><input type=\"submit\" name=\"Submit\" value=\"Paso 2/3 &gt;&gt;\"></td></tr>
</form></table>";


