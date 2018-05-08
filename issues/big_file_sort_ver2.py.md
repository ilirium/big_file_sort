# Issues for `big_file_sort_ver2.py` project
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


## issue 005 at 2018-04-19, type: refactoring, status: open
[short name: learn objects and classes]
### Description

I have two file_splitter functions. Develop class, super method file_splitter then inherit super method and implement two realization of file_splitter. Use class var (what right term?) to store `file_descriptors`.

What are right terms for:
+ the super method (base class?),
+ the inheritance operation of the super method,
+ the implementation of inherited method,
+ class var.

### Comment 1 at 2018-05-09, status: open, need to test

Right terms are for:
+ the super method (base class?) = base class or super class;
+ class var = attribute.

Done:
+ Created 1 base classes: SorterBase.
+ Created 3 classes: PreSorterInDrive(SorterBase), Sorter(SorterBase) and OptionalMethods.
+ Moved all functions to these classes. Splitted methods to public and private.
+ Add one public attibute.
+ Revised the issue.md file. Splitted to several files and the original file was been kept as issues_old.md.

Next step:
+ Test this changes.
+ Implement the PreSorterInMemory(PreSorterInDrive) class.


