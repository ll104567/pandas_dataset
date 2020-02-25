#!/bin/bash

cat step1-5.txt step6-10.txt |sed 's/<\/b>.*$//g'|sed 's/<code>//g'|sed 's/<\/code>//g' > step.txt
cat step.txt |sed 's/步骤1 /\n&/g'|awk 'BEGIN{a=1}/^$/{print "\n["a"]";a++}1' > step1-10.txt

echo "File:step.txt"
echo "Cleaned: step1-10.txt"
