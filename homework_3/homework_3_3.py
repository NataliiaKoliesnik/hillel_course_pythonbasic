# splitting one list into two lists

# code verification - example 1
lst_1 = [1, 2, 3, 4, 5, 6]
if lst_1:
    if len(lst_1) % 2 == 0:
        m = len(lst_1) // 2
        lst_1 = [lst_1[:m], lst_1[m:len(lst_1)]]
        print(lst_1)
    else:
        if len(lst_1) == 1:
            lst_1 = [lst_1,[]]
            print(lst_1)
        else:
            m = len(lst_1) // 2 + 1
            lst_1 = [lst_1[:m], lst_1[m:len(lst_1)]]
            print(lst_1)
else:
    lst_1 = [[],[]]
    print(lst_1)

# code verification - example 2
lst_2 = [1, 2, 3]
if lst_2:
    if len(lst_2) % 2 == 0:
        n = len(lst_2) // 2
        lst_2 = [lst_2[:n], lst_2[n:len(lst_2)]]
        print(lst_2)
    else:
        if len(lst_2) == 1:
            lst_2 = [lst_2,[]]
            print(lst_2)
        else:
            n = len(lst_2) // 2 + 1
            lst_2 = [lst_2[:n], lst_2[n:len(lst_2)]]
            print(lst_2)
else:
    lst_2 = [[],[]]
    print(lst_2)

# code verification - example 3
lst_3 = [1, 2, 3, 4, 5]
if lst_3:
    if len(lst_3) % 2 == 0:
        l = len(lst_3) // 2
        lst_3 = [lst_3[:l], lst_3[l:len(lst_3)]]
        print(lst_3)
    else:
        if len(lst_3) == 1:
            lst_3 = [lst_3,[]]
            print(lst_3)
        else:
            l = len(lst_3) // 2 + 1
            lst_3 = [lst_3[:l], lst_3[l:len(lst_3)]]
            print(lst_3)
else:
    lst_3 = [[],[]]
    print(lst_3)

# code verification - example 4
lst_4 = [1]
if lst_4:
    if len(lst_4) % 2 == 0:
        k = len(lst_4) // 2
        lst_4 = [lst_4[:k], lst_4[k:len(lst_4)]]
        print(lst_4)
    else:
        if len(lst_4) == 1:
            lst_4 = [lst_4,[]]
            print(lst_4)
        else:
            k = len(lst_4) // 2 + 1
            lst_4 = [lst_4[:k], lst_4[k:len(lst_4)]]
            print(lst_4)
else:
    lst_4 = [[],[]]
    print(lst_4)

# code verification - example 5
lst_5 = []
if lst_5:
    if len(lst_5) % 2 == 0:
        p = len(lst_5) // 2
        lst_5 = [lst_5[:p], lst_5[p:len(lst_5)]]
        print(lst_5)
    else:
        if len(lst_5) == 1:
            lst_5 = [lst_5,[]]
            print(lst_5)
        else:
            p = len(lst_5) // 2 + 1
            lst_5 = [lst_5[:p], lst_5[p:len(lst_5)]]
            print(lst_5)
else:
    lst_5 = [[],[]]
    print(lst_5)