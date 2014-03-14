#!/bin/bash
thisfile="./scripts/myinfo.sh"

datediff2() {
        bdate=$1
        presentyear=`date +%Y`
        bdate=$presentyear$bdate
        btime=`date -d "$bdate" +%s`
        datenow=`date +%s`
        nextyear=$(($presentyear + 1))
        diff=$(($btime - $datenow))
        diffsec=0
        if [[ "$diff" -gt "0" ]]; then
                diffsec=$diff
        else
                bdate=`sed '{ s:'$presentyear':'$nextyear':g }' <<< $bdate`
                btime=`date -d "$bdate" +%s`
                diffsec=$(($btime - $datenow))
        fi
        tothr=$((diffsec/3600))
        totday=$((tothr/24))
        remhr=$((tothr%24))
        remday=$((totday%7))
        totweek=$((totday/7))
        echo -ne "There are "$totweek" weeks "$remday" days and "$remhr" hours left for the birthday of " 

}

echo "Today is "`date +%A`", "`date +%d`" "`date +%B`", "`date +%Y`"."

datediff2 "-11-07 00:00"
echo "Pratik Fegade"
datediff2 "-09-05 00:00"
echo "M.S.Krishna Deepak"
datediff2 "-08-17 00:00"
echo "P. Bharath Kumar"

echo "Thank you for asking, "`whoami`

file_out=`cat /proc/uptime`
timesec=`sed '{s/.[0-9]* [0-9]*.[0-9]*//g}' <<< $file_out`

totmin=$((timesec/60))
tothr=$((totmin/60))
remmin=$((totmin%60))
day=$((tothr/24))
remhr=$((tothr%24))

echo "Your system has been up for "$day" days, and "$remhr":"$remmin" hours."


diskstats=`df -T /`
echo "$diskstats" | awk '
BEGIN{
	FS=" "
}
{
	if ( NR == 2 ) {
		print "The current disk on which your home folder is located is "$1" and is "$6" % full.";
	}
}
'

#Disk usage and name remains

echo -ne "You are using"
osname=`lsb_release -i`
echo $osname | awk 'BEGIN{FS=":"}{printf $2}'
echo -ne " and"
versionno=`lsb_release -r`
echo $versionno | awk 'BEGIN{FS=":"}{printf $2}'
echo " with Kernal "`uname -r`

cat /proc/meminfo | awk '
BEGIN{
	FS=":"
	RAM=0
}
{
	if ( NR == 1 ) {
		RAM = $2;
		printf "Your machine has "RAM/1000000" GB RAM. Of which ";
	}
	else if ( NR == 2 ) {
		free = 100 * $2 / RAM;
		printf free;
		print " % is in use.";
	}
}
'


words=`wc -w $thisfile`
lines=`wc -l $thisfile`

a=`cat $thisfile | sed 's:[ \t]::g'`

nolines=`awk ' BEGIN{FS=" "}{printf $1}' <<< $lines`
#
chars=`echo "$a" | wc -m`
totchars=$((chars-nolines+1))

echo -ne "This script has "
awk ' BEGIN{FS=" "}{printf $1}' <<< $words
echo -ne " words, "
echo -ne $nolines
echo " lines and "$totchars" characters (without counting whitespace)"
