"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-09-21"
-------------------------------------------------------
"""

prinicpal = float(input("Prinicpal: $"))
interest = float(input("Interest (Decimal): "))
n_of_years = int(input("Number of years: "))
interest_compounded = int(
    input("Number of times interest compounded per year: "))

brackets = (1 + (interest / interest_compounded))
result = (brackets)**interest_compounded
result = result**n_of_years
result = prinicpal * result

print(f"Balance: ${result}")
