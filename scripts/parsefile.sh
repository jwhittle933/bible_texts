#!/bin/bash

[ -z "$1" ] && echo -e "\033[0;31mError\033[m: Please supply a file to parse" && exit 0
[[ ! "${1##*.}" =~ "txt" ]] && echo -e "\033[0;33mWarning\033[m: parsefile only supports .txt" && exit 0

file=$1
re_verse="^[0-9a-z]+$"

while IFS= read -r line; do
	newline=""

	if [[ "${line:0:1}" =~ "@" ]]; then
		break
	fi

	if [[ "${line:0:1}" =~ "#" ]]; then
    current_chapter=$(echo $line | sed -e 's/[0-9].*[a-zA-Z]//g' -e 's/:.*[0-9]//g' -e 's/[^0-9]//g' -e 's/ //g')
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
