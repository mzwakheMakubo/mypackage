rom mypackage import myFunction

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert myFunction.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert myFunction.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myFunction.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'

def test_sum_array():

    assert myFunction.sum_array([1,2,3]) == 6, 'incorrect'
    assert myFunction.sum_array([3,9,1]) == 13, 'incorrect'
    assert myFunction.sum_array([1,9,5]) == 15, 'incorrect'

def test_fibonacci():

    assert myFunction.fibonacci(6) == 8, 'incorrect'
    assert myFunction.fibonacci(11) == 89, 'incorrect'
    assert myFunction.fibonacci(5) == 5, 'incorrect'

def test_factorial():

    assert myFunction.factorial(5) == 120, 'incorrect'
    assert myFunction.factorial(9) == 362880, 'incorrect'
    assert myFunction.factorial(4) == 24, 'incorrect'

def test_reverse():

    assert myFunction.reverse('talk') == 'klat', 'incorrect'
    assert myFunction.reverse('good') == 'doog', 'incorrect'
    assert myFunction.reverse('python') == 'nohtyp', 'incorrect'

def test_bubble_sort():

    assert myFunction.bubblesort([5, 3, 7, 9]) == [3, 5, 7, 9], 'incorrect'
    assert myFunction.bubblesort([8, 3]) == [3, 8], 'incorrect'
    assert myFunction.bubblesort([1, 2, 3]) == [1, 2, 3], 'incorrect'

def test_merge_sort():

    assert myFunction.merge_sort([8, 3, 4, 1]) == [1, 3, 4, 8], 'incorrect'
    assert myFunction.merge_sort([5, 25, 3]) == [3, 5, 25], 'incorrect'
    assert myFunction.merge_sort([1, 2, 3]) == [1, 2, 3], 'incorrect'

def test_quick_sort():
    
    assert myFunction.quickSort([5, 3, 7, 9]) == [3, 5, 7, 9], 'incorrect'
    assert myFunction.quickSort([1, 17, 5, 9]) == [1, 5, 9, 17], 'incorrect'
    assert myFunction.quickSort([1, 2, 3]) == [1, 2, 3], 'incorrect'
