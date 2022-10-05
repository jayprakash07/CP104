"""
-------------------------------------------------------
Lab 3, Task 14
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-09-30"
-------------------------------------------------------
"""
time = int(input("Enter number of minutes: "))

days = time / 1440
leftover_mins = time % 1440
hours = leftover_mins / 60
mins = time % 60

print(
    f"There are {days:.0f} days, {hours:.0f} hours, and {mins:.0f} minutes in {time} minutes")
