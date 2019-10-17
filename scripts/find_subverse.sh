#!/bin/bash

[ -z $1 ] && echo -e "\t\033[0;31mError\033[m: Please supply a value to search on" && exit 0
files=(*.txt)

for f in "${files[@]}"; do
  echo $(grep " a " $f) >> subverses.txt
done
