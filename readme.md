# Several strategies for sorting a large file that does not fit in RAM

## Block-based reading and writing
Read a block of numbers from the file into memory and sort them into auxiliary lists. Write these auxiliary lists to corresponding temporary files. Repeat this read-and-write process until all numbers from the input file have been processed. Then, load each temporary file one by one, sort its contents, and append the sorted array of numbers to the output file.

### Pre-sorting
Sort the auxiliary list before writing it to a file.

This may speed up the subsequent sorting of the temporary file.

## Line-based reading and writing
Read line by line, write line by line.

## Line-based reading, block-based writing
Read line by line, write in blocks.
