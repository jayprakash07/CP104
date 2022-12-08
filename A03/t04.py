"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""
from functions import multiply_fractions

num1 = int(input("Numerator 1: "))
denom1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
denom2 = int(input("Denominator 2: "))

numerator, denominator, product = multiply_fractions(
    num1, denom1, num2, denom2)

print(f"\nResult: {numerator}/{denominator} = {product}")
