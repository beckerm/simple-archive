#!/bin/bash

for DIR in $(cat dirs.dat); do
./archive_files.py -s $DIR -a /Users/larry/Desktop/archived_files -d 30
done

