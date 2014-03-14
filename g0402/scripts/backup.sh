#!/bin/bash
# The path to backup folder is relative to pendrive
# The command should look like ./scripts/backup.sh backup
path=./src

var1=`dmesg | tail --lines=5 | grep 'sd.: sd..' | awk '
{
	printf $(NF)
}'`

var2=`df | grep "/dev/$var1" | awk '
{
	printf $(NF)
}'`

if [ "$var1" == "" ]
	then echo "Pendrive not inserted"
	else
	{
	if [ "$var2" == "" ]
		then #Case where pendrive is not mounted automatically
		{
		if [ ! -d ./pendrive ]
			then
			{
			mkdir -p pendrive
			sudo mount /dev/$var1 ./pendrive 
			}
		fi
		rsync -azvr $path ./pendrive/$1

		if [ -d ./pendrive ]
			then
			{
			sudo umount pendrive
			rm -R pendrive
			}
		fi
		}
		else
		{

		rsync -azvr $path "$var2/$1"
		}
	fi
	}
fi
