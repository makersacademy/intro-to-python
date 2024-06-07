# Video alternative: https://vimeo.com/954334163/bf61706e77#t=338

from lib.helpers import check_that_these_are_equal

# We've seen the `==` comparison operator. There are some
# others too. Each of them evaluates to True or False, which
# is how the `if` knows whether to execute or not.

# @TASK: Research by searching the web for "python
# comparison operators" and complete the exercises below.
#
# I've started it for you.

print("")
print("Function: a_is_equal_to_b")

def a_is_equal_to_b(a, b):
  return a == b

check_that_these_are_equal(
  a_is_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_equal_to_b("a", "a"),
  True
)

check_that_these_are_equal(
  a_is_equal_to_b(1, 2),
  False
)

# == Exercise One ==

print("")
print("Function: a_is_less_than_b")

def a_is_less_than_b(a, b):
  # Uncomment this next line and replace ?? with the right operator
  # return a ?? b
  pass

check_that_these_are_equal(
  a_is_less_than_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_less_than_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_less_than_b(2, 1),
  False
)

# == Exercise Two ==

print("")
print("Function: a_is_greater_than_b")

def a_is_greater_than_b(a, b):
  # return a ?? b
  pass

check_that_these_are_equal(
  a_is_greater_than_b(1, 2),
  False
)

check_that_these_are_equal(
  a_is_greater_than_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_greater_than_b(2, 1),
  True
)

# == Exercise Three ==

print("")
print("Function: a_is_less_than_or_equal_to_b")

def a_is_less_than_or_equal_to_b(a, b):
  # return a ?? b
  pass

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(2, 1),
  False
)

# == Exercise Four ==

print("")
print("Function: a_is_greater_than_or_equal_to_b")

def a_is_greater_than_or_equal_to_b(a, b):
  # return a ?? b
  pass

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(1, 2),
  False
)

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(2, 1),
  True
)

# == Exercise Five ==

print("")
print("Function: a_is_not_equal_to_b")

def a_is_not_equal_to_b(a, b):
  # return a ?? b
  pass

check_that_these_are_equal(
  a_is_not_equal_to_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_not_equal_to_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_not_equal_to_b(2, 1),
  True
)

# == Exercise Six ==

print("")
print("Function: a_is_within_b")

# May be a little tricky — search for
# "python check if string contains substring"
def a_is_within_b(a, b):
  # return a ?? b
  pass

check_that_these_are_equal(
  a_is_within_b("e", "hello"),
  True
)

check_that_these_are_equal(
  a_is_within_b("f", "hello"),
  False
)

# When you're done, move on to 028_logic.py
