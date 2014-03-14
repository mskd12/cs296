#!/bin/bash

dir=0
exe=0
files=0
path=0
all_exe=""

ls_out=`ls -bR $1`
OIFS=$IFS
IFS="	"
while read line
do
	if [[ $line =~ ^[./] ]]; then
		path=${line%?}
	elif [[ $line != "" ]]; then
		for names in $line
		do
			file_out=`file $path/$names`
			dir_grep=`echo $file_out | grep "directory"`
			exe_grep=`echo $file_out | grep "executable"`
			file_grep=`echo $file_out | grep "file"`
			if [[ $dir_grep != "" ]]; then
				dir=$(($dir + 1))
				#echo $path/$names
			elif [[ $exe_grep != "" ]]; then
				all_exe="$all_exe
$names"
				exe=$(($exe + 1))
				files=$(($files + 1))
			else
				files=$(($files + 1))
			fi
		done
	fi
done <<< "$ls_out"
IFS=$OIFS
echo "Number of directories: " $dir
echo "Number of files: " $files
echo "Number of executables: " $exe
echo "Executables: "
echo "$all_exe"
