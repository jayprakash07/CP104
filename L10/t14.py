"""
-------------------------------------------------------
Lab 10, Task 14
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
from functions import file_copy_n

fh = open("words.txt", "r+", encoding="utf-8")

fh2 = open("new_words.txt", "w+", encoding="utf-8")

print("Copying 'words.txt' to 'new_words.txt'")

number = int(input("Number of lines to copy: "))


file_copy_n(fh, fh2, number)

fh.close()
fh2.close()
