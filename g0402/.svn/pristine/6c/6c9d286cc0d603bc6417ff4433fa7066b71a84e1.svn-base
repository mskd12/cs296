#!/bin/bash

cpp_files=`ls ./src/* | grep .cpp`
if [ $1 == 1 ]; then

	for file in $cpp_files
	do
		mv $file $file.bak
	done
elif [ $1 == 2 ]; then
	cd ./src/
	find *.cpp -print0 | xargs -n 10 -0 -I {} mv {} {}.bak
	cd ../scripts/
fi

