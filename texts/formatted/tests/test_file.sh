#!/usr/bin/env bats

@test "each line has chapter and verse" {
  re='^[0-9]([0-9]):[0-9]+'
  arr=()
  while IFS= read -r line; do
	arr=("$line", "${arr[@]}")		
  done < ../1Esdras.txt
  for line in $arr; do
     [ "$line" -eq "$re" ]	
  done
}
