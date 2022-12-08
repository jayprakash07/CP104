"""
-------------------------------------------------------
Lab 5, Functions with Decisions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-21"
-------------------------------------------------------
"""


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    ACCELER_DUE_TO_GRAVITY = 9.8
    weight = (mass * ACCELER_DUE_TO_GRAVITY)

    if weight >= 1000:
        message = "heavy"
    elif weight <= 10:
        message = "light"
    else:
        message = "average"

    return weight, message


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """

    # Calculations
    diffv1 = (((target - v1)**2)**1 / 2)
    diffv2 = (((target - v2)**2)**1 / 2)

    if diffv1 <= diffv2:
        result = v1
    else:
        result = v2

    return result


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if 0 < speed < 39:
        category = "Breeze"
    elif 39 <= speed <= 61:
        category = "Strong Wind"
    elif 62 <= speed <= 88:
        category = "Gale Winds"
    elif 89 <= speed <= 117:
        category = "Whole Gale"
    elif speed > 117:
        category = "Hurricane"
    else:
        category = "Unknown"

    return category


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Constants
    MINIMUM_YEARS = 5
    MINIMUM_SALARY = 30000

    # Inputs
    years = int(input("Years employed: "))
    if (MINIMUM_YEARS <= years):
        salary = int(input("Annual Salary: "))
        if(MINIMUM_SALARY <= salary):
            qualified = True
        else:
            qualified = False
    elif years < MINIMUM_YEARS:
        qualified = False

    return qualified


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER = 6.00
    WINGS = 8.00
    FRIES = 1.50
    SALAD = 2.00

    order = input("Order B - burger or W - wings: ")
    if order == "B":
        price = BURGER
    elif order == "W":
        price = WINGS

    combo = input("Make it a combo? (Y/N): ")

    if combo == "Y":
        side = input("Add F - fries or S - salad: ")
        if side == "F":
            price += FRIES
        elif side == "S":
            price += SALAD

    return price
