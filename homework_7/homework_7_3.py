# a function to search for the second occurrence of a string within a string

def second_index(text, some_str):
  first_ind = text.find(some_str)
  if first_ind == -1: # if there is no first occurrence
      return None
  second_ind = text.find(some_str, first_ind + 1)
  if second_ind == -1: # if there is no second occurrence
      return None
  else:
      return second_ind

# function testing
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')