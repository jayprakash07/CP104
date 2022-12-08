"""
-------------------------------------------------------
Lab 8, Lists
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-11"
-------------------------------------------------------
"""
from random import randint


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    day = ["Sunday", "Monday", "Tuesday",
           "Wednesday", "Thursday", "Friday", "Saturday"]
    answer = day[d - 1]
    return answer


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    numbers = []
    i = 0
    while i < n:
        num = randint(low, high)
        if not (num in numbers):
            numbers.append(num)
            i += 1
    numbers.sort()

    return numbers


def linear_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns its index.
    User: index = linear_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        index - the index of the location of value in values,
            -1 if not found (int).
    -------------------------------------------------------
    """
    index = 0
    if not(value in values):
        index = -1
    else:
        while value != values[index]:
            index += 1

    return index


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    for x in range(0, len(source1)):
        target.append(source1[x] + source2[x])

    return target


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents
    of source1 and source2. Only elements that appear in both
    source1 and source2 appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    for element in source1:
        if element in source2:
            target.append(element)

    return target
