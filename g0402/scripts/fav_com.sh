#!/bin/bash

inputfile=~/.bash_history
com="`cat $inputfile | sort | uniq -c | sort -nrk 1 | sed -n 1,10p`"
echo "$com"
