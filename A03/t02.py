"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""
from functions import mow_lawn

width = int(input("Width (m): "))
length = int(input("Length (m): "))
speed = int(input("Speed (m^2/minute): "))

time = mow_lawn(width, length, speed)

print(f"\nMowing the lawn takes {time:.0f} minutes")
