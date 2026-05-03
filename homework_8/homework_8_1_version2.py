# a function that adds 1 to a number obtained from a given list and outputs it as a list

def add_one(some_list):
    result = some_list[:] # we copy the list so as not to modify the one that was passed in
    i = len(result) - 1 # counter
    while i >= 0:
        if result[i] < 9: # if a list element is less than 9
            # we add 1 to the last element of the list,
            # or to the next element that comes after the element equal to 9
            result[i] += 1
            return result
        result[i] = 0 # if an element equals 9, when adding 1 it becomes 0
        i -= 1
    # our loop did not break earlier, so we need to add 1 to the front of the resulting list
    return [1] + result
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")