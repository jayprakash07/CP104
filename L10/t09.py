"""
-------------------------------------------------------
Lab 10, Task 9
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
from functions import count_frequency_value

file = open("numbers.txt", "r+", encoding="utf-8")

print("file 'numbers.txt' open for reading")

value = int(input("Value to count: "))

result = count_frequency_value(file, value)

print(f"{value} appears {result} time(s)")

file.close()
