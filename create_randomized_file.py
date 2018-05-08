#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import argparse
import random

def main(argv=None):
    parser = argparse.ArgumentParser(description='This program generates a file with random integer values without duplicates.')
    parser.add_argument('destination_file', type=str, help='The destination file which will be created')
    parser.add_argument('size', type=int, help='The max size of the file in megabyte')
    args = parser.parse_args()
    
    
    written_bytes = 0
    max_written_bytes = args.size * 1024 * 1024
    bin_size = sys.maxint / 1000
    next_numbers = {}
    for i in range(999):
        next_numbers[i] = bin_size * i
        
    destination_file = open(args.destination_file, 'w', 10000485) 
    while written_bytes < max_written_bytes:
        bin_no = random.randint(0, 998)
        current_no = str(next_numbers[bin_no])
        
        destination_file.write(current_no + "\n")
        written_bytes += len(current_no) + 1
        next_numbers[bin_no] += 1
    destination_file.close()


if __name__ == "__main__":
    sys.exit(main())
