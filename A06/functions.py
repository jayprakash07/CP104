"""
-------------------------------------------------------
Assignment 6, While-Loops
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-14"
-------------------------------------------------------
"""


def winner():
    """
    -------------------------------------------------------
    Displays the wins of both teams.
    Use: result = winner()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        blue - # of wins (int)
        grey - # of wins (int)
    ------------------------------------------------------
    """
    blue = 0
    grey = 0

    while True:
        winning_team = input("Enter the winning team: ")
        if winning_team == 'blue':
            blue += 1
        elif winning_team == 'grey':
            grey += 1
        elif winning_team == '':
            break
    return blue, grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    low_prime = 2
    while num > low_prime:
        if num % low_prime == 0:
            prime = False
        low_prime += 1

    return prime


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    LINE = "-" * 34
    print(f"Principal: ${principal:.2f}")
    print(f"Interest Rate: {rate}%")
    print(f"Monthly Payment: ${payment:.2f}")
    print(LINE)
    print(f"Month Interest  Payment  Balance")
    print(LINE)

    month = 0
    balance = principal
    interest_per_month = rate / 12

    while balance > 0:
        month += 1
        interestAdded = balance * (interest_per_month / 100)
        balance += interestAdded

        if balance - payment < 0:
            payment = balance
            balance = 0
        else:
            balance -= payment
        print(f"{month:3d}  {interestAdded:9.2f} {payment:8.2f} {balance:10.2f}")

    return None


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    num = abs(num)
    count = 0
    if num == 0:
        count = 1
    while num != 0:
        num = num // 10
        count += 1

    return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    i = 1
    total = 0

    while i <= num + 1:
        if num % i == 0:
            total += i
        i += 1

    total = total - num

    return total
