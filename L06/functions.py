"""
-------------------------------------------------------
Lab 6, For Loops
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-10-28"
-------------------------------------------------------
"""


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(1, num + 1, 2):
        total += i * (i % 2)
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for row in range(height):
        characters = 1 + row * 2
        for _ in range(1, height - row):
            print(" ", end="")
        print(characters * char)

    return None


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(n, 2, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer")
        print(
            f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        print("--")
    print("""2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall!
--
1 bottle of beer on the wall, 1 bottle of beer
Take one down, pass it around, no more bottles of beer on the wall!""")

    return None


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Task 11
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    sal = salary
    RETIREMENT = 65
    print(f"""Age         Salary 
------------------""")
    for year in range(0, RETIREMENT + 1 - age, 1):
        line = f"{age + year}      {sal:,.2f}"
        sal += sal * (increase / 100)
        print(line)

    return None


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    min_num = 0
    max_num = 0
    total = 0

    for i in range(n):
        prompt = " "
        if (i == 0):
            prompt = "First"
        else:
            prompt = "Next"

        value = float(input(f"{prompt} value:"))

        if(i == 0):
            min_num = value
            max_num = value
        else:
            if value < min_num:
                min_num = value
            if value > max_num:
                max_num = value

        total += value

    avgerage = total / n

    return min_num, max_num, total, avgerage
