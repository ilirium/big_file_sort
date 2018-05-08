#!/usr/bin/env python
# coding: utf8
'''
Big File Sorter

Given a text file of integer numbers, return a sorted file of integers. The input file has a size bigger
then a RAM size. An output file has same format as the input file.

File format:
```
integer_as_string\n
integer_as_string\n
...
```

Sample of input data:
```
9
123987
2
```

Desired output (numerically sorted):
```
2
9
123987
```

Wrong output (lexicographically sorted):
```
123987
2
9
```


Usage: big_file_sort (input_file)
'''

# TODO:
#
# 1) I have two file_splitter functions. Develop class, super method file_splitter then inherit super method
#    and implement two realization of file_splitter.
# 2) What are right terms for:
#    (a) the super method (base class?),
#    (b) the inheritance operation of the super method,
#    (c) the implementation of inherited method.
# 3) Magic Number 16: describes by way of:
#    int_maxsize = 8 bytes (in text file),
#    sizeof_int_maxsize = 36 bytes,
#    36 / 8 = 4
# 4) Use class var (what right term?) to store `file_descriptors`
# 5) Analyze time, CPU and memory consumption.
#


import argparse
import math
import os
import os.path


class SorterBase:
    def _close_auxiliary_files(self, files_descriptors):
        for i in files_descriptors:
            i['file descriptor'].close()

        return True


class PreSorterInDrive(SorterBase):
    def __init__(self):
        self.files_descriptors = []

    def _calc_auxiliary_files_boundaries(self, input_filename):
        number_of_auxiliary_files = self._calc_number_of_auxiliary_files(input_filename)
        maxint_value = self._calc_maxint_value()

        boundaries = []
        segment_length = int(math.ceil(maxint_value / number_of_auxiliary_files))
        for i in range(1, number_of_auxiliary_files + 1):
            boundaries.append(i * segment_length)

        return boundaries

    def _calc_block_size_gb(self):
        """
        The programme sorts the big text file which size more then RAM. The file is read by blocks. So, we should define
        the right size of block. My laptop has 16 GB, so I thought that 1 GB is normal. For 8 GB RAM it will be 512 MB. It
        looks good.

        :return:
         - `block_size_gb`: The input file reads by some parts, all parts are equal to `block_size_gb`.
        """

        ram_size_gb = self._get_ram_size_gb_unix()

        magic_constant = 16.0

        block_size_gb = ram_size_gb / magic_constant

        return block_size_gb

    def _calc_input_file_size_gb(self, input_filename):
        input_file_size_bytes = os.stat(input_filename).st_size
        factor_bytes_in_gbytes = 1024.0 * 1024.0 * 1024.0
        input_file_size_gbytes = input_file_size_bytes / factor_bytes_in_gbytes

        return input_file_size_gbytes

    def _calc_maxint_value(self):
        int_64bits = 64
        maxint_value = 2 ** (int_64bits - 1) - 1

        return maxint_value

    def _calc_number_of_auxiliary_files(self, input_filename):
        input_file_size_gbytes = self._calc_input_file_size_gb(input_filename)
        block_size_gb = self._calc_block_size_gb()

        number_of_auxiliary_files = int(math.ceil(input_file_size_gbytes / block_size_gb))

        return number_of_auxiliary_files

    def _choose_auxiliary_file_for_writing(self, integer, boundaries):
        for file_number, boundary in enumerate(boundaries):
            if integer < boundary:
                return file_number

        # when the integer is greater than the maxint_value, the integer is written to an additional auxiliary file
        file_number = len(boundaries) + 1

        return file_number

    def _create_auxiliary_files(self, input_filename):
        number_of_auxiliary_files = self._calc_number_of_auxiliary_files(input_filename)

        for i in range(0, number_of_auxiliary_files):
            new_filename = 'temp' + str(i)
            fd_write = open(new_filename, 'w')
            self.files_descriptors.append({'file name': new_filename, 'file descriptor': fd_write})

        return True

    def _get_sysconf(self):
        sysconf_names = os.sysconf_names

        sc_phys_pages = os.sysconf('SC_PHYS_PAGES')
        sc_pagesize = os.sysconf('SC_PAGESIZE')

        return sysconf_names, sc_phys_pages, sc_pagesize

    def _get_ram_size_gb_unix(self):
        sysconf_names, sc_phys_pages, sc_pagesize = self._get_sysconf()

        total_ram_bytes = sc_phys_pages * sc_pagesize
        factor_bytes_in_gbytes = 1024 * 1024 * 1024
        total_ram_gbytes = total_ram_bytes / factor_bytes_in_gbytes

        return total_ram_gbytes

    def _write_int_to_auxiliary_file(self, integer_as_str, files_descriptors, file_number):
        files_descriptors[file_number]['file descriptor'].write(integer_as_str)

        return True

    def file_splitter_str(self, input_filename):
        self._create_auxiliary_files(input_filename)
        boundaries = self._calc_auxiliary_files_boundaries(input_filename)

        progress_past = -1
        with open(input_filename, 'r') as file:
            for quantity, line in enumerate(file):
                file_number = self._choose_auxiliary_file_for_writing(int(line), boundaries)
                self._write_int_to_auxiliary_file(line, self.files_descriptors, file_number)
                progress = self._choose_auxiliary_file_for_writing(quantity, boundaries)
                if progress > progress_past:
                    print(progress)
                    progress_past = progress

        self._close_auxiliary_files(self.files_descriptors)

        return self.files_descriptors


class PreSorterInMemory(PreSorterInDrive):
    pass


class Sorter(SorterBase):
    def __init__(self):
        pass

    def _create_result_file(self, input_filename):
        i = 0
        fd = False
        filename = input_filename + '_sorted'

        while not fd:
            if not os.path.isfile(filename):
                fd = open(filename, 'w')
                result_file = {'file name': filename, 'file descriptor': fd}
            else:
                i += 1
                filename = input_filename + str(i) + '_sorted'

        return result_file

    def _del_auxiliary_files(self, files_descriptors):
        for i in files_descriptors:
            os.remove(i['file name'])

        return True

    def _open_auxiliary_files(self, files_descriptors):
        files_descriptors_for_reading = []
        for file in files_descriptors:
            fd_read = open(file['file name'], 'r')
            files_descriptors_for_reading.append({'file name': file['file name'],
                                                  'file descriptor': fd_read})

        return files_descriptors_for_reading

    def sorter(self, input_filename, files_descriptors):
        files_descriptors_for_reading = self._open_auxiliary_files(files_descriptors)
        result_file = self._create_result_file(input_filename)

        for file in files_descriptors_for_reading:
            integers = [int(line) for line in file['file descriptor'].readlines()]
            integers.sort()
            # BUGFIX: str(number) return the pure string without EOL symbol.
            # And when we write this list to file, all numbers will be written in one long line
            # So, we need to use '{0}\n'.format(number).
            integers = ['{0}\n'.format(number) for number in integers]
            result_file['file descriptor'].writelines(integers)
            print('Part "{0}" sorted'.format(file['file name']))

        self._close_auxiliary_files(files_descriptors_for_reading)
        self._del_auxiliary_files(files_descriptors_for_reading)
        result_file['file descriptor'].close()

        return True


class OptionalMethods:
    def calc_read_boundaries_gb(self, input_filename):
        input_file_size_gbytes = calc_input_file_size_gb(input_filename)
        block_size_gb = calc_block_size_gb()

        if input_file_size_gbytes > block_size_gb:
            number_of_temp_files = calc_number_of_auxiliary_files(input_filename)
            boundaries = []
            bound = 0
            for i in range(0, number_of_temp_files + 1):
                start_bound = bound
                end_bound = start_bound + block_size_gb
                bound += block_size_gb
                boundaries.append({'start': start_bound, 'end': end_bound})
        else:
            boundaries = [{'start': 0, 'end': block_size_gb}]

        return boundaries


def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument('file_of_integers')

    args = p.parse_args()

    return args


def main(input_filename):
    print('Reading...')
    pre_sort = PreSorterInDrive()
    files_descriptors = pre_sort.file_splitter_str(input_filename)

    print('Sorting...')
    sort = Sorter()
    sort.sorter(input_filename, files_descriptors)

    return True


def read_past_auxiliary_files():
    # TODO: magic number
    number_of_auxiliary_files = 20

    file_descriptors = []
    for i in range(0, number_of_auxiliary_files):
        new_filename = 'temp' + str(i)
        fd_write = None
        file_descriptors.append({'file name': new_filename, 'file descriptor': fd_write})

    return file_descriptors


def main_auxiliary_files_are_available(input_filename):
    print('Reading...')
    files_descriptors = read_past_auxiliary_files()

    print('Sorting...')
    sorter(input_filename, files_descriptors)


    return True


def test(input_filename):
    # print('Input File Name: {0}'.format(input_filename))
    # ram_size_gb = get_ram_size_gb_unix()
    # block_size_gb = calc_block_size_gb()
    # write_boundaries = calc_read_boundaries_gb(input_filename)
    #
    # print('RAM Size: {0} GB'.format(ram_size_gb))
    # print('Block Size: {0} GB'.format(block_size_gb))
    # print('Write Boundaries: {0}'.format(write_boundaries))
    #
    # maxint_value = calc_maxint_value()
    # print('Integer Maximum Value: {0}'.format(maxint_value))
    #
    # calc_auxiliary_files_boundaries(input_filename)

    # *** *** ***
    # *** Test auxiliary files creation and removing ***
    files_descriptors = create_auxiliary_files(input_filename)
    del_auxiliary_files(files_descriptors)

    return True


def test_class():
    reader = Reader()
    reader.file_splitter_str()
    obj = object()


if __name__ == '__main__':
    args = parse_args()
    input_filename = args.file_of_integers

    main(input_filename)
    # main_auxiliary_files_are_available(input_filename)

