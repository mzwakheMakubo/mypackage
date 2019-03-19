def bubble_sort(items):

    '''
        Args:
            items: an array or list containing unsorted values.

        Returns:
            array or list: values are sorted in ascending order.

        Examples:
        >>> bubble_sort([1,7,6,2,3])
        [1,2,3,6,7]
    '''

    exitCondition = 0
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            temp = myList[i]
            myList[i] = myList[i + 1]
            myList[i + 1] = temp
            exitCondition+=1
    if exitCondition == 0: #return the list if it is already sorted
        return myList
    else:
        return bubblesort(myList) #calling our function recursively acts as an outer loop with the exitCondition terminating the loop

def merge_sort(items):

    '''
        Args:
            items: an array or list containing unsorted values.

        Returns:
            array or list: values are sorted in ascending order.

        Examples:
        >>> merge_sort([1,7,6,2,3])
        [1,2,3,6,7]
    '''

    arrayLength = len(arr)
    if arrayLength > 1:
        #we split our array into two seperate arrays
        middle = arrayLength//2
        leftArray = arr[:middle]
        rightArray = arr[middle:]

        '''we call our merge_sort function to recursively split our two
        arrays.  '''
        merge_sort(leftArray)
        merge_sort(rightArray)

        leftPos = 0
        rightPos = 0
        arrPos = 0

        while leftPos < len(leftArray) and rightPos < len(rightArray):
            #for each iteration, we compare values between two arrays
            #we insert the smallest one in the original array
            if leftArray[leftPos] < rightArray[rightPos]:
                arr[arrPos] = leftArray[leftPos]
                leftPos+=1
            else:
                arr[arrPos] = rightArray[rightPos]
                rightPos+=1
            arrPos+=1

        '''what ever that is left from both arrays is inserted into the original array.
        .We start with the leftArray because those values will be less than the values in
        the rightArray'''
        while leftPos < len(leftArray):
            arr[arrPos] = leftArray[leftPos]
            leftPos+=1
            arrPos+=1

        while rightPos < len(rightArray):
            arr[arrPos] = rightArray[rightPos]
            rightPos+=1
            arrPos+=1
        '''i have not figured out why the remaining leftArray and rightArray values are already sorted.
        I would have loved to give a better explanation but as i continue to understand recursion and the idea of a stack,
        i will update the codebase'''
    return arr

def quick_sort(items):

    '''
        Args:
            items: an array or list containing unsorted values.

        Returns:
            array or list: values are sorted in ascending order.

        Examples:
        >>> bubble_sort([1,7,6,2,3])
        [1,2,3,6,7]
    '''

    def partitionMyList(items, startingPoint, myPivot):
        '''partionMyList splits our array/list into two seperate parts divided by myPivot'''
        pivot = items[myPivot] #for this function, are pivot is always the last element in the list (-1)
        i = -1
        for j in range(0, myPivot):
            if items[j] <= pivot:
                i+=1
                temp = items[i]
                items[i] = items[j]
                items[j] = temp

        #at the end of the above loop, we move our pivot to the correct positioning
        temp = items[i + 1]
        items[i + 1] = items[myPivot]
        items[myPivot] = temp
        return i + 1

    def quickSort(items, startingPoint, myPivot):
        if startingPoint < myPivot:
            piv = partitionMyList(items, startingPoint, myPivot)#our pivot value defined in the function above

            quickSort(items, startingPoint, piv-1)#firts half of list before pivot
            quickSort(items, piv+1, myPivot)#second half of pivot after pivot
        return items

    n = len(myList)
    quickSort(items, 0, n-1)#this forces our function to always assign the last element in the array/list as pivot
    return items
