#!/bin/bash

[ -z "$1" ] && echo -e "\t\033[0;31mError\033[m: Please supply a file to parse" && exit 0

file=$1
re_verse="^[0-9]+$"
current_chapter=0

while IFS= read -r line; do
	newline=""

	if [[ "${line:0:1}" =~ "@" ]]; then
		break
	fi

	if [[ "${line:0:1}" =~ "#" ]]; then
    current_chapter=$(echo $line | sed -e 's/:.*[0-9]//g' -e 's/[^0-9]//g' -e 's/ //g')
		continue
	fi

  line=$(echo "$current_chapter:1 $line")

	for value in $line; do
		if [[ $value =~ $re_verse ]]; then
			newline+=$(echo "\n$current_chapter:$value")
		else
			newline+=" $value"
		fi
	done
	echo -e $newline >> ../formatted/"$file"

done < "$file"
