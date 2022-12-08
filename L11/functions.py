"""
-------------------------------------------------------
Lab 11, 2D-Arrays
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    for x in range(len(matrix[0])):
        print(f"{x:>7d}", end="")
    print()

    if (value_type == "float"):
        for i in range(len(matrix)):
            print(f"{i:>2.0f}", end="")
            for y in range(len(matrix[i])):
                answer = matrix[i][y]
                print(f"{answer:>7.2f}", end="")
            print()
    if (value_type == "int"):
        for i in range(len(matrix)):
            print(f"{i:>2d}", end="")
            for y in range(len(matrix[i])):
                answer = matrix[i][y]
                print(f"{answer:>7d}", end="")
            print()

    return None


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    string = " "
    for i in range(len(matrix[0])):
        print(f"{string}{i:>5d}", end="")
        string = ""
    print()
    for j in range(len(matrix)):
        print(f"{j:>2.0f}", end="")
        for y in range(len(matrix[j])):
            answer = matrix[j][y]
            print(f"{answer:>5s}", end="")
        print()

    return None


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    stat_list = []
    total = 0
    count = 0
    for i in matrix:
        for j in i:
            stat_list.append(j)

    stat_list.sort()
    min = stat_list[0]
    max = stat_list[-1]
    for k in stat_list:
        total += k
        count += 1
    average = total / count
    return min, max, total, average


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < matrix[min_x][min_y]:
                min_x = i
                min_y = j

            if matrix[i][j] > matrix[max_x][max_y]:
                max_x = i
                max_y = j

    return ([min_x, min_y], [max_x, max_y])


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    answer = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            answer[i][j] = matrix[j][i]
    return answer
