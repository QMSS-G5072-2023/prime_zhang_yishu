import math

def is_prime(n):
    """
    Check if the imput number is a prime number.

    Parameter
    ----------
    n : a number

    Returns
    -------
    True: the imput number n is a prime number.
    False: the imput number n is not a prime number.

    Examples
    --------
    >>> is_prime(-10)
    False
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
