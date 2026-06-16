#!/usr/bin/env bash

sum1=0
sum2=0

for i in {1..10}; do
result=$(python benchmark.py)

d1=$(echo "$result" | cut -d';' -f1)
d2=$(echo "$result" | cut -d';' -f2)

sum1=$(awk -v a="$sum1" -v b="$d1" 'BEGIN {print a+b}')
sum2=$(awk -v a="$sum2" -v b="$d2" 'BEGIN {print a+b}')

done

avg1=$(awk -v s="$sum1" 'BEGIN {print s/10}')
avg2=$(awk -v s="$sum2" 'BEGIN {print s/10}')

echo "Average first transpile:  $avg1 ms"
echo "Average second transpile: $avg2 ms"
