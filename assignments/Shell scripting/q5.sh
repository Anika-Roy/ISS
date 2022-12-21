#!/bin/bash

#printing entire string in reverse
read string
len=${#string}
#echo $len
for (( i=len-1 ; i>=0 ; i-- ))
do
    reverse+="${string[0]:i:1}"
done
echo $reverse

#replacing all letters by the next letter
temp=$(tr 'a-y' 'b-z'<<<"$reverse")
temp=$(tr 'z' 'a'<<<"$temp")
temp=$(tr 'A-Y' 'B-Z'<<<"$temp")
temp=$(tr 'Z' 'A'<<<"$temp")
echo $temp

#printing first half string in reverse
for (( i=(len/2)-1 ; i>=0 ; i-- ))
do
    echo -n "${string[0]:i:1}"
done
for (( i=(len/2) ; i<len ; i++ ))
do
    echo -n "${string[0]:i:1}"
done
echo


