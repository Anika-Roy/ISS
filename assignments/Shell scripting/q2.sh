#!/bin/bash

#cat quotes.txt | sed 's/.~//' > authors.txt



while IFS= read -r line; do
    echo -n `cut -d "~" -f2- <<< "$line" `
    [[ ! -z  $line  ]] && echo -n " once said, \""
         
    
    echo -n `cut -d~ -f1 <<< "$line" `
    [[ ! -z  $line  ]] && echo -n "\"."  
    echo
done < quotes.txt > speech.txt