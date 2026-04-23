#the sum of elements with even indices was found and multiplied by the last one

#lst = [0,1,7,2,4,8]
#different versions of the list are commented out
#lst = [1,3,5]
#lst = [6]
lst = []
result = 0
if lst:
    for index, item in enumerate(lst):
        if index % 2 == 0:
            result += item
    result = result * lst[-1]
print(f'{result}')