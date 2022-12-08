"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""
from functions import date_extract

date = int(input("Enter a date in the format MMDDYYYY: "))

year, month, day = date_extract(date)

print(f"\nThe reformatted date: {year}/{month}/{day}")
