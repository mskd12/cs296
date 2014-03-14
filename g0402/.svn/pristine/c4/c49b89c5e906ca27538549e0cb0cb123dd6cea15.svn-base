#!/bin/bash
iterations=1500
reruns=150
randomsamples=15
inputfile=../data/g04_lab05data_02.csv
outputfile=../data/g04_lab05data_random.csv
rm -rf $outputfile
systemtime=`date +%s`;

cat $inputfile | awk '
{
	if (NR%'$reruns'==1) {
		#print "Generating new array"
		
		for (i=0;i<'$reruns';++i) {
			array[i]=0;
		}
		
		srand('$systemtime'+(10000*NR));
		NUM='$randomsamples';
		MIN=0;
		MAX='$reruns'-1;
		Number=0;
		
		while (Number < NUM) {
			r=int(((rand() *(1+MAX-MIN))+MIN));
			if (array[r]==0) {
			    Number++;
			    array[r]++;
			}
		}
	}
	#print NR%'$reruns';
	#print array[NR%'$reruns'];
	if (array[NR%'$reruns']) {
		print $0;
	}
}
' >> $outputfile
