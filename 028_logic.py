# Video alternative: https://vimeo.com/954334163/bf61706e77#t=760

from lib.helpers import check_that_these_are_equal

# As we've mentioned, while numeric operators evaluate to
# numbers, like this:

1 + 2 # evaluates to 3

# Comparison operators evaluate to True or False

1 == 2 # evaluates to False
2 == 2 # evaluates to True

# The `if` keyword looks at whether the conditional
# expression evaluates to True or False to decide whether to
# execute its block, or the else block.

# We can use this information to combine conditions using a
# new kind of operators: logical operators.

# Consider this function:

def starts_with_x_or_y(the_str):
  first_letter = the_str[0]
  #                      VV look at this!
  if first_letter == "x" or first_letter == "y":
    return "It does!"
  else:
    return "It does not."

# That `or` operator says "evaluate to true if the condition
# on the left, or on the right, or both evaluate to true".

# Operators like `or` are called 'logical' or 'Boolean'
# operators.

# There are others here too.

# @TASK: Research by searching the web for "python
# logical operators" and complete the exercises below.

# I've started it for you.

print("")
print("Function: a_or_b")

def a_or_b(a, b):
  return a or b

check_that_these_are_equal(a_or_b(True, True), True)
check_that_these_are_equal(a_or_b(True, False), True)
check_that_these_are_equal(a_or_b(False, True), True)
check_that_these_are_equal(a_or_b(False, False), False)

# == Exercise One ==

print("")
print("Function: a_and_b")

def a_and_b(a, b):
  # return a ?? b
  pass

check_that_these_are_equal(a_and_b(True, True), True)
check_that_these_are_equal(a_and_b(True, False), False)
check_that_these_are_equal(a_and_b(False, True), False)
check_that_these_are_equal(a_and_b(False, False), False)

# == Exercise Two ==

print("")
print("Function: not_a")

# Note that this operator only takes one value. The operator
# goes first, and the value second.
def not_a(a):
  # return ?? a
  pass

check_that_these_are_equal(not_a(True), False)
check_that_these_are_equal(not_a(False), True)

# Perhaps you could have guessed those... but now you know
# for sure! When you're done, move on to 029_lists.py
