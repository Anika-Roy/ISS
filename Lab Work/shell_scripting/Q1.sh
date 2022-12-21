#!/bin/bash

if [[ $# -ne 2 ]]
then 
    echo "Number of arguements don't match." ; exit
fi

echo "\`./run.sh\` $1 $2 gives output $(($1*$2))"

