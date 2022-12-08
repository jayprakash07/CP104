"""
-------------------------------------------------------
Assignment 7, Lists
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-20"
-------------------------------------------------------
"""


def list_factors(num):
    """
    -------------------------------------------------------
    Returns a list of the factors that make up that number excepting
    the number itself.
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - an integer greater or equal to 0 (int)
    Returns:
        List - list of the factors (list of *)
    -------------------------------------------------------
    """
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    user_input = int(input("Enter an list of positive numbers: "))

    numbers = []
    while user_input != 0:
        if user_input > 0:
            numbers.append(user_input)
        else:
            user_input = user_input

        user_input = int(input("Enter a list of positive numbers: "))

    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    base_number = 0
    locations = []

    for i in values:
        if i == target:
            locations.append(base_number)
        base_number += 1
    return locations


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in subtrahend:
        while i in minuend:
            indexes = list_indexes(minuend, i)
            minuend.pop(indexes[0])

    return None


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = 0
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            in_order = False
    if in_order is False:
        index = 1
    else:
        index = -1

    return in_order, index
