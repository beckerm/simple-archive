#!/usr/bin/env python

 
import argparse
import sys, errno
import gzip
import datetime
import os
import time
import re


parser = argparse.ArgumentParser(description='Archive and move files (using gzip).')

parser.add_argument('-s', '--source', help='Source directory.', required=True)
parser.add_argument('-a', '--archive', help='Archive directory.', required=True)
parser.add_argument('-d', '--days', help='Days old.', type=int, required=True)
parser.add_argument('-r', '--regex', help='Regular expression.  Default = ".*"', default='.*')

args = parser.parse_args()

file_regex = re.compile(args.regex)
 
now   = time.time()
days_old = int(args.days)


def gzip_file(file_to_zip):
    zipped_file = file_to_zip + '.gz'
    try:
        with open(file_to_zip, 'rb') as f_in:   
            with gzip.open(zipped_file, 'wb') as f_out:
                f_out.writelines(f_in)
    except IOError as err:
        print('Error: ', err)
        pass
    finally:
        if os.path.exists(file_to_zip):
            try:
                os.remove(file_to_zip)
            except PermissionError as err:
                print('Error: ', err)
                pass
        return zipped_file


 
if os.path.exists(args.source):

    if os.path.exists(args.archive):

        for f in os.listdir(args.source):
            full_path = os.path.join(args.source,f)

            if os.path.isfile(full_path):

                if file_regex.search(f):

                    if os.stat(full_path).st_mtime < now - (days_old * 86400):
                        full_path_source_archived_file=gzip_file(full_path)
                        destination_archived_file = os.path.join(full_path_source_archived_file.split('/')[-1])
                        full_path_destination_archived_file = os.path.join(args.archive, destination_archived_file)
                        try:
                            os.rename(full_path_source_archived_file, full_path_destination_archived_file)
                        except PermissionError as err:
                            print('Error: ', err)
                            pass
    else:
        print('Invalid archive directory: ' + args.archive)
        exit(1)

else:
    print('Invalid source directory: ' + args.source)
    exit(1)



