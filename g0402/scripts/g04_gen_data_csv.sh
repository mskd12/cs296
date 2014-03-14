#!/bin/bash

it_limit=1500
reruns=150
csvfile2=../data/g04_lab05data_02.csv
rm -rf $csvfile2

for i in $(seq 1 $it_limit)
do
        for j in $(seq 1 $reruns)
        do
		output=`../mybins/cs296_4_exe $i`
		echo -ne "$i," >> $csvfile2
		echo -ne "$j" >> $csvfile2

		echo "$output" | awk '
		{
                        if (NR == 1 || NR == 6) {
                        } else {
                                time=NF-1
                                printf "," $time >> "'$csvfile2'"
                        }
                
                }
		'
		echo >> $csvfile2
	done
done
