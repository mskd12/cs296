#!/bin/bash
inputfile=../data/g04_lab05data_random.csv
outputfile=../data/plot_data_random.dat
samplesize=15
rm -rf $outputfile

cat $inputfile | awk '
BEGIN {
        avg_step=0;
}
{       FS=",";

        avg_step+=$3;
        if (NR%'$samplesize'==0) {
                avg_step/='$samplesize';
                print avg_step;
                avg_step=0;
        }
}
' >> $outputfile
