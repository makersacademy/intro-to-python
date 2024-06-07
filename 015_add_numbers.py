from lib.helpers import check_that_these_are_equal

# Video alternative: https://vimeo.com/954334235/902b0b036d#t=444

# @TASK: Now you try. Here's an exercise for you:
#
# Write a function called `add_numbers` that:
#
# * Takes two numbers as input
# * Adds them together
# * Returns the result

# YOUR FUNCTION GOES BELOW THIS LINE



# YOUR FUNCTION GOES ABOVE THIS LINE

# @TASK: Check your work by running:

#   python 015_add_numbers.py

# Below is a test for your function.

print("add_numbers(2, 3) is:")

check_that_these_are_equal(
  add_numbers(2, 3),
  5
)

print("add_numbers(3, 5) is:")

check_that_these_are_equal(
  add_numbers(3, 5),
  8
)

# When you're done, move on to 016_operators.py
