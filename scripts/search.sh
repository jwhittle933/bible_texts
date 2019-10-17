#!/bin/bash

files=(*.txt)

for f in "${files[@]}"; do
	echo "$f"
done

function genesis() {
	grep "${1} " "~/text_search/Genesis.txt" 
}
