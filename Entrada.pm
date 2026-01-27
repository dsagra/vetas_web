sub Entrada {
	my $entrada;

	if ($ENV{REQUEST_METHOD} eq "POST") {
		read(STDIN, $entrada, $ENV{CONTENT_LENGTH});
	}
	elsif ($ENV{REQUEST_METHOD} eq "GET") {
		$entrada = $ENV{QUERY_STRING};
	}
	else {
		$entrada = $ARGV[0];
	}

	my $clave, $valor;

	foreach(split(/\&/, $entrada)) {
		($clave, $valor) = split(/=/, $_);
		$valor =~ tr/+/ /;
		$valor =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$formulario{$clave} = $valor;
		
	}
}
1;