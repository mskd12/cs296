#!/bin/bash
inputfile=../data/g04_lab05data_02.csv
outputfile1=../data/plot_data02.dat
outputfile2=../data/plot_data_it58.dat
reruns=150
rm -rf $outputfile1 $outputfile2

cat $inputfile | awk '
BEGIN {
        avg_step=0;
}
{       FS=",";
        
        avg_step+=$3;
        if ($1 == 58) {
                print $3 >> "../data/plot_data_it58.dat";
        }
        if (NR%'$reruns'==0) {
                avg_step/='$reruns';
                print avg_step >> "../data/plot_data02.dat";
                avg_step=0;
        }
}
'
