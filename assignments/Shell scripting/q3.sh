#!/bin/bash

#for printing file size
stat $1 | awk 'FNR == 2 {print $2}'

#for printing number of lines
cat $1 | wc -l

#for printing number of words
cat $1 | wc -w 

#for printing number of words per line
line_num=1
while read line;
do
echo -n "Line no: $line_num -Count of words:"
echo `echo $line | wc -w`
((line_num++))
done < $1

#repition frequency of words

while read line; do
    for word in $line; do
        freq=`cat $1 | grep -ow $word | wc -l`
        #echo "$freq"
        if (( $freq > 1 ))
        then echo "Word: $word - Count of repetition: `cat $1 | grep -ow $word | wc -l`"  >> temp.txt
        fi
    done
done <$1

awk '!a[$0]++' temp.txt 