def sum_array(array):
    '''
        Args:
            array: an array or list containing values.

        Returns:
            int: the sum of the array/list

        Examples:
        >>> sum_array([1,2,3])
        6
    '''

    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''
        Return nth term in fibonacci sequence

        Args:
            n: nth term in a fibonacci sequence

        Returns:
            int: fibonacci sequence number in positon n

        Examples:
            >>> fibonacci(6)
            8
    '''

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):

    '''
        Args:
            n: factorial

        Returns:
            int: factorial of n

        Example:
            >>> factorial(5)
            120
    '''

    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1) # this is equivalent to -> 5! = 5 * (5-1)!
    return

def reverse(word):

    '''
        Args:
            word: a string literal.

        Returns:
            string: string literal in reverse

        Examples:
        >>> reverse('talk')
        klat
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(string[1:]) + string[0]
