#!/bin/bash

if [[ $1 == 1 ]]; then
	tar czf src.tar.gz src
elif [[ $1 == 2 ]]; then
	all_files=`ls ./src/`
	for file in $all_files
	do
		gzip ./src/$file
	done
	tar cf src.tar src 
fi
