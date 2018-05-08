#!/usr/bin/env python
# coding: utf8


import random
import os
import os.path


def generate_sample_lines():
    integers = []
    for i in range(0, 1000):
        number = random.randint(0, 998)
        integers.append(number)

    integers = ['{0}\n'.format(number) for number in integers]

    return integers


def check_existence_of_file(filename):
    if os.path.isfile(filename):
        existence = True
    else:
        existence = False

    return existence


def verify_that_file_does_not_exist(filename):
    if check_existence_of_file(filename):
        os.remove(filename)
        not_exist = True
    else:
        not_exist = True

    return not_exist


def write_lines(filename, list_of_str):
    if verify_that_file_does_not_exist(filename):
        fd = open(filename, 'w')
        fd.writelines(list_of_str)

    return True


def test_write_lines(filename):
    list_of_str = generate_sample_lines()
    write_lines(filename, list_of_str)

    return True


def main(filename):
    test_write_lines(filename)

    return True


def main_test():
    integers = generate_sample_lines()
    print('*** Integers\n{0}'.format(integers))


if __name__ == '__main__':
    filename = 'read_and_write_testing.txt'
    main(filename)
