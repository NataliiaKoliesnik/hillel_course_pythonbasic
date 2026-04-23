# splitting one list into two lists

lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
#lst = [1, 2, 3, 4, 5]
#lst = [1]
#lst = []
if len(lst) % 2 == 0:
    half = len(lst) // 2
    result = [lst[:half], lst[half:]]
else:
    half = len(lst) // 2
    result = [lst[:half + 1], lst[half + 1:]]
print(result)