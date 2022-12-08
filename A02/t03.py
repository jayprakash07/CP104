"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
date = int(input("Enter a date in the format DDMMYYYY: "))

year = date % 10000
datemonth = date // 10000
month = datemonth % 100
day = datemonth // 100

print(f"\nThe reformatted date: {year}/{month}/{day}")
