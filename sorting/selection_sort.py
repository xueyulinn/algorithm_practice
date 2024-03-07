""" selection sort has better performance than bubble sort
    as it only swaps once for every loop while its time 
    complexity is O(n^2) """
def selection_sort(lst):
    """ make use of the index of the minimum then swap 
        from the beginning to the end """
    for i in range(len(lst)-1):
        # initialize min as the first position
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j

        if i != min:
            lst[i], lst[min] = lst[min], lst[i]

    return lst


lst = test_lst = [12, 23, 1, 44, 10, 33, 21]

print(selection_sort(lst))
