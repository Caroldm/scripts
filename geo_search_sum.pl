#!/usr/local/bin/perl
use Time::ParseDate;    # to parse dates
use POSIX qw(strftime); # to format dates

my ($year1, $month1, $day1) = (localtime)[5,4,3];   ###gets today date
$a = (($year1+1900)."/"."$month1". "/".($day1)."");
#print($a);

$b = (($year1+1900)."/"."$month1". "/".($day1-7)."");  ###gets date from -7days
#print($b);
#print ("'$a'[PDAT] : '$b'[PDAT]" );

print($a);
print($b);

#use strict;
use Data::Dumper;
use LWP::Simple;

#Add new platforms to list when they become supported
my $acc_list = 'GPL8321,GPL7091,GPL11383,GPL2902,GPL4044,GPL2700,GPL6887,GPL3084,
GPL16268,GPL13692,GPL2881,GPL2011,GPL94,GPL15207,GPL3697,GPL2006,GPL93,GPL92,GPL339,
GPL284,GPL6883,GPL17518,GPL887,GPL15401,GPL13712,GPL201,GPL1261,GPL10558,GPL6193,GPL6244,
GPL3050,GPL7430,GPL6101,GPL6885,GPL95,GPL4685,GPL2507,GPL3408,GPL44,GPL6102,GPL4200,
GPL6480,GPL6106,GPL7202,GPL4134,GPL1708,GPL3921,GPL85,GPL4074,GPL2897,GPL4133,GPL6947,
GPL10666,GPL1536,GPL1355,GPL11532,GPL4487,GPL80,GPL81,GPL6096,GPL8063,GPL737,GPL11202,
GPL16686,GPL15792,GPL6246,GPL340,GPL2895,GPL11180,GPL97,GPL13497,GPL571,GPL570';
my @acc_array = split(/,/, $acc_list);


#append [accn] field to each accession
for ($a=0; $a < @acc_array; $a++) {
   $acc_array[$a] .= "[ACCN]";
}

#join the accessions with OR
#my $query = join('+OR+',@acc_array);



#assemble the esearch URL with the desired time period, type of organism
my $base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/';
my $url = $base . 'esearch.fcgi?db=gds&term=$query+AND+homo sapiens[ORGN]+OR+
Mus musculus[ORGN]+OR+Rattus norvegicus[ORGN]+
AND+"2015/11/30"[PDAT] : "2015/12/7"[PDAT]&usehistory=y';

#post the esearch URL
my $output = get($url);

#parse WebEnv and QueryKey
$web = $1 if ($output =~ /<WebEnv>(\S+)<\/WebEnv>/);
$key = $1 if ($output =~ /<QueryKey>(\d+)<\/QueryKey>/);

### include this code for ESearch-ESummary
#assemble the esummary URL
$url = $base . "esummary.fcgi?db=$db&query_key=$key&WebEnv=$web";

#post the esummary URL
$docsums = get($url);
#print "$docsums";


#post the efetch URL
$data = get($url);
$dataout = getstore( $url, "geosummary1.txt")
#print "$data";

