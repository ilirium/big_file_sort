# Issues for `interview-avira` project


# big_file_sort.py

## The Program Description

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


## New Issues

+ add Unit Tests
+ investigate, how people do this, other software, common techinue
+ catch errors, exceptions, bullet proof (free space, file names etc)


## `[big_file_sort_ver2.py-005]` at 2018-04-19, type: refactoring, status: open

[short name: learn objects and classes]

### Description

I have two file_splitter functions. Develop class, super method file_splitter then inherit super method and implement two realization of file_splitter. Use class var (what right term?) to store `file_descriptors`.

What are right terms for:
+ the super method (base class?),
+ the inheritance operation of the super method,
+ the implementation of inherited method,
+ class var.


## `[big_file_sort_ver1.py-004]` at 2018-05-07, type: refactoring, status: fixed

### Description

Save current version from 2018-04-19 as the version 1 and save next version as the version 2.
Vesrion 1 file name is `big_file_sort_ver1.py`.
Version 2 file name is `big_file_sort_ver2.py`.


## `[big_file_sort_ver1.py-003]` at 2018-04-19, type: refactoring, status: transfered to version 2

[short name: learn objects and classes]

### Description

I have two file_splitter functions. Develop class, super method file_splitter then inherit super method and implement two realization of file_splitter. Use class var (what right term?) to store `file_descriptors`.

What are right terms for:
+ the super method (base class?),
+ the inheritance operation of the super method,
+ the implementation of inherited method,
+ class var.


## `[big_file_sort_ver1.py-002]` at 2018-04-19, type: bug, status: fixed

### Description

The result file contains one long line with all numbers without a delimitier.

### Comment 1 at 2018-04-19

The method `str(number)` returns the pure string without EOL symbol. And when we write this list to file, all numbers will be written in one long line So, we need to use '{0}\n'.format(number).

## `[big_file_sort_ver1.py-001]` at 2018-04-19, type: bug, status: fixed

### Description

Result file is not created. When the programm stopped, the error message show that the result file cannot be created. The programm is in an infinity loop.

### Comment 1 at 2018-04-19

Rewrite the `while` loop. Works well.

# `read_and_write_files.py`

## The Program Description

Write good and comfortable to reuse simple functions (methods) for reading and writing files.



