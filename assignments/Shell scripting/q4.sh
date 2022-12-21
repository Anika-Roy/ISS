#!/bin/bash

read string
my_array=($(echo $string | tr "," "\n"))
#echo ${my_array[*]}

size=${#my_array[*]}
#echo "size=$size"

#echo $min

while (( size>0 ))
do
    min=${my_array[0]}
    index=0
    for (( i=0 ; i<$size ; i++))
    do
        if (( ${my_array[i]}<min ))
        then (( min=${my_array[i]} )) ; (( index=i ))
        fi   
    done
    echo -n "$min "
    #echo " "
    unset my_array[index]
    my_array=($(echo ${my_array[*]}))
    (( size-- ))
done
echo