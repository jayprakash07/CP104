"""
-------------------------------------------------------
Assignment 4, Decisions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Returns the day of the week from input number
    Use: day_of_week()
    -------------------------------------------------------
    Parameters:
        day_number - number of the day in a week
    Returns:
        day of the week - ex. Monday, Tuesday (String)
    ------------------------------------------------------
    """
    if (day_number == 1):
        day = "Monday"

    elif (day_number == 2):
        day = "Tuesday"

    elif (day_number == 3):
        day = "Wednesday"

    elif (day_number == 4):
        day = "Thursday"

    elif (day_number == 5):
        day = "Friday"

    elif (day_number == 6):
        day = "Saturday"

    elif (day_number == 7):
        day = "Sunday"

    else:
        day = "Error"

    return day


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if (aqi >= 0) and (aqi <= 50):
        level = "Good"

    elif (aqi >= 51) and (aqi <= 100):
        level = "Moderate"

    elif (aqi >= 101) and (aqi <= 150):
        level = "Unhealthy for Sensitive Groups"

    elif (aqi >= 151) and (aqi <= 200):
        level = "Unhealthy"

    elif (aqi >= 201) and (aqi <= 300):
        level = "Very Unhealthy"

    elif (aqi > 300):
        level = "Hazardous"

    else:
        level = "Error"

    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    total_1 = (v1 * v2)
    total_2 = (v2 * v3)
    total_3 = (v1 * v3)

    if total_1 > total_2:
        result = total_1
    elif total_2 > total_3:
        result = total_2
    elif total_3 > total_1:
        result = total_3
    else:
        result = 0

    return result


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if (rgb1 == "red") and (rgb2 == "blue"):
        colour = "fuchsia"
    elif (rgb1 == "blue") and (rgb2 == "red"):
        colour = "fuchsia"
    elif (rgb1 == "red") and (rgb2 == "green"):
        colour = "yellow"
    elif (rgb1 == "green") and (rgb2 == "red"):
        colour = "yellow"
    elif (rgb1 == "green") and (rgb2 == "blue"):
        colour = "aqua"
    elif (rgb1 == "blue") and (rgb2 == "green"):
        colour = "aqua"
    elif rgb1 == "red" and rgb2 == "red":
        colour = "red"
    elif rgb1 == "blue" and rgb2 == "blue":
        colour = "blue"
    elif rgb1 == "green" and rgb2 == "green":
        colour = "green"
    else:
        colour = "Error"

    return colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Returns messages according to what condition it satisfies
    Use: message = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - any arbitrary integer
    Returns:
        message - according to the condition (str)
    -------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 == 0:
        message = "Yee Ha"
    elif number % 7 == 0:
        message = "Ha"
    elif number % 3 == 0:
        message = "Yee"
    else:
        message = "Nada"

    return message
