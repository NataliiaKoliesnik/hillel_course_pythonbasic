# moving the last element of a list from the end to the beginning

# example 1
#lst = [12, 3, 4, 10]
# example 2
#lst = [1]
# example 3
#lst = []
# example 4
lst = [12, 3, 4, 10, 8]
if lst:
    if len(lst) == 1:
        print(lst)
    else:
        lst.insert(0, lst.pop())
        print(lst)
else:
    print(lst)
