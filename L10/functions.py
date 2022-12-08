"""
-------------------------------------------------------
Lab 10, Files
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    this = fh.readline()
    result = []

    while result == [] and this != "":
        that = this.strip().split(",")
        if id_number in that:
            result = that
        else:
            this = fh.readline()

    return result


def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    num = 0
    line = fh.readline()

    while line != "":
        value = int(line)
        if value > num:
            num = value
        line = fh.readline()
    fh.write(f"\n{num}")

    return num


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    count = 0

    fh.seek(0)

    line = fh.readline()

    while line != "":

        if(int(line) == value):

            count += 1

        line = fh.readline()

    return count


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    currentWord = fh.readline().strip()

    while currentWord != '':
        secondWord = fh.readline().strip()

        if secondWord != '':
            if len(currentWord) > len(secondWord):
                currentWord = currentWord
            else:
                currentWord = secondWord
        else:
            break

    word = currentWord.strip()

    return word


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    count = 0

    fh_1.seek(0)
    line = fh_1.readline()

    while line != "" and count < n:
        print("{}".format(line), file=fh_2, end="")
        line = fh_1.readline()
        count += 1

    return None
