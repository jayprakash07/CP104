"""
-------------------------------------------------------
Lab 10, Task 7
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
from functions import append_max_num

fileName = "numbers.txt"
fh = open(fileName, "r+", encoding="utf-8")

print("file 'numbers.txt' open for reading and writing")

num = append_max_num(fh)

fh.close()
print(f"{num} is appended")
