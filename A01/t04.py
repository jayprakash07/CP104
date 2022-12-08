"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-09-12"
-------------------------------------------------------
"""

cost_pizza = float(input("Cost of 1 pizza slice: $"))
number_pizza = int(input("Number of pizza slices: "))
total_cost = cost_pizza * float(number_pizza)
print(
    f"\nTotal cost of {number_pizza} pizza slices: ${total_cost:.2f}")
