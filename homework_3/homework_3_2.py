# moving the last element of a list from the end to the beginning

# code verification - example 1
lst_1 = [12, 3, 4, 10]
if lst_1:
    if len(lst_1) == 1:
        print(lst_1)
    else:
        lst = lst_1.insert(0,lst_1.pop())
        print(lst_1)
else:
    print(lst_1)

# code verification - example 2
lst_2 = [1]
if lst_2:
    if len(lst_2) == 1:
        print(lst_2)
    else:
        lst = lst_2.insert(0,lst_2.pop())
        print(lst_2)
else:
    print(lst_2)

# code verification - example 3
lst_3 = []
if lst_3:
    if len(lst_3) == 1:
        print(lst_3)
    else:
        lst = lst_3.insert(0,lst_3.pop())
        print(lst_3)
else:
    print(lst_3)

# code verification - example 4
lst_4 = [12, 3, 4, 10, 8]
if lst_4:
    if len(lst_4) == 1:
        print(lst_4)
    else:
        lst = lst_4.insert(0,lst_4.pop())
        print(lst_4)
else:
    print(lst_4)