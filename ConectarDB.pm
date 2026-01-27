#!/usr/bin/perl -w
package ConectarDB;
use strict;
use DBI;

my $database="VETAS";
my $hostname="10.0.0.3";
my $port="";
my $driver = "mysql";
my $dsn = "DBI:$driver:database=$database;host=$hostname;port=$port";

my $database2="vetas_VETAS2";
my $hostname2="localhost";
my $port2="";
my $driver2 = "mysql";
my $dsn2 = "DBI:$driver2:database=$database2;host=$hostname2;port=$port2";



sub connectLocal{
return (DBI->connect ($dsn, "root", "vetas",
{PrintError => 0, RaiseError => 1}));
}


sub connectWeb{
return (DBI->connect ($dsn2, "vetas_user", "ghewrp54",
{PrintError => 0, RaiseError => 1}));
}

1;


