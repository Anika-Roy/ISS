#!/bin/bash

cat $(find . -type f -name "*.txt") | grep -ow "Linux" | wc -l




