#!/usr/bin/env python
# coding: utf8

import sys


def maxvalue_for_maxsize():
    """
    Насколько большое число можно хранить в переменной с размером, соответствующим переменной со значениием sys.maxsize?
    How much can you store in a variable with a size corresponding to a variable with the sys.maxsize value?

    :return:
    """
    maxsize = sys.maxsize
    maxvalue = maxsize
    flag = True
    # while flag:
    #     maxvalue *= 2
    #     if sys.getsizeof(maxvalue) <= sys.getsizeof(maxsize):
    #         flag = False
    #         maxvalue /= 2

    while sys.getsizeof(maxvalue) <= sys.getsizeof(maxsize):
        maxvalue *= 2

    while sys.getsizeof(maxvalue) > sys.getsizeof(maxsize):
        maxvalue -= 10000000000000000000

    # while sys.getsizeof(maxvalue) <= sys.getsizeof(maxsize):
    #     maxvalue += 1

    return maxvalue


def print_maxvalue_for_maxsize():
    print('How much can you store in a variable with a size corresponding to a variable with the sys.maxsize value?')
    maxvalue = maxvalue_for_maxsize()
    maxsize = sys.maxsize
    print('maxsize = {}'.format(maxsize))
    print('maxvalue = {}'.format(maxvalue))

    return True


if __name__ == '__main__':
    int_maxsize_bytes = 8
    int_meansize_bytes = 4
    factor_bytes_in_gb = 1024 * 1024 * 1024
    file_size_gb = 20
    file_size_bytes = file_size_gb * factor_bytes_in_gb

    int_maxsize = 2**63 - 1
    print('int maxsize value = {0}'.format(int_maxsize))
    sizeof_int_maxsize = sys.getsizeof(int_maxsize)
    print('sizeof_int_maxsize = {0} bytes'.format(sizeof_int_maxsize))

    representing_maxsize_as_bits_size_in_gb = int_maxsize / 8 / factor_bytes_in_gb
    print('representing maxsize as bits size in gb = {0}'.format(representing_maxsize_as_bits_size_in_gb))

    print_maxvalue_for_maxsize()

    maxvalue_calculated = 1237940038570760549529812992


