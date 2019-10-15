#!/bin/bash

[ -z $1 ] && echo -e "\t\033[0;31mError\033[m: Please supply a file to parse" && exit 0

file=$1
newfile=$(pwd)/$1.temp

ch_line='[a-zA-Z]+'
re_number='^[0-9]+$'
final_line=$(tail -n 1 $file)

current_chapter=0

while IFS= read -r line || [[ -n $line ]]
do

	newline=""

	if [[ $line =~ $ch_line ]] 
	then
		current_chapter=$((current_chapter+1))
		continue
	fi

	if [[ ! $line =~ $ch_line ]]
	then
		line="${current_chapter}:1 ${line}"
	fi

	for value in $line
	do
		if [[ $value =~ $re_number ]]
	       	then
			newline+="\n${current_chapter}:${value}"
		else
			newline+=" $value"
		fi
	done
	echo -e $newline >> finals/$file

done < "$file"
