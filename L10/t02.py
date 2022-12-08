"""
-------------------------------------------------------
Lab 10, Task 2
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
from functions import customer_by_id

print("Find customer by id_number")

id_number = input("Enter an ID: ")

fh = open("customers.txt", 'r+', encoding="utf-8")

result = customer_by_id(fh, id_number)

fh.close()
print(result)
