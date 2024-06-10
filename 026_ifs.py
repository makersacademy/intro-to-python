# Video alternative: https://vimeo.com/954334163/bf61706e77#t=0

from lib.helpers import check_that_these_are_equal

# Programs often have to make decisions based on their
# input. For this, we use the `if` keyword.

# Here is an example:

leaves_on_the_tree = 0

if leaves_on_the_tree == 0:
  print("It must be winter — or a dead tree")

# Let's break this down:

# The `if` keyword tells Python we want to execute some code
# conditionally.

# The `leaves_on_the_tree == 0` is the conditional
# expression. If this evaluates to True, then the block of
# code afterwards will be run.

# Within this, the `==` is a comparison operator. It
# evaluates to True if the value on the left and on the
# right are equal.

# The colon `:` indicates the start of a new block of code.

# The indented block of code after the if is the conditional
# block. Python will run it if the condition evaluates to
# True.

# We can also have an `else` to cover the other case:

if leaves_on_the_tree == 0:
  print("It must be winter — or a dead tree")
else:
  print("This is a happy tree with nice leaves")

# When Python sees the `else:`, it will execute the next
# block of code only if the condition evaluated to False.

# These blocks are mutually exclusive — only one of them
# will run, never both.

# @TASK: Complete these exercises

# == Exercise One ==

print("")
print("Function: is_first_of_the_month")

def is_first_of_the_month(day_number):
  # Return "First of the month!" if the day number is 1.
  # Return "Not first of the month" otherwise.
  pass

check_that_these_are_equal(
  is_first_of_the_month(1),
  "First of the month!"
)

check_that_these_are_equal(
  is_first_of_the_month(12),
  "Not first of the month"
)

# == Exercise Two ==

print("")
print("Function: has_five_chars")

def has_five_chars(the_str):
  # Return "STRING is five characters long" if the string
  # is five characters long.
  # Otherwise, return "Not five characters".
  pass

check_that_these_are_equal(
  has_five_chars("ABCDE"),
  "ABCDE is five characters long"
)

check_that_these_are_equal(
  has_five_chars("FORGE"),
  "FORGE is five characters long"
)

check_that_these_are_equal(
  has_five_chars("Nope"),
  "Not five characters"
)

check_that_these_are_equal(
  has_five_chars("Nor this one"),
  "Not five characters"
)

# When you're done, move on to 027_comparison.py
