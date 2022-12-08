"""
-------------------------------------------------------
Lab 7, Task 8
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-04"
-------------------------------------------------------
"""
# Imports
from functions import budget

expenses, balance, status = budget(200)
print(f"({expenses:.2f}, {balance:.2f}, {status})")
