"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""
# Imports
from random import randint


# Constants
SQFT_PER_AC = 43560


def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = (square_footage / SQFT_PER_AC)

    return acres


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """

    time = ((width * length) / speed)

    return time


def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = date_number % 10000
    datemonth = date_number // 10000
    month = datemonth % 100
    day = datemonth // 100

    return year, day, month


def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """

    numerator = (num1 * num2)
    denominator = (denom1 * denom2)
    product = (numerator / denominator)

    return numerator, denominator, product


def math_quiz():
    """
    -------------------------------------------------------
    Generates two random numbers and returns the sum to compare with the user's answer  
    Use: math_quiz():
    -------------------------------------------------------
    Parameters:
    num1 - Randomly generated number # 1
    num2 - Randomly generated number # 2
    Returns:
    rand_sum - The sum of the two randomly generated numbers
    """
    num1 = randint(0, 999)
    num2 = randint(0, 999)
    rand_sum = num1 + num2
    print(f"  {num1}")
    print("+", num2)
    answer = int(input("\nYour answer: "))
    print(f"\nYour Answer:    {answer}")
    print(f"Excepted:     {rand_sum}")
    return rand_sum
