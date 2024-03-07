""" insertion sort is like sorting poker,
    it starts from the right and compares with
    the left """
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]

        j = i-1

        while j >= 0 and key < lst[j]:
                lst[j+1], lst[j] = lst[j], key
                j -= 1


lst = test_lst = [12, 23, 1, 44, 10, 33, 21]

print(insertion_sort(lst))
