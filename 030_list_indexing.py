# Video alternative: https://vimeo.com/954334163/bf61706e77#t=1171

from lib.helpers import check_that_these_are_equal

# Similarly to strings, you can index into lists.

my_list = [44, 35, 21, 63]
my_list[0]   # Evaluates to 44
my_list[-1]  # Evaluates to 63
my_list[1:3] # Evaluates to [35, 21]

# To show you how similar they are, here are some very
# similar exercises as in the strings material. You may find
# the exact same code works for strings and lists!

# @TASK: Complete the following exercises. You can check
# them as you go by running: python 030_list_indexing.py

# == Exercise One ==

print("")
print("Function: get_first_item")

def get_first_item(the_list):
  # Return the first item of the list
  pass

check_that_these_are_equal(
  get_first_item(["a", "b", "c", "d", "e"]),
  "a"
)

check_that_these_are_equal(
  get_first_item([34, 44, 54, 64]),
  34
)

# == Exercise Two ==

print("")
print("Function: get_last_item")

def get_last_item(the_list):
  # Return the last item of the list
  pass

check_that_these_are_equal(
  get_last_item(["a", "b", "c", "d", "e"]),
  "e"
)

check_that_these_are_equal(
  get_last_item([34, 44, 54, 64]),
  64
)

# == Exercise Three ==

print("")
print("Function: get_nth_item")

def get_nth_item(the_list, n):
  # Return the item of the list at the specified index
  pass

check_that_these_are_equal(
  get_nth_item(["a", "b", "c", "d", "e"], 3),
  "d"
)

check_that_these_are_equal(
  get_nth_item([34, 44, 54, 64], 1),
  44
)

# == Exercise Four ==

print("")
print("Function: get_items_between_one_and_three")

def get_items_between_one_and_three(the_list):
  # Return the section of the list between indexes one
  # and three
  pass

check_that_these_are_equal(
  get_items_between_one_and_three(["a", "b", "c", "d", "e"]),
  ["b", "c"]
)

check_that_these_are_equal(
  get_items_between_one_and_three([34, 44, 54, 64]),
  [44, 54]
)

# When you're done, move on to 031_list_modification.py

