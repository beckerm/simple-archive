#!/bin/bash

for D in $(cat dirs.dat); do
./archive_cost_files.py -s $D -a /Users/larry/Desktop/archived_files -d 30
done

