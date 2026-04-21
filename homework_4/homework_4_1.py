# moving all zeros to the end of the list

#different versions of the list are commented out
#lst = [0,1,0,12,3]
#lst = [0]
#lst = [1,0,13,0,0,0,5]
lst = [9,0,7,31,0,45,0,45,0,45,0,0,96,0]
j = 0
n = len(lst)
for i in range(n):
    if lst[j] == 0:
        lst.append(lst.pop(j))
    else:
        j += 1
print(lst)