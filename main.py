"""
Module for processing and analyzing data from a CSV file containing integer lists.

This module provides functionalities to:
- Read and parse a CSV file containing lists of integers.
- Access specific lists from the data by index.
- Retrieve the first or last list from the data.
- Perform basic operations such as finding the maximum, minimum, or sum of a list.

Example usage:
    Run the main() function to print and interact with the data from the specified CSV file.

"""

#### Imports et définition des variables globales

FILENAME = "listes.csv"

def read_data(filename):
    """Read and parse a CSV file containing integer lists.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of lists, where each inner list corresponds to a line in the file,
              and its elements are integers parsed from semicolon-separated values.
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as file:
        s = file.readlines()
        for line in s:
            l_prime = line.strip().split(';')
            l.append(list(map(int, l_prime)))

    print(l)
    return l

def get_list_k(data, k):
    """Retrieve the k-th list from the data.

    Args:
        data (list): The list of lists containing the data.
        k (int): The index of the list to retrieve.

    Returns:
        list: The k-th list in the data.
    """
    return data[k]

def get_first(l):
    """Retrieve the first list from the data.

    Args:
        l (list): The list of lists containing the data.

    Returns:
        list: The first list in the data.
    """
    return l[0]

def get_last(l):
    """Retrieve the last list from the data.

    Args:
        l (list): The list of lists containing the data.

    Returns:
        list: The last list in the data.
    """
    return l[-1]

def get_max(l):
    """Find the maximum value in a list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The maximum value in the list.
    """
    return max(l)

def get_min(l):
    """Find the minimum value in a list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The minimum value in the list.
    """
    return min(l)

def get_sum(l):
    """Calculate the sum of all integers in a list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The sum of the integers in the list.
    """
    return sum(l)

#### Fonction principale

def main():
    """Main function to read data from a file and print it with selected operations."""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, k))

if __name__ == "__main__":
    main()
