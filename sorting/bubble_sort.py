def bubble_sort(lst):
    for i in range(len(lst) - 1):
        flag = False
        for j in range(len(lst) - i - 1):
            # it's certain that after one inner loop the maximum is placed at last
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                # if there happens swap then it still needs loop
                flag = True
        # this will not pass if there happens swap
        if not flag:
            break

    return lst


test_lst = [12, 23, 1, 44, 10, 33, 21]

print(bubble_sort(test_lst))

