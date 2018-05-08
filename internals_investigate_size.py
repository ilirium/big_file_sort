#!/usr/bin/env python
# coding: utf8


import sys
import math


def get_maxsize_py3():
    """

    :return:
    """

    """An integer giving the maximum value a variable of type Py_ssize_t can take. It’s usually 2**31 - 1 on a 32-bit 
    platform and 2**63 - 1 on a 64-bit platform. """
    maxsize = sys.maxsize

    maxsize_number_of_bits = math.log2(maxsize+1)

    return maxsize, maxsize_number_of_bits


def get_sizeof_integers():
    """

    :return:
    """

    maxsize, maxsize_number_of_bits = get_maxsize_py3()
    sizeof_bytes_maxsize = sys.getsizeof(maxsize)
    sizeof_bytes_zero = sys.getsizeof(0)
    sizeof_bytes_one = sys.getsizeof(1)

    return sizeof_bytes_maxsize, sizeof_bytes_zero, sizeof_bytes_one


def get_int_info():
    """

    :return:
    """

    int_info = sys.int_info

    return int_info


if __name__ == '__main__':
    print('*** sys.maxsize ***')
    maxsize, maxsize_number_of_bits = get_maxsize_py3()
    print('maxsize = {0}'.format(maxsize))
    print('maxsize_number_of_bits = {0}'.format(maxsize_number_of_bits))
    print('\n')


    print('*** sys.getsizeof ***')
    sizeof_bytes_maxsize, sizeof_bytes_zero, sizeof_bytes_one = get_sizeof_integers()
    print('sizeof_bytes_maxsize = {0}'.format(sizeof_bytes_maxsize))
    print('sizeof_bytes_zero = {0}'.format(sizeof_bytes_zero))
    print('sizeof_bytes_one = {0}'.format(sizeof_bytes_one))
    print('\n')


    print('*** sys.int_info ***')
    int_info = get_int_info()
    print('int_info = {0}'.format(int_info))
    print('\n')