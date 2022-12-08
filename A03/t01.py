"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""
from functions import feet_to_acres

square_footage = int(input("Square footage: "))

acres = feet_to_acres(square_footage)

print(f"\n{acres:,.2f} acres is equivalent to {square_footage:,.2f} square feet")
