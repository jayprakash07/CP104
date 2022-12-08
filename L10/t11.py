"""
-------------------------------------------------------
Lab 10, Task 11
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
from functions import find_longest

fileName = "words.txt"
fh = open(fileName, "r+", encoding="utf-8")

print("file 'words.txt' open for reading and writing")

word = find_longest(fh)

fh.close()
print(f"{word} is the last longest word")
