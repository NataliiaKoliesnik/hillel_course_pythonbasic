# a function that adds 1 to a number obtained from a given list and outputs it as a list

def add_one(some_list):
    my_str = "".join(map(str, some_list)) # converting a list to a string
    new_list = []
    # converting a string to a number, adding 1, then converting it back to a string and to a list
    for i in str(int(my_str) + 1):
        new_list.append(int(i)) #
    return new_list # outputting the new list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")