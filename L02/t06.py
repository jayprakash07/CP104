"""
-------------------------------------------------------
Lab 2, Task 6
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-09-21"
-------------------------------------------------------
"""
principal = float(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
interest_rate = int(input("Yearly interest rate (%): "))

years_months = years * 12
years_percent = (interest_rate / 100) / 12

numerator = years_percent * ((1 + years_percent)**years_months)
denominator = ((1 + years_percent)**years_months) - 1
MONTHLY_PAYMENT = principal * (numerator / denominator)

print(f"\nThe monthly payments are: ${MONTHLY_PAYMENT}")
