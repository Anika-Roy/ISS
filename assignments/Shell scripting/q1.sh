#!/bin/bash

sed '/^$/d' quotes.txt > no_empty_lines.txt

awk '!a[$0]++' quotes.txt > no_duplicates.txt