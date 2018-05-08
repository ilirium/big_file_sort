#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import argparse


def load(file_name):
    with open(file_name) as f:
        string = f.read()

    array = [int(line) for line in string.split()]

    return array


def sort(array):
    array = sorted(array)

    return array


def save(file_name, array):
    with open(file_name, 'w') as f:
        for line in array:
            f.write(str(line)+'\n')

    return True


def main():
    args = parse_args()

    filename = args.file_of_integers
    sorted_filename = filename+'_sorted'
    array = load(filename)
    array = sort(array)
    save(sorted_filename, array)


def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument('file_of_integers')

    args = p.parse_args()
    return args

if __name__ == '__main__':
    sys.exit(main())

