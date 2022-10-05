"""
-------------------------------------------------------
Lab 2, Task 7
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-09-21"
-------------------------------------------------------
"""
flyers = int(input("Number of flyers: "))
volunteers = int(input("Number of volunteers: "))

flyers_person = flyers // volunteers

print(f"\nFlyers per volunteer: {flyers_person}")

leftovers = flyers % volunteers

print(f"Flyers left over: {leftovers}")
