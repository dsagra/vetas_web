#!/usr/bin/perl
use cPanelUserConfig;
use CGI::Carp qw/fatalsToBrowser/;
use DBI;
use Entrada;
&Entrada;


$env="$ENV{REQUEST_URI}";
$envarreglado=$env; 

if ($env =~ m/2636+/) {
 exit;
}




use CGI::Session;
use CGI;
my $cgi= new CGI;
my $session= new CGI::Session;
$session -> load();
my @autenticar = $session->param;

use ConectarDB;
$dbh=ConectarDB->connectWeb();


require "contador.cgi";
if ($ENV{'HTTP_USER_AGENT'} =~ /bot/  or $ENV{'HTTP_USER_AGENT'} =~ /spider/  or $ENV{'HTTP_USER_AGENT'} =~ /AhrefsBot/ or $ENV{'HTTP_USER_AGENT'} =~ /SemrushBot/ or $ENV{'HTTP_USER_AGENT'} =~ /crawl/ or $ENV{'HTTP_USER_AGENT'} =~ /slurp/ or $ENV{'HTTP_USER_AGENT'} =~ /mediapartners/ or $ENV{'HOST'} =~ /msnbot/)
  {
  
  }
else
  {
  
&contar ($formulario{cliente},"$formulario{c}") if ($formulario{c} ne "") ;
&contar ($formulario{cliente},"VISITAS");

use Socket;
$hostname = gethostbyaddr(inet_aton($ENV{REMOTE_ADDR}), AF_INET);
$dbh->do("insert into CONTA_CLIENTES_HTTP_REFERER (CLIENTE,HTTP_REFERER,FECHA,REMOTE_ADDR,HTTP_USER_AGENT,HTTP_HOST,REMOTE_HOST,REMOTE_USER,HOST) values ('$formulario{cliente}','$ENV{'HTTP_REFERER'}',now(),'$ENV{'REMOTE_ADDR'}','$ENV{'HTTP_USER_AGENT'}','$ENV{'HTTP_HOST'}','$ENV{'REMOTE_HOST'}','$ENV{'REMOTE_USER'}','$hostname')");
  }
  if ($formulario{p} != "")
    {
   $stm6 = $dbh->prepare("select * from PROMOCION where ID=$formulario{p}");
$stm6->execute();
if ($a=$stm6->fetchrow_hashref)
  {
    
  $sql = "update PROMOCION set FECHA=now() where ID = $a->{ID}";
  $dbh->do($sql);
}
    }

if($formulario{web}==1)
	{
	print "Location: http://$formulario{sitio} \n\n";	
&contar ($formulario{cliente},"WEB");
	}
    if ($formulario{inf}==1)
      {
        $dbh->do("insert into EMAILS_ENV_CLICK (FECHA,EMPRESA_EMAIL,EMPRESA,EMAIL_ENVIADO) values (now(),'$formulario{email}','$formulario{emailemp}','$formulario{cliente}')");
      }





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


$idioma="es";
$idioma=$formulario{i} if ($formulario{i} eq "br" or $formulario{i} eq "en" );



if ($idioma eq "es")
  {
$catalogoproducto="Ver catalogo"; 
$descidioma="DESCRIPT";
  $MENU="menu.html";
  $idi="SP";
  $irubro="RUBRO_ES";
  $idescript="DESCRIPT";
  $prodtxt="Productos";
  $desc="DESCRIPT";
  $desc2="DESCRIPT_2";
  $txtcontact="Contactar con la empresa";
  $txtenviar="Enviar un mensaje";
  $txtnot="Noticias";
  $txtvideos="Videos";
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=es/i=en/;
  $volver2=~s/i=es/i=br/;
  $ivideo="TITULO_SP";
  $txtempresa="Empresa";
$txtnombre="Nombre";
$txttel="Telefono";
$txtpais="Pais";
$txtconsulta="Consulta";
$txtenvi= "Enviar";
$tm="TITULO";
$cm="COPETE";
$ti="es";
 $mensajeenviado="Su mensaje fue enviado con exito!!!";
  }
if ($idioma eq "en")
  {
$videoproducto="See catalog";
$descidioma="DESCRIPT_EN";
$tm="TITULO_EN";
$cm="COPETE_EN";
  $MENU="menu_en.html";
  $idi="EN";
  $irubro="RUBRO_EN";
  $idescript="DESCRIPT_EN";
  $prodtxt="Products";
  $desc="DESCRIPT_EN";
  $desc2="DESCRIPT_2EN";
  $txtcontact="Contact the company";
  $txtenviar="Send a message";
  $txtnot="News";
  $txtvideos="Videos";
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=en/i=es/;
  $volver2=~s/i=en/i=br/;
  $ivideo="TITULO_EN";
  $txtempresa="Company";
$txtnombre="Name";
$txttel="Phone";
$txtpais="Country";
$txtconsulta="Inquiry";
$txtenvi= "Send";
$ti="en";
$mensajeenviado="Your email was send successfully!!!";
  }
if ($idioma eq "br")
  {
$videoproducto="Ver cat�logo";
$ti="br";
$descidioma="DESCRIPT_BR";
$tm="TITULO_BR";
$cm="COPETE_BR";
  $MENU="menu_br.html";
  $irubro="RUBRO_BR";
  $idescript="DESCRIPT_BR";
  $idi="BR";
  $prodtxt="Produtos";
  $desc="DESCRIPT_BR";
  $desc2="DESCRIPT_2BR";
  $txtcontact="Entre em contato com a empresa";
  $txtenviar="Enviar uma consulta";
  $txtnot="Novidades";
  $txtvideos="Videos";
  $volver="$envi";
  $volver2="$envi";
  $volver=~s/i=br/i=es/;
  $volver2=~s/i=br/i=en/;
  $ivideo="TITULO_BR";
  $txtempresa="Empresa";
$txtnombre="Nome";
$txttel="Telefono";
$txtpais="Pais";
$txtconsulta="Consulta";
$txtenvi= "Enviar";
$mensajeenviado="Seu email foi enviado com sucesso!!!";
  }
 

if ($formulario{enviarformulario} eq "SI")
  {
print "Content-Type: TEXT/HTML\n\n";
$ex="";
foreach (keys %{formulario}) {
if ($_ ne "cliente" and $_ ne "empresa" and $_ ne "email" and $_ ne "consulta" and $_ ne "telefono" and $_ ne "pais" and $_ ne "activo"and $_ ne "enviarformulario" and $_ ne "g-recaptcha-response" and $_ ne "activo" and $_ ne"i"and $_ ne"nombre")
{
$a=$_;
$a =~ tr/+/ /;
$a =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$ex=$ex." ". $a."=".$formulario{$_}."<br>";
}
    }


use CGI;
my $q = new CGI; 
$remoteip=$q->remote_host();
use Captcha::reCAPTCHA::V2;
    my $rc = Captcha::reCAPTCHA::V2->new;
 my $response = $formulario{'g-recaptcha-response'};
    my $result = $rc->verify('6LdMFXAUAAAAAPReeYuseJzEcE-IaKUijlVmZeU0',$response, $remoteip);


    # Check the result
  if ($result->{success}){
    # Good
$dbh->do("insert into EMAILSCLI(ID_CLIENTE,NOMBRE,EMPRESA,EMAIL,MENSAJE,TEL,PAIS,FECHA,ENVIO,CLIENTE,EXTRAS,CAPTCHA) values ('$formulario{cliente}','$formulario{nombre}','$formulario{empresa}','$formulario{email}','$formulario{consulta}','$formulario{telefono}','$formulario{pais}',now(),'n','$formulario{activo}','$ex','$result->{success}')");
&contar ($formulario{cliente},"EMAIL");
} else {
    # Bad -- get first error that was returned
    $error = $result->{error_codes}->[0];
}










#print qq(
#<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
#<script type="text/javascript">
#\$(document).ready(function() {
#    setTimeout(function() {
#        \$(".alert").fadeOut(2000);
#    },3000);
#});
#</script>
#);
print qq(

  <div  class="alert alert-success" role="alert">
  $mensajeenviado
</div>);
  }


$FOOTER="footer.html";
$FOOTER="footer_vacio.html" if ($formulario{nomenu}==1);
$MENU="menu_vacio.html" if ($formulario{nomenu}==1);




require "menu.cgi";

&menu($MENU);

if ($user->{ID}!=0){
  $us=$user->{ID};

}else{
  $us=0;
}
$dbh->do("insert into CLIENTES_ESTADISTICAS(CLIENTE,FECHA,ACTIVIDAD,ID_USER,IDIOMA,TIMEZONE,HTTP_USER_AGENT,REMOTE_ADDR) values ($formulario{cliente},now(),'VISITA','$us','$formulario{i}','$ENV{timezone}','$ENV{HTTP_USER_AGENT}','$ENV{REMOTE_ADDR}')");

$clienteactivo="NO";
$stm = $dbh->prepare("select * from USUARIOS where ID=$formulario{cliente}"); 
$stm->execute();
if ($cliente=$stm->fetchrow_hashref)
  {
    if ($cliente->{ACTIVO_REVISTA}!=0  or $cliente->{ACTIVO_GUIA}!=0 or $cliente->{ACTIVO}==1)
      {
      $clienteactivo="SI";
      }
  }
  $clienteactivo="SI" if ($formulario{v} == 1);
print qq(  <title>$cliente->{EMPRESA}</title>);


## COLOR DEL FONDO
$color="white";
$textColor="black";

print <<EOFHTML;

  <main role="main" style="background-color: $color">
    <!-- Main jumbotron for a primary marketing message or call to action -->
 <div class="container" >

EOFHTML

if ($clienteactivo eq "SI")
  {
    print qq(
       <div class="row">
 <div class="col-md-12">
      <p class="text-center"><img class="img-thumbnail center" width="174px" height="50px" src="https://www.vetas.com/clientes/logos/$cliente->{ID}.jpg" alt=""></p>
    </div>

    );


  $stm40=$dbh->prepare("SELECT * FROM VIDEOS WHERE CLIENTE=$cliente->{ID} and TIPO=0 and PORTADA=1"); 
       $stm40->execute();
if ($video=$stm40->fetchrow_hashref)
{
$videoportada=1;
}
else
{
$videoportada=0;
}






if ($videoportada==1){

print <<EOFHTML



  <div class="container">

         
            <div class="embed-responsive embed-responsive-16by9">
            
            
 <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/$video->{VIDEO}?playlist=$video->{VIDEO}&autoplay=0&controls=1&loop=0&start=$video->{VIDEO}&end=$video->{VIDEO}"  frameborder="0" allow="loop; accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            


</div></div>
EOFHTML

}
else
{
print <<EOFHTML;    
    </div>
      <div class="row">

          <div class="col-md-12">
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
EOFHTML
     $stm40=$dbh->prepare("SELECT *, F.ID as fot FROM FOTOS AS F WHERE F.CLIENTE=$cliente->{ID} and F.SLIDER=1 order by F.ID"); 
       $stm40->execute();
       $c=1;
while ($producto=$stm40->fetchrow_hashref)
    {
print qq(<div class="carousel-item active" data-duration="100">) if ($c==1);
print qq(<div class="carousel-item" data-duration="100">) if ($c>1);
$foto=$producto->{fot}.".jpg";
$foto=$producto->{ARCHIVO} if ($producto->{ARCHIVO} ne "");
print qq(
     <img class="d-block w-100" src="https://www.vetas.com/clientes/fotos/$foto" alt="First slide">
    </div>
     );
$c++;
}




print <<EOFHTML;  

  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<p>
          </div>

EOFHTML
}

}

print <<EOFHTML;  
 <div class="row">

    
  <div class="col-md-12">

                  <h3 class="text-left" style= "color:$textColor">$cliente->{EMPRESA}</h3>
EOFHTML

print qq(
  <div class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#"><span class="flag-icon flag-icon-es"></span> Espa�ol</a>
                    <div class="dropdown-menu">
            <a href="
$volver
            " class="dropdown-item"><span class="flag-icon flag-icon-us"></span> English</a>
            <a href="
$volver2
            " class="dropdown-item"><span class="flag-icon flag-icon-br"></span> Portugues</a>
          </div>
        </div>
) if ($formulario{nomenu}==1);
print qq(<p class="text-justify" style= "color:$textColor">$cliente->{$desc}</p>) if ($clienteactivo eq "SI");
print qq(<p class="text-justify"style= "color:$textColor">$cliente->{$desc2}</p>) if ($clienteactivo eq "SI");
print qq(<p class="text-justify"style= "color:$textColor">$cliente->{DESCRIPT} - <small>Text in original language</small></p>) if ($cliente->{$desc} eq "" and $clienteactivo eq "SI");


print <<EOFHTML;            
          </div>
            <div class="col-md-12">
                
EOFHTML
$orden="R.ID,F.FECHA";
$orden="ORDEN";
      $stm40=$dbh->prepare("SELECT *, F.ID as fot FROM FOTOS AS F, RUBROS_NUEVO AS R WHERE F.CLIENTE=$cliente->{ID} and F.RUBRO=R.ID and F.SLIDER<>1 and FOTODEFECTO<>1 and (F.FECHAVENCE='' or F.FECHAVENCE > now()) order by $orden"); 
       $stm40->execute();
       $a=0;
       $b=0;
while ($producto=$stm40->fetchrow_hashref and $clienteactivo eq "SI")
    {
      print qq(<h3 class="text-center border-bottom" style= "color:$textColor">$prodtxt</h3>) if ($b==0);
      $b=1;
$foto=$producto->{fot}.".jpg";
$foto=$producto->{ARCHIVO} if ($producto->{ARCHIVO} ne "");
$a++;
$des=$producto->{$idescript};




$cantidadColumnas=3;
$anchoColumna=4;


$des=$producto->{$descidioma} if ($des eq "");
    print qq(<div class="row">) if ($a==1);
      print qq(
<style>     
.card-block {max-height:300px;overflow:auto;}
</style>
           <div class="col-md-$anchoColumna">
              <div class="card mb-$anchoColumna shadow-sm">
<A href="javascript:window.open('https://www.vetas.com/producto.cgi?ID=$producto->{fot} &i=$formulario{i}','$des','toolbar=0,location=0,directories=0, status=0,menubar=0,scrollbars=0,resizable=0,width= screen.width,height=screen.height,top=0,left=0');" >
                <img class="card-img-top" src="https://www.vetas.com/clientes/fotos/$foto" alt="Card image cap"></a>
               
                <div class="card-body  card-block">);

print qq(                <b>$producto->{$irubro}</b><br>)  if ($producto->{$irubro});
print qq(
                  <p class="card-text">$formulario{producto} - $des</p>) if ($des ne "");
print qq(
                </div>);
if ($producto->{VIDEO} ne "")
{
$videoproducto="Ver video";
print qq(

  <div class="card-footer text-muted">
  <a href="https://www.youtube.com/watch?v=$producto->{VIDEO}" target="_blank" class="btn btn-primary">$videoproducto</a>
  </div>

); 


}
if ($producto->{CATALOGO} ne "")
{

print qq(

  <div class="card-footer text-muted">
  <a href="$producto->{CATALOGO}" target="_blank" class="btn btn-primary">$catalogoproducto</a>
  </div>

); 
}
print qq(
              </div>
            </div>

);
if ($a==$cantidadColumnas)
{
  print qq(</div>);
  $a=0;
}  
  
  

  }
  if ($a!=0)
    {
      print qq(</div>);
    }

print <<EOFHTML;

EOFHTML
$videook=0;
$videocont=0;
      $stm40=$dbh->prepare("SELECT * FROM VIDEOS WHERE CLIENTE=$cliente->{ID} and TIPO=0 and PORTADA=0"); 
       $stm40->execute();
while ($video=$stm40->fetchrow_hashref and $clienteactivo eq "SI")
    {
print qq(
               <div class="row">
                <div class="col-md-12">
              <h3 class="text-center border-bottom" style= "color:$textColor">$txtvideos</h3>
            </div>
            ) if ($videook==0);
$videook=1;
$descvideo=$video->{$ivideo};
$descvideo=$video->{TITULO_SP} if ($descvideo eq "");
print qq( <div class="col-md-3">
                    <div class="thumbnail">
                    <iframe width="100%" src="https://www.youtube.com/embed/$video->{VIDEO}" frameborder="0" allowfullscreen></iframe><p>$descvideo
                    </div></div>);
$videocont++;
$videocont=0 if ($videocont==4);
}
print qq(<div class="col-md-3"></div><div class="col-md-3"></div><div class="col-md-3"></div>) if ($videocont==1);
print qq(<div class="col-md-3"></div><div class="col-md-3"></div>) if ($videocont==2);
print qq(<div class="col-md-3"></div>) if ($videocont==3);
print qq(</div>) if ($videook==1);
$noticiasok=0;
$id=0;
$stm100 = $dbh->prepare("select  * from NOTAS where PUBLICADA=0 and ESPECIAL=0 and NOESP=0 and ID_CLIENTE=$cliente->{ID} ORDER BY FECHANOT desc,ID desc limit $id,10");
$stm100->execute();
$cont=0;

while ($noticias=$stm100->fetchrow_hashref and $clienteactivo eq "SI")
  {
	$t=$tm;
	$c=$cm;
	$t="TITULO" if ($noticias->{$t} eq "");
	$c="COPETE" if ($noticias->{$c} eq "");
   print qq(
   
    <div class="col-md-12">
                <h3 class="text-center border-bottom" style= "color:$textColor">$txtnot</h3>) if ($noticiasok==0);
   $noticiasok=1;
    $stm30 = $dbh->prepare("select  * from NOTAS_FOTOS where ID_NOTAS=$noticias->{ID} and SLIDER=0");
    $stm30->execute();
        $fot="https://www.vetas.com/notas/fotos/$noticias->{'ID'}_1.jpg";
        if ($foto=$stm30->fetchrow_hashref)
          {
          $fot="https://www.vetas.com/notas/fotos/$noticias->{ID}_$foto->{ID}_$foto->{FOTO}";
          }





print qq(
            <div class="card container">
   <div class="row ">
          <div class="col-md-4">
              <img src="$fot" class="img-fluid" alt="Responsive image">
          </div>
          <div class="col-md-8">
            <h4 >
                <a  href="noticias.cgi?i=$idioma&noticia=$noticias->{ID}">$noticias->{$t}</a>
              </h4>
              <div class="text-muted">$noticias->{FECHANOT}</div>
               <p>$noticias->{$c}</p>
               
          </div>
          </div>
          </div>
          <p>
        );
      }
      $txtcontact="Solicitar mas informacion" if ($cliente->{INF}==1);

print qq(</div>) if ($noticiasok==1);
      print <<EOFHTML;
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>
  jQuery(document).ready(function(){
  \$(".oculto").hide();              
    \$(".inf").click(function(){
          var nodo = \$(this).attr("href");  
 
          if (\$(nodo).is(":visible")){
               \$(nodo).hide();
               return false;
          }else{
        \$(".oculto").hide("slow");                             
        \$(nodo).fadeToggle("fast");
        return false;
          }
    });
}); 
</script>
               
            </div>
          </div>
      
    <div class="color1 col-md-12">
        <h4 class="text-center">$txtcontact</h4>
EOFHTML

        print qq(<a href="http://www.vetas.com/empresa.cgi?web=1&sitio=$cliente->{SITE}&cliente=$formulario{cliente}" target="_blank" class="btn btn-block btn-success"><span class="glyphicon glyphicon-globe"></span> $cliente->{SITE}</a>) if ($cliente->{SITE} ne "" and $clienteactivo eq "SI");
print qq(<a href="tel://$cliente->{TEL}" class="btn btn-block btn-success"><span class="glyphicon glyphicon-earphone"></span> $cliente->{TEL}</a>) if ($clienteactivo eq "SI");
print qq(<a href="https://api.whatsapp.com/send?phone=$cliente->{WHATSAPP}" class="btn btn-block btn-success"><span class="glyphicon glyphicon-earphone"></span><img src="whatsapp.png " width="30px"> Whatsapp</a>) if ($cliente->{WHATSAPP} ne "" and $clienteactivo eq "SI");


print qq(<a href="https://www.facebook.com/$cliente->{FACEBOOK}" target="_blank" class="btn btn-block btn-primary">Facebook</a>) if ($cliente->{FACEBOOK} ne "" and $clienteactivo eq "SI");
print qq(<a href="https://www.instagram.com/$cliente->{INSTAGRAM}" target="_blank" class="btn btn-block btn-info">Instagram</a>) if ($cliente->{INSTAGRAM} ne "" and $clienteactivo eq "SI");
print qq(<a href="https://www.youtube.com/$cliente->{YOUTUBE}" target="_blank" class="btn btn-block btn-danger">Youtube</a>) if ($cliente->{YOUTUBE} ne "" and $clienteactivo eq "SI");
print qq(<a href="https://www.linkedin.com/$cliente->{LINKEDIN}" target="_blank" class="btn btn-block btn-primary">Linkedin</a>) if ($cliente->{LINKEDIN} ne "" and $clienteactivo eq "SI");
print qq(<a href="https://www.tiktok.com/\@$cliente->{TIKTOK}" target="_blank" class="btn btn-block btn-primary">TikTok</a>) if ($cliente->{TIKTOK} ne "" and $clienteactivo eq "SI");
print qq(<a href="https://www.twitter.com/$cliente->{TWITTER}" target="_blank" class="btn btn-block btn-info">Twitter</a>) if ($cliente->{TWITTER} ne "" and $clienteactivo eq "SI");



$in="oculto";
$in="" if ($cliente->{INF}==1);
print qq(<a href="#mensaje" class="btn btn-block btn-warning inf "><span class="glyphicon glyphicon-envelope"></span> $txtenviar</a>) if ($cliente->{INF}!=1);
  print <<EOFHTML;
        

<script src="https://www.google.com/recaptcha/api.js" async defer></script>
<script>
       function onSubmit(token) {
         document.getElementById("frmmensaje").submit();
       }
     </script>

      <div id="mensaje" class="col-md-12 $in">
      <h5 class="center">$txtenviar</h5>
                <form class="form-horizontal" id="frmmensaje" method="POST"  action="empresa.cgi"  novalidate>

EOFHTML
print qq(
  $cliente->{EXTRAS}
) ;
  print <<EOFHTML;
        <div class="form-group">
          <label for="email" class="control-label col-md-3">Email:</label>
          <div class="col-md-12">
          <input type="email" class="form-control" name="email" id="email" placeholder="email" required>
          </div>
          <div class="invalid-feedback">Ingresar datos</div> 
        </div>
                <div class="form-group">
          <label for="empresa" class="control-label col-md-3">$txtempresa:</label>
          <div class="col-md-12">
          <input type="text" class="form-control" id="empresa" name="empresa" placeholder="Empresa" required>
          </div>
          <div class="invalid-feedback">Ingresar datos</div>
        </div>
        <div class="form-group">
          <label for="nombre" class="control-label col-md-3">$txtnombre:</label>
          <div class="col-md-12">
          <input type="text" class="form-control" id="nombre"  name="nombre" placeholder="Nombre" required>
          </div>
          <div class="invalid-feedback">Ingresar datos</div>
        </div>
        <div class="form-group">
          <label for="telefono" class="control-label col-md-3">$txttel:</label>
          <div class="col-md-12">
          <input type="text" class="form-control" id="telefono" name="telefono" placeholder="Telefono" required>
          </div>
          <div class="invalid-feedback">Ingresar datos</div>
        </div>
       <div class="form-group">
          <label for="pais" class="control-label col-md-3">$txtpais:</label>
          <div class="col-md-12">
                     <select name="pais" id="_ctl178__ctl30_DropDownCountry" class="form-control col-md-12" style="width:100%;">
      <option value="$formulario{pais}" selected>$formulario{pais}</option>
      <option value="Aden">Aden    </option>
      <option value="Afghanistan">Afghanistan    </option>
      <option value="Albania">Albania    </option>
      <option value="Algeria">Algeria    </option>
      <option value="American Samoa">American Samoa    </option>
      <option value="Andorra">Andorra    </option>
      <option value="Angola">Angola    </option>
      <option value="Anguilla">Anguilla    </option>
      <option value="Antarctica">Antarctica    </option>
      <option value="Antigua">Antigua    </option>
      <option value="Antigua and Barbuda">Antigua and Barbuda    </option>
      <option value="Argentina" >Argentina   </option>
      <option value="Armenia">Armenia    </option>
      <option value="Aruba">Aruba    </option>
      <option value="Ascension">Ascension    </option>
      <option value="Ashmore Islands">Ashmore Islands    </option>
      <option value="Australia">Australia    </option>
      <option value="Austria">Austria    </option>
      <option value="Azerbaijan">Azerbaijan    </option>
      <option value="Azores">Azores    </option>
      <option value="Bahamas">Bahamas    </option>
      <option value="Bahrain">Bahrain    </option>
      <option value="Baker Island">Baker Island    </option>
      <option value="Bangladesh">Bangladesh    </option>
      <option value="Barbados">Barbados    </option>
      <option value="Barbuda">Barbuda    </option>
      <option value="Belarus">Belarus    </option>
      <option value="Belgium">Belgium    </option>
      <option value="Belize">Belize    </option>
      <option value="Benin">Benin    </option>
      <option value="Bermuda">Bermuda    </option>
      <option value="Bhutan">Bhutan    </option>
      <option value="Bolivia">Bolivia    </option>
      <option value="Bosnia">Bosnia    </option>
      <option value="Bosnia and Herzegovina">Bosnia and Herzegovina    </option>
      <option value="Botswana">Botswana    </option>
      <option value="Bouvet Island">Bouvet Island    </option>
      <option value="Brazil">Brazil    </option>
      <option value="British Indian Ocean Territory">British Indian Ocean Territory    </option>
      <option value="British Virgin Islands">British Virgin Islands    </option>
      <option value="Brunei">Brunei    </option>
      <option value="Bulgaria">Bulgaria    </option>
      <option value="Burkina Faso">Burkina Faso    </option>
      <option value="Burma">Burma    </option>
      <option value="Burundi">Burundi    </option>
      <option value="Caicos Islands">Caicos Islands    </option>
      <option value="Cambodia">Cambodia    </option>
      <option value="Cameroon">Cameroon    </option>
      <option value="Canada">Canada    </option>
      <option value="Cape Verde">Cape Verde    </option>
      <option value="Cartier Islands">Cartier Islands    </option>
      <option value="Cayman Islands">Cayman Islands    </option>
      <option value="Central African Republic">Central African Republic    </option>
      <option value="Ceuta, Melilla">Ceuta, Melilla    </option>
      <option value="Chad">Chad    </option>
      <option value="Channel Islands">Channel Islands    </option>
      <option value="Chechnya">Chechnya    </option>
      <option value="Chile">Chile    </option>
      <option value="China">China    </option>
      <option value="Christmas Island">Christmas Island    </option>
      <option value="Cocos Islands">Cocos Islands    </option>
      <option value="Colombia">Colombia    </option>
      <option value="Comoros">Comoros    </option>
      <option value="Congo">Congo    </option>
      <option value="Cook Islands">Cook Islands    </option>
      <option value="Coral Sea Island">Coral Sea Island    </option>
      <option value="Corsica">Corsica    </option>
      <option value="Costa Rica">Costa Rica    </option>
      <option value="C&ocirc;te d Ivoire">C&ocirc;te d Ivoire </option>
      <option value="Croatia">Croatia    </option>
      <option value="Cuba">Cuba    </option>
      <option value="Curacao">Curacao    </option>
      <option value="Cyprus">Cyprus    </option>
      <option value="Czech Republic">Czech Republic    </option>
      <option value="Denmark">Denmark    </option>
      <option value="Diego Garcia">Diego Garcia    </option>
      <option value="Djibouti">Djibouti    </option>
      <option value="Dominica">Dominica    </option>
      <option value="Dominican Republic">Dominican Republic    </option>
      <option value="East Timor">East Timor    </option>
      <option value="Ecuador">Ecuador    </option>
      <option value="Egypt">Egypt    </option>
      <option value="El Salvador">El Salvador    </option>
      <option value="England">England    </option>
      <option value="Equatorial Guinea">Equatorial Guinea    </option>
      <option value="Eritrea">Eritrea    </option>
      <option value="Estonia">Estonia    </option>
      <option value="Ethiopia">Ethiopia    </option>
      <option value="Falkland Islands (Malvinas)">Falkland Islands (Malvinas)    </option>
      <option value="Far&ouml;e Islands">Far&ouml;e Islands </option>
      <option value="Fiji">Fiji    </option>
      <option value="Finland">Finland    </option>
      <option value="France">France    </option>
      <option value="French Guiana">French Guiana    </option>
      <option value="French Polynesia">French Polynesia    </option>
      <option value="Gabon">Gabon    </option>
      <option value="Gambia">Gambia    </option>
      <option value="Georgia">Georgia    </option>
      <option value="Germany">Germany    </option>
      <option value="Ghana">Ghana    </option>
      <option value="Gibraltar">Gibraltar    </option>
      <option value="Great Britain">Great Britain    </option>
      <option value="Greece">Greece    </option>
      <option value="Greenland">Greenland    </option>
      <option value="Grenada">Grenada    </option>
      <option value="Grenadines">Grenadines    </option>
      <option value="Guadeloupe">Guadeloupe    </option>
      <option value="Guam">Guam    </option>
      <option value="Guantanamo Bay">Guantanamo Bay    </option>
      <option value="Guatemala">Guatemala    </option>
      <option value="Guinea">Guinea    </option>
      <option value="Guinea-Bissau">Guinea-Bissau    </option>
      <option value="Guyana">Guyana    </option>
      <option value="Haiti">Haiti    </option>
      <option value="Heard Islands">Heard Islands    </option>
      <option value="Herzegovina">Herzegovina    </option>
      <option value="Honduras">Honduras    </option>
      <option value="Hong Kong">Hong Kong    </option>
      <option value="Howland Island">Howland Island    </option>
      <option value="Hungary">Hungary    </option>
      <option value="Iceland">Iceland    </option>
      <option value="India">India    </option>
      <option value="Indochina">Indochina    </option>
      <option value="Indonesia">Indonesia    </option>
      <option value="Iran">Iran    </option>
      <option value="Iraq">Iraq    </option>
      <option value="Ireland">Ireland    </option>
      <option value="Isle of Man">Isle of Man    </option>
      <option value="Israel">Israel    </option>
      <option value="Italy">Italy    </option>
      <option value="Jamaica">Jamaica    </option>
      <option value="Jan Mayen">Jan Mayen    </option>
      <option value="Japan">Japan    </option>
      <option value="Jarvis Island">Jarvis Island    </option>
      <option value="Johnston Atoll">Johnston Atoll    </option>
      <option value="Jordan">Jordan    </option>
      <option value="Kampachea">Kampachea    </option>
      <option value="Kazakhstan">Kazakhstan    </option>
      <option value="Kenya">Kenya    </option>
      <option value="Kingman Reef">Kingman Reef    </option>
      <option value="Kirghiz">Kirghiz    </option>
      <option value="Kirghizstan">Kirghizstan    </option>
      <option value="Kiribati">Kiribati    </option>
      <option value="Korea">Korea    </option>
      <option value="Kuwait">Kuwait    </option>
      <option value="Kyrgyzstan">Kyrgyzstan    </option>
      <option value="Laos">Laos    </option>
      <option value="Latvia">Latvia    </option>
      <option value="Lebanon">Lebanon    </option>
      <option value="Lesotho">Lesotho    </option>
      <option value="Liberia">Liberia    </option>
      <option value="Libya">Libya    </option>
      <option value="Liechtenstein">Liechtenstein    </option>
      <option value="Lithuania">Lithuania    </option>
      <option value="Luxembourg">Luxembourg    </option>
      <option value="Macao">Macao    </option>
      <option value="Macedonia">Macedonia    </option>
      <option value="Madagascar">Madagascar    </option>
      <option value="Madeira Island">Madeira Island    </option>
      <option value="Malawi">Malawi    </option>
      <option value="Malaysia">Malaysia    </option>
      <option value="Maldives">Maldives    </option>
      <option value="Mali">Mali    </option>
      <option value="Malta">Malta    </option>
      <option value="Marisat (Atlantic West)">Marisat (Atlantic West)    </option>
      <option value="Marisat (Atlantic)">Marisat (Atlantic)    </option>
      <option value="Marisat (Indian)">Marisat (Indian)    </option>
      <option value="Marisat (Pacific)">Marisat (Pacific)    </option>
      <option value="Marshall Islands">Marshall Islands    </option>
      <option value="Martinique">Martinique    </option>
      <option value="Mauritania">Mauritania    </option>
      <option value="Mauritius">Mauritius    </option>
      <option value="Mayotte">Mayotte    </option>
      <option value="McDonald Island">McDonald Island    </option>
      <option value="Mexico">Mexico    </option>
      <option value="Micronesia">Micronesia    </option>
      <option value="Midway Islands">Midway Islands    </option>
      <option value="Miquelon">Miquelon    </option>
      <option value="Moldova">Moldova    </option>
      <option value="Monaco">Monaco    </option>
      <option value="Mongolia">Mongolia    </option>
      <option value="Montenegro">Montenegro    </option>
      <option value="Montserrat">Montserrat    </option>
      <option value="Morocco">Morocco    </option>
      <option value="Mozambique">Mozambique    </option>
      <option value="Myanmar">Myanmar    </option>
      <option value="Namibia">Namibia    </option>
      <option value="Nauru">Nauru    </option>
      <option value="Nepal">Nepal    </option>
      <option value="Netherlands">Netherlands    </option>
      <option value="Netherlands Antilles">Netherlands Antilles    </option>
      <option value="Nevis">Nevis    </option>
      <option value="New Caledonia">New Caledonia    </option>
      <option value="New Zealand">New Zealand    </option>
      <option value="Nicaragua">Nicaragua    </option>
      <option value="Niger">Niger    </option>
      <option value="Nigeria">Nigeria    </option>
      <option value="Niue Island">Niue Island    </option>
      <option value="Norfolk Island">Norfolk Island    </option>
      <option value="North Korea">North Korea    </option>
      <option value="North Mariana Island">North Mariana Island    </option>
      <option value="Northern Cyprus">Northern Cyprus    </option>
      <option value="Norway">Norway    </option>
      <option value="Oman">Oman    </option>
      <option value="Pakistan">Pakistan    </option>
      <option value="Palau">Palau    </option>
      <option value="Panama">Panama    </option>
      <option value="Papua - New Guinea">Papua - New Guinea    </option>
      <option value="Paraguay">Paraguay    </option>
      <option value="Peru">Peru    </option>
      <option value="Philippines">Philippines    </option>
      <option value="Pitcairn Island">Pitcairn Island    </option>
      <option value="Pitcairn Islands, Henderson, Ducie et Oeno">Pitcairn Islands, Henderson, Ducie et Oeno    </option>
      <option value="Poland">Poland    </option>
      <option value="Portugal">Portugal    </option>
      <option value="Principe">Principe    </option>
      <option value="Puerto Rico">Puerto Rico    </option>
      <option value="Qatar">Qatar    </option>
      <option value="Reunion">Reunion    </option>
      <option value="Romania">Romania    </option>
      <option value="Russia">Russia    </option>
      <option value="Russian Federation">Russian Federation    </option>
      <option value="Rwanda">Rwanda    </option>
      <option value="Saipan">Saipan    </option>
      <option value="San Marino">San Marino    </option>
      <option value="Sanaa">Sanaa    </option>
      <option value="Sao Tome and Principe">Sao Tome and Principe    </option>
      <option value="Saudi Arabia">Saudi Arabia    </option>
      <option value="Scotland">Scotland    </option>
      <option value="Senegal">Senegal    </option>
      <option value="Serbia">Serbia    </option>
      <option value="Seychelles">Seychelles    </option>
      <option value="Sierra Leone">Sierra Leone    </option>
      <option value="Singapore">Singapore    </option>
      <option value="Slovakia">Slovakia    </option>
      <option value="Slovenia">Slovenia    </option>
      <option value="Solomon Islands">Solomon Islands    </option>
      <option value="Somalia">Somalia    </option>
      <option value="South Africa">South Africa    </option>
      <option value="South Georgia and the South Sandwich Islands">South Georgia and the South Sandwich Islands    </option>
      <option value="South Korea">South Korea    </option>
      <option value="Spain">Spain    </option>
      <option value="Sri Lanka">Sri Lanka    </option>
      <option value="St Christopher">St Christopher    </option>
      <option value="St Christopher (St Kitts) and Nevis">St Christopher (St Kitts) and Nevis    </option>
      <option value="St Eustatius">St Eustatius    </option>
      <option value="St Helena">St Helena    </option>
      <option value="St Lucia">St Lucia    </option>
      <option value="St Maarten">St Maarten    </option>
      <option value="St Pierre et Miquelon">St Pierre et Miquelon    </option>
      <option value="St Vincent and the Grenadines">St Vincent and the Grenadines    </option>
      <option value="Sudan">Sudan    </option>
      <option value="Suriname">Suriname    </option>
      <option value="Svalbard">Svalbard    </option>
      <option value="Swaziland">Swaziland    </option>
      <option value="Sweden">Sweden    </option>
      <option value="Switzerland">Switzerland    </option>
      <option value="Syria">Syria    </option>
      <option value="Tahiti">Tahiti    </option>
      <option value="Taiwan">Taiwan    </option>
      <option value="Tajikistan">Tajikistan    </option>
      <option value="Tanzania">Tanzania    </option>
      <option value="Tasmania">Tasmania    </option>
      <option value="Thailand">Thailand    </option>
      <option value="Tobago">Tobago    </option>
      <option value="Togo">Togo    </option>
      <option value="Tokelau">Tokelau    </option>
      <option value="Tokelau Islands">Tokelau Islands    </option>
      <option value="Tonga">Tonga    </option>
      <option value="Trinidad">Trinidad    </option>
      <option value="Trinidad and Tobago">Trinidad and Tobago    </option>
      <option value="Tristan da Cunha">Tristan da Cunha    </option>
      <option value="Trust Territories">Trust Territories    </option>
      <option value="Tunisia">Tunisia    </option>
      <option value="Turkey">Turkey    </option>
      <option value="Turkmenistan">Turkmenistan    </option>
      <option value="Turks and Caicos Islands">Turks and Caicos Islands    </option>
      <option value="Tuvalu">Tuvalu    </option>
      <option value="Uganda">Uganda    </option>
      <option value="Ukraine">Ukraine    </option>
      <option value="United Arab Emirates">United Arab Emirates    </option>
      <option value="United Kingdom">United Kingdom    </option>
      <option value="United States">United States  </option>
      <option value="Uruguay">Uruguay    </option>
      <option value="US Virgin Islands">US Virgin Islands    </option>
      <option value="Uzbekistan">Uzbekistan    </option>
      <option value="Vanuatu">Vanuatu    </option>
      <option value="Vatican City">Vatican City    </option>
      <option value="Venezuela">Venezuela    </option>
      <option value="Viet Nam">Viet Nam    </option>
      <option value="Ville dAvray">Ville dAvray    </option>
      <option value="Virgin Islands">Virgin Islands    </option>
      <option value="Wake Island">Wake Island    </option>
      <option value="Wallis and Futuna Islands">Wallis and Futuna Islands    </option>
      <option value="West Indies">West Indies    </option>
      <option value="Western Sahara">Western Sahara    </option>
      <option value="Western Samoa">Western Samoa    </option>
      <option value="Yemen">Yemen    </option>
      <option value="Yugoslavia">Yugoslavia    </option>
      <option value="Zaire">Zaire    </option>
      <option value="Zambia">Zambia    </option>
      <option value="Zimbabwe">Zimbabwe    </option>

                    </select>
          </div>
          <div class="invalid-feedback">Ingresar datos</div>
        </div>
        <div class="form-group">
          <label for="consulta" class="control-label col-md-3">$txtconsulta:</label>
          <div class="col-md-12">
          <textarea class="form-control"  rows="5"  id="consulta" name="consulta" placeholder="$txtconsulta..." required></textarea>
          </div>
          <div class="invalid-feedback">Ingresar datos</div>
        </div>
        <div class="form-group">
        <input type="hidden" id="cliente" name="cliente" value="$cliente->{ID}">
        <input type="hidden" id="i" name="i" value="$formulario{i}">
        <input type="hidden" id="nomenu" name="nomenu" value="$formulario{nomenu}">
        <input type="hidden" id="enviarformulario" name="enviarformulario" value="SI">
     
  <input type="hidden" id="activo" name="activo" value="$clienteactivo">




EOFHTML


  print <<EOFHTML; 

          </div>
                <div class="form-group">
                   <button class="g-recaptcha btn btn-info" data-sitekey="6LdMFXAUAAAAAB_UlEC3ioDMoEWycTTHiv4Zdavv" data-callback='onSubmit'  type="submit">$txtenvi</button>
            
                </div>

                    </form>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

             <script>
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';

  window.addEventListener('load', function() {
    var form = document.getElementById('frmmensaje');
    form.addEventListener('submit', function(event) {
      if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  }, false);
})();
</script>    
      </div>







<style>
       #map {
        height: 300px;
        width: 100%;
       }
    </style>
            
        <br>
<script type="text/javascript"     src="https://maps.google.com/maps/api/js?sensor=false"> </script>       
<script type="text/javascript"> 
  function initialize() { 
    var latlng = new google.maps.LatLng("$cliente->{LAT}","$cliente->{LON}"); 
    var myOptions = { 
      zoom: 15, 
      center: latlng, 
      mapTypeId: google.maps.MapTypeId.ROADMAP 
    };
    var map = new google.maps.Map(document.getElementById("map"),myOptions); 
  
var marker = new google.maps.Marker({ 
      position: latlng,  
      map: map,  
      title:"$cliente->{EMPRESA}" 
  });   
}
 
</script> 
EOFHTML

print qq(<div class="mapouter"><div class="gmap_canvas"><iframe width="100%" height="355" id="gmap_canvas" src="https://maps.google.com/maps?q=$cliente->{LAT},$cliente->{LON}&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe></div><style>.mapouter{text-align:right;height:355px;width:100%;}.gmap_canvas {overflow:hidden;background:none!important;height:355px;width:100%;}</style></div>) if ($cliente->{LAT} ne "" and $clienteactivo eq "SI");


print qq(
      <br>
      <div class="text-center">
        <p><a href="https://www.google.com/maps/dir//$cliente->{LAT},$cliente->{LON}/\@$cliente->{LAT},$cliente->{LON},17z">$cliente->{DIRE} - ($cliente->{CPOSTAL}) $cliente->{CIUDAD} - $cliente->{PROV} - $cliente->{PAIS}</a></p>
      </div>
      ) if ($cliente->{DIRE} ne "" and $clienteactivo eq "SI");

  print <<EOFHTML;       
      <br>
      </div>  




      </div>


EOFHTML

$stm20 = $dbh->prepare("select * from USUARIOS as U, DISTRIBUIDORES AS D, DISTRIBUIDORES_TIPO AS T where D.ID_CLIENTE=$formulario{cliente} and D.ID_CLIENTE_DIST=U.ID and D.TIPO_DISTRIBUIDOR=T.ID"); 
$stm20->execute();
$a=0;
$b=0;
while ($dist=$stm20->fetchrow_hashref)
  {
print qq(<div class="col-md-12">) if ($b==0);
                
$prodtxtsuc="Locaciones" if ($idioma eq "es");
$prodtxtsuc="Locations" if ($idioma eq "en");
$prodtxtsuc="Localiza��es" if ($idioma eq "br");

     
      print qq(<h3 class="text-center border-bottom">$prodtxtsuc</h3>) if ($b==0);

      $b=1;
$foto=$producto->{fot}.".jpg";
$foto=$producto->{ARCHIVO} if ($producto->{ARCHIVO} ne "");
$a++;
$des=$producto->{$idescript};
$des=$producto->{$descidioma} if ($des eq "");
    print qq(<div class="row">) if ($a==1);
      print qq(
<style>     
.card-block {max-height:300px;overflow:auto;}
</style>
           <div class="col-md-3">
<div class="card-header">
<b>$dist->{PAIS}</b>
  </div>
              <div class="card mb-3 shadow-sm">
               
               
                <div class="card-body  ">
 <h5 class="card-title">$dist->{EMPRESA}</h5>

                
);
print qq(<a href="http://$dist->{SITE}" target="_blank" class="btn btn-block btn-success"><span class="glyphicon glyphicon-globe"></span> $dist->{SITE}</a>) if ($dist->{SITE} ne "" and $clienteactivo eq "SI");
print qq(<a href="mailto:$dist->{EMAIL}" target="_blank" class="btn btn-block btn-success"><span class="glyphicon glyphicon-globe"></span> $dist->{EMAIL}</a>) if ($dist->{EMAIL} ne "" and $clienteactivo eq "SI");

print qq(<a href="tel://$dist->{TEL}" class="btn btn-block btn-success"><span class="glyphicon glyphicon-earphone"></span> $dist->{TEL}</a>) if ($clienteactivo eq "SI");

print qq(
<style>
       #map {
        height: 200px;
        width: 100%;
       }
    </style>
            
        <br>
<script type="text/javascript"     src="https://maps.google.com/maps/api/js?sensor=false"> </script>       
<script type="text/javascript"> 
  function initialize() { 
    var latlng = new google.maps.LatLng("$dist->{LAT}","$dist->{LON}"); 
    var myOptions = { 
      zoom: 15, 
      center: latlng, 
      mapTypeId: google.maps.MapTypeId.ROADMAP 
    };
    var map = new google.maps.Map(document.getElementById("map"),myOptions); 
  
var marker = new google.maps.Marker({ 
      position: latlng,  
      map: map,  
      title:"$dist->{EMPRESA}" 
  });   
}
 
</script> 
);

print qq(<div class="mapouter"><div class="gmap_canvas"><iframe width="100%" height="200" id="gmap_canvas" src="https://maps.google.com/maps?q=$dist->{LAT},$dist->{LON}&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe></div><style>.mapouter{text-align:right;height:200px;width:100%;}.gmap_canvas {overflow:hidden;background:none!important;height:200px;width:100%;}</style></div>) if ($dist->{LAT} ne "" and $clienteactivo eq "SI");
print qq(
      <br>
      <div class="text-center">
        <p><a href="https://www.google.com/maps/dir//$dist->{LAT},$dist->{LON}/\@$dist->{LAT},$dist->{LON},17z">$dist->{DIRE} - ($dist->{CPOSTAL}) $dist->{CIUDAD} - $dist->{PROV} - $dist->{PAIS}</a></p>
      </div>
      ) if ($dist->{DIRE} ne "" and $clienteactivo eq "SI");
print qq(

                </div>
              </div>
            </div>

);
if ($a==4)
{
  print qq(</div>);
  $a=0;
}  
  
  

  }
  if ($a!=0)
    {
      print qq(</div>);
    }

print <<EOFHTML; 
  </div>
    <!-- /container -->
  </main>


 
EOFHTML


open FOOTER;
while (<FOOTER>) 
	{
	$linea = $_;
	print "$linea";
	}


#}
#else
#{

 # print "Location: login.cgi?premium=1&i=$idioma&&vol=$envarreglado\n\n";

#}
$dbh->disconnect;

