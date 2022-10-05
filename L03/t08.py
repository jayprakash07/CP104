"""
-------------------------------------------------------
Lab 3, Task 8
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-09-27"
-------------------------------------------------------
"""
amt_of_dirt = float(input("Enter amount of dirt (m^3): "))
amt_of_gravel = float(input("Enter amount of gravel (m^3): "))
amt_of_sand = float(input("Enter amount of sand (m^3): "))

total_amt = amt_of_dirt + amt_of_gravel + amt_of_sand

print("")
print("Material   Cubic Metres")
print(f"Dirt     {amt_of_dirt:>7.1f}")
print(f"Gravel   {amt_of_gravel:>7.1f}")
print(f"Sand     {amt_of_sand:>7.1f}")
print(f"Total    {total_amt:>7.1f}")
