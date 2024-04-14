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


def get_positive_integer(prompt):
    """
    Get a positive integer from the user.

    :param prompt: The prompt to display to the user
    :return: A positive integer input by the user
    """
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    a = get_positive_integer("Enter the first positive integer: ")
    b = get_positive_integer("Enter the second positive integer: ")
    gcd = euclidean_algorithm(a, b)
    print(f"The greatest common divisor of {a} and {b} is {gcd}.")

if __name__ == "__main__":
    main()
