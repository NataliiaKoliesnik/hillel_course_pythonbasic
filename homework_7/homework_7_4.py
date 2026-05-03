# finding common elements of two sets

def common_elements():
    set_div_3 = set() # declare the first set
    set_div_5 = set() # declare the second set
    for i in range(100):
        if i % 3 == 0: # fill the first set with numbers divisible by 3
            set_div_3.add(i)
        if i % 5 == 0: # fill the second set with numbers divisible by 5
            set_div_5.add(i)
    return set_div_3.intersection(set_div_5) # find the intersection of the two sets

# function testing
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')