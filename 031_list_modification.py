# Video alternative: ...

from lib.helpers import check_that_these_are_equal

# Python comes with a number of helpful functions to work
# with lists. We'll look at some that modify lists.

# Let's look at `append` first:

my_list = ["a", "b", "c"]
my_list.append("d")
print(my_list) # my_list is now ["a", "b", "c", "d"]

# The effect is straightforward enough — it adds an item to
# the list.

# But there are two unusual aspects to this code.

# == Aspect One: Methods ==

# When we looked at strings, our function looked like this:

my_string = "hello!"
len(my_string) # Evaluates to 6

# Whereas this function looks like this:

my_list = ["a", "b", "c"]
my_list.append("d")

# For `append` the function name comes after the variable
# name. This is known as a 'method'. We would refer to
# `append` as being called 'on' `my_list`.

# Don't worry about it too much for now. Just remember that
# some functions come after the variable name.

# == Aspect Two: Mutation ==

# Consider this code with numbers

my_num = 3
3 + 1
print(my_num) # my_num is still 3

# `my_num` stays `3` here because in the above code we're
# not assigning the result of the expression to a variable.

# However, in our list code:

my_list = ["a", "b", "c"]
my_list.append("d")
print(my_list) # my_list is now ["a", "b", "c", "d"]

# `my_list` gets magically changed without an assignment!

# The behaviour of append is to modify the list 'in-place'.
# Again, don't worry too much about this right now. If you
# have any trouble with it, you can always create a new
# list by using the `copy` method.

my_list = ["a", "b", "c"]
my_copy = my_list.copy()
my_copy.append("d")
print(my_list) # my_list is still ["a", "b", "c"]
print(my_copy) # my_copy is now   ["a", "b", "c", "d"]

# But mostly you won't need to worry about it just yet.

# @TASK Do these exercises.
#
# You'll need to research the right methods to use. Here's
# a useful resource: https://docs.python.org/3/tutorial/datastructures.html

# I've started it for you.

print("")
print("Function: append_item_to_list")

def append_item_to_list(the_list, item):
  the_list.append(item)
  return the_list

check_that_these_are_equal(
  append_item_to_list(['a', 'b'], 'c'), ['a', 'b', 'c'])
check_that_these_are_equal(
  append_item_to_list([3, 1], 6), [3, 1, 6])

# == Exercise One ==

print("")
print("Function: remove_item_from_list")

def remove_item_from_list(the_list, item):
  # ...
  return the_list

check_that_these_are_equal(
  remove_item_from_list(['a', 'b'], 'b'), ['a'])
check_that_these_are_equal(
  remove_item_from_list([3, 1], 3), [1])

# == Exercise Two ==

print("")
print("Function: count_items_in_list")

def count_items_in_list(the_list, item):
  return # ...

check_that_these_are_equal(
  count_items_in_list(['a', 'b', 'a'], 'a'), 2)
check_that_these_are_equal(
  count_items_in_list([4, 1, 4, 4], 4), 3)

# == Exercise Three ==

print("")
print("Function: get_index_of_item")

def get_index_of_item(the_list, item):
  return # ...

check_that_these_are_equal(
  get_index_of_item(['a', 'b', 'c'], 'b'), 1)
check_that_these_are_equal(
  get_index_of_item([33, 44, 55], 55), 2)

# == Exercise Four ==

print("")
print("Function: reverse_list")

def reverse_list(the_list):
  # ...
  return the_list

check_that_these_are_equal(
  reverse_list(['a', 'b', 'c']), ['c', 'b', 'a'])
check_that_these_are_equal(
  reverse_list([33, 44, 55]), [55, 44, 33])

# == Exercise Five ==

print("")
print("Function: list_length")

# Note — it's the same as for strings!
def list_length(list):
  return # ...

check_that_these_are_equal(
  list_length(['a', 'b', 'c']), 3)
check_that_these_are_equal(
  list_length([33, 44]), 2)

# When you're done, move on to 032_while_loops.py
