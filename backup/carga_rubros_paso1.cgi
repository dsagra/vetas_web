#!/usr/bin/perl
use cPanelUserConfig;
use DBI;

$database1="vetas_VETAS2";
$hostname1="webmail.vetas.com";
$port1="";
$driver1 = "mysql";
$dsn1 = "DBI:$driver1:database=$database1;host=$hostname1;port=$port1";
$dbh1 = DBI->connect ($dsn1, vetas_admin, 45104510);
print "Content-Type: TEXT/HTML\n\n";

$stm0 = $dbh1->prepare("select * from RUBROS order by CODIGO,RUBRO_ES");
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
</style>
<SCRIPT LANGUAGE="JavaScript">
function valida_envia(){ 
    if (document.formu.empresa.value.length==0){ 
       alert("Tiene que escribir su Empresa") 
       document.formu.empresa.focus() 
       return 0; 
    } 
  if (document.formu.email.value.length==0){ 
       alert("Tiene que escribir su E-mail") 
       document.formu.email.focus() 
       return 0; 
    } 
    if (document.formu.site.value.length==0){ 
       alert("Tiene que escribir su Web Site") 
       document.formu.site.focus() 
       return 0; 
    } 
    if (document.formu.pais.value.length==0){ 
       alert("Tiene que escribir su Pais") 
       document.formu.pais.focus() 
       return 0; 
    } 
    if (document.formu.cpostal.value.length==0){ 
       alert("Tiene que escribir su Codigo Postal") 
       document.formu.cpostal.focus() 
       return 0; 
    } 
    if (document.formu.prov.value.length==0){ 
       alert("Tiene que escribir su Provincia") 
       document.formu.prov.focus() 
       return 0; 
    } 
    if (document.formu.dire.value.length==0){ 
       alert("Tiene que escribir su Dirección") 
       document.formu.dire.focus() 
       return 0; 
    } 
    if (document.formu.ciudad.value.length==0){ 
       alert("Tiene que escribir su Ciudad") 
       document.formu.ciudad.focus() 
       return 0; 
    } 
    if (document.formu.tel.value.length==0){ 
       alert("Tiene que escribir su Telefono") 
       document.formu.tel.focus() 
       return 0; 
    } 
    if (document.formu.contacto.value.length==0){ 
       alert("Tiene que escribir el Contacto") 
       document.formu.contacto.focus() 
       return 0; 
    } 
document.formu.submit(); 
}
</SCRIPT>
</head>
<body>
<table width="800">
<tr align="center"><td>
<img src="logoguia.jpg" width="800" height="166">
</td></tr>
<tr align="center"><td>
<form name="formu" method="post" action="carga_rubros_paso2.cgi">
<table border="1" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF">
<tr><td colspan=\"4\" align=\"center\"><b>Complete los datos de su empresa para que figuren en la Guia Maderera</b></td></tr>
  <tr bgcolor="#003300">
    <td colspan="4">
    <div align="center"><b><font color="#FFFFFF">Datos de la Empresa</font></b></div></td>
  </tr>
  <tr>
    <td bgcolor="#CCCCCC"><i>Empresa</i></td>
    <td>
      <input type="text" name="empresa" size="30" maxlength="50">
    </td>
    <td bgcolor="#CCCCCC"><i>Provincia</i></td>
    <td>
      <input type="text" name="prov" size="20" maxlength="50">
    </td>
  </tr>
  <tr>
    <td bgcolor="#CCCCCC"><i>Direcci&oacute;n</i></td>
    <td>
      <input type="text" name="dire" size="30" maxlength="50">
    </td>
    <td bgcolor="#CCCCCC"><i>Cpostal</i></td>
    <td>
      <input type="text" name="cpostal" size="12" maxlength="10">
    </td>
  </tr>
  <tr>
    <td bgcolor="#CCCCCC"><i>Ciudad</i></td>
    <td>
      <input type="text" name="ciudad" size="20" maxlength="50">
    </td>
    <td bgcolor="#CCCCCC"><i>Pa&iacute;s</i></td>
    <td>
      <input type="text" name="pais" size="30" maxlength="50">
    </td>
  </tr>
  <tr>
    <td bgcolor="#CCCCCC"><i>Tel&eacute;fono</i></td>
    <td>
      <input type="text" name="tel" size="30" maxlength="50">
    </td>
    <td bgcolor="#CCCCCC"><i>E-mail</i></td>
    <td>
      <input type="text" name="email" size="30" maxlength="50">
    </td>
  </tr>
  <tr>
    <td bgcolor="#CCCCCC"><i>Fax</i></td>
    <td>
      <input type="text" name="fax" size="30" maxlength="50">
    </td>
    <td bgcolor="#CCCCCC"><i>Web Site</i></td>
    <td>
      <input type="text" name="site" size="30" maxlength="50">
    </td>
  </tr>
  <tr>
    <td bgcolor="#CCCCCC"><i>Contacto</i></td>
    <td>
      <input type="text" name="contacto" size="30" maxlength="50">
    </td>
    <td bgcolor="#CCCCCC"><i>Facebook</i></td>
    <td>
      <input type="text" name="facebook" size="30" maxlength="50">
    </td>
  </tr>
<tr>
    <td bgcolor="#CCCCCC"><i>Twitter</i></td>
    <td>
      <input type="text" name="twitter" size="30" maxlength="50">
    </td>
  </tr>
  <tr>
    <td bgcolor="#CCCCCC"></td>
    <td>

    </td>
  </tr>
  <tr>
    <td colspan="2"bgcolor="#CCCCCC"><i>Formato del Aviso</i></td>
    <td colspan="2">

<select name=\"AVISO\"><option value=\"UNA\">Una Pagina</option>    <option value=\"MEDIA\">Media Pagina</option>
    <option value=\"CUARTO\">Cuarto de Pagina</option>
    <option value=\"OCTAVO\">Octavo de Pagina</option>
<option value=\"DIECISEIS\">Dieciseis de Pagina</option>
    <option value=\"MENCION\">Mencion</option>
<option value=\"PROMOCION\">Promocion</option></select>

    </td>
  </tr>
<tr><td align="center" colspan="4"><input type="button" name="Submit" value="Paso 1/3 &gt;&gt;" onclick="valida_envia()"></td></tr>
</table>

</form>
</td></tr></table>
EOFHTML



