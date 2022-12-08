"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
number = int(input("Enter a positive digit number: "))


number1 = number % 10
number2 = number // 10
total = (number1 * number2)

print(f"\nThe product of the digits of {number:d} is {total:d}")
