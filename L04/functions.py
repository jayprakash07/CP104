"""
-------------------------------------------------------
Lab 4, Functions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
import math


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """

    diam = 2 * radius

    return diam


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """

    sh = math.sqrt((base / 2)**2 + float(height)**2)
    area = base**2 + 2 * base * math.sqrt(base**2 / 4 + float(height)**2)
    vol = base**2 * float(height) / 3

    return sh, area, vol


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    LOONIE = 1.00
    TOONIE = 2.00

    total = NICKEL * (nickels) + DIME * (dimes) + QUARTER * \
        (quarters) + LOONIE * (loonies) + TOONIE * (toonies)

    return total


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """
    SECONDSPERYEAR = 31536000
    SECONDSPERYEAR = SECONDSPERYEAR * years
    birthspyear = int(SECONDSPERYEAR / births)
    deathspyear = int(SECONDSPERYEAR / deaths)
    immigrantspyear = int(SECONDSPERYEAR / immigrants)
    new_size = int(size + birthspyear - deathspyear + immigrantspyear)
    return new_size


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    DAYS = 86400
    HOURS = 3600
    MINS = 60

    days = int(seconds // DAYS)
    hours = int(seconds // HOURS)
    mins = int(seconds // MINS)

    return days, hours, mins
