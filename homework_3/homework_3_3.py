# splitting one list into two lists

# example 1
lst = [1, 2, 3, 4, 5, 6]
# example 2
#lst = [1, 2, 3]
# example 3
#lst = [1, 2, 3, 4, 5]
# example 4
#lst = [1]
# example 5
#lst = []
if lst:
    if len(lst) % 2 == 0:
        m = len(lst) // 2
        lst_1 = [lst[:m], lst[m:len(lst)]]
        print(lst_1)
    else:
        if len(lst) == 1:
            lst_1 = [lst,[]]
            print(lst_1)
        else:
            m = len(lst) // 2 + 1
            lst_1 = [lst[:m], lst[m:len(lst)]]
            print(lst_1)
else:
    lst_1 = [[],[]]
    print(lst)
