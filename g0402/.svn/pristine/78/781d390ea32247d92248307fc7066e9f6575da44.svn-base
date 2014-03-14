#!/bin/bash
ps_out=` ps u -A | grep -v "grep" | grep "cs296_04_exe"`

curr_user=`whoami`
ps_user=`awk ' BEGIN{FS=" "} {printf $1}' <<< $ps_out`

echo ${#ps_out}
if [[ ${#ps_out} != 0 ]] && [ "$ps_user" == "$curr_user" ]; then
	echo 'The process cs296_04_exe is being run by you. Do you want kill the process?'
	read response
	if [ "$response" == "y" ]; then
		echo "Killing cs296_04_exe"
		ps_pid=`awk ' BEGIN{FS=" "} {printf $2}' <<< $ps_out`
		kill $ps_pid
		echo "Process killed"
	fi
elif [[ $ps_out != "" ]] && [[ $ps_user != $curr_user ]]; then
	echo "The process cs296_04_exe is being run by user "$ps_user". You do not have the privileges to kill this process."
else
	echo "The process cs296_04_exe is not being run."
fi
