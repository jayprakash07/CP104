"""
-------------------------------------------------------
Assignment 5, For-Loops
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-07"
-------------------------------------------------------
"""


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, num + 1):
        product = product * i

    return product


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Calculates and returns the number of calories burned in
    a specific duration of time.
    Use: calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - calories burned per minute
        minutes - total duration of minutes
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(5, minutes + 1, 5):
        CALORIES_BURNT = per_minute * i
        print(f"{i}: {CALORIES_BURNT:.1f}")
    return None


def open_triangle(num_rows):
    """
    --------------------------------------------------------
    Takes the user input of rows and returns a open triangle
    Use: open_triangle(number)
    --------------------------------------------------------
    Parameters:
        num_rows - the number of rows
    Returns:
        None
    --------------------------------------------------------
    """
    for i in range(num_rows):
        print("#" + (" " * i) + "#")

    return None


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    line = "-----" * (stop - start + 1)
    print("       ", end="")
    for i in range(start, stop + 1):
        print(f"{i:5d}", end="")
    print()
    print("      ", line)
    for j in range(start, stop + 1):
        print(f"{j:5d} |", end="")
        for k in range(start, stop + 1):
            print(f"{j*k:5d}", end="")
        print()

    return None


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, start + count * increment, increment):
        total += i

    return total
