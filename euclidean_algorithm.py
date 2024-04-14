def euclidean_algorithm(a, b):
    """
    Calculate the greatest common divisor of two integers using the Euclidean Algorithm.

    :param a: First positive integer
    :param b: Second positive integer
    :return: The greatest common divisor of a and b
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
