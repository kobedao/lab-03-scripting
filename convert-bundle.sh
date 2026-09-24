#!/bin/bash
set -euo pipefail

curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

tar -xzvf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > output.csv

lines=$(wc -l < cleaned.tsv)

echo "$lines"

tar -czf converted-archive.tar.gz output.csv
