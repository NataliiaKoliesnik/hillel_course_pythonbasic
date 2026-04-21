#the sum of elements with even indices was found and multiplied by the last one

lst = [0,1,7,2,4,8]
#different versions of the list are commented out
#lst = [1,3,5]
#lst = [6]
#lst = []
result = 0
for i in lst:
    if lst:
        if lst.index(i) % 2 == 0 or lst.index(i) == 0:
            result += i
        if lst.index(i) == len(lst) - 1:
            result *= i
print(result)