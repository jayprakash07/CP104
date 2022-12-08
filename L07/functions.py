"""
-------------------------------------------------------
Lab 7, Functions
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-04"
-------------------------------------------------------
"""


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    percentage_formula = rate / 100

    while current < target:
        current = current + percentage_formula * current
        years = years + 1
    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    total = 0
    num_values = 0

    value = float(input("First positive value: "))
    minimum = value
    maximum = value

    while value >= 0:
        total = total + value
        value = float(input("Next positive value: "))
        num_values = num_values + 1
        average = total / num_values
        if value >= 0:
            if value < minimum:
                minimum = value
            else:
                maximum = value
    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    total = 0
    status = "Balanced"
    balance = available - total
    value = float(input("Enter an expense (0 to quit): $"))

    while value > 0:
        total = total + value
        value = float(input("Enter another expense (0 to quit): $"))
        balance = available - total
        if balance < 0:
            status = "Deficit"
        elif balance > 0:
            status = "Surplus"
        if available == balance or balance == 0:
            status
    return total, balance, status


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low} and {high}: "))

    while value > low or value < high:
        if value > high:
            print("Value entered is too high")
            value = int(input(f"Enter a value between {low} and {high}: "))
        elif value < low:
            print("Value entered is too low")
            value = int(input(f"Enter a value between {low} and {high}: "))
        else:
            break
    return value


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    employeeID = int(input("Employee ID: "))
    total = 0
    employees = 0
    OVERTIME = 40
    OVERTIME_RATE = 1.5
    TAX_RATE = 3.625
    while employeeID != 0:
        pay = 0
        wage = int(input("Hourly wage rate: "))
        hours = int(input("Hours worked: "))
        if hours > OVERTIME:
            pay = (OVERTIME + (hours-OVERTIME)
                   * OVERTIME_RATE) * wage
        else:
            pay = hours * wage
        pay -= (pay * (TAX_RATE / 100))
        total += pay
        employees += 1
        print(f"Net payment for employee {employeeID}: ${pay:,.2f}")
        employeeID = int(input("\nEmployee ID: "))
        average = total / employees

    return total, average
