#!/bin/bash

inputfile=../data/g04_lab05data_01.csv
outputfile=../data/plot_data.dat
reruns=150
rm -rf $outputfile

cat $inputfile | awk '
BEGIN {
	avg_step=0;
	avg_collision=0;
	avg_velocity=0;
	avg_position=0;
	avg_loop=0;
	mini="100";
	max=0;
	FS=",";
}
{	
	avg_step+=$3;
	avg_collision+=$4;
	avg_velocity+=$5;
	avg_position+=$6;
	avg_loop+=$7;
	#print mini;
	#print max;
	
	if (max < $3) max=$3;
	if (mini < $3) {$3=$3;}
	else {#print "crap";
	mini=$3;
	}
	#print mini;
	#print $3;
	if (NR%'$reruns'==0) {
                avg_step/='$reruns';
                avg_collision/='$reruns';
                avg_velocity/='$reruns';
                avg_position/='$reruns';
                avg_loop/='$reruns';
		printf avg_step;
		printf " ";
		printf avg_collision;
		printf " ";
		printf avg_velocity;
		printf " ";
		printf avg_position;
		printf " ";
		printf avg_loop;
		printf " ";
		printf mini;
		printf " ";
		print max;
		avg_step=0;
                avg_collision=0;
                avg_velocity=0;
                avg_position=0;
                avg_loop=0;
		mini=100;
		max=0;
	}
}
END {}
' >> $outputfile
