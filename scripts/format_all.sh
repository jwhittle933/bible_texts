#!/bin/bash

files=(../texts/*.txt)

for f in $files; do
  parsefile "$f"
done
