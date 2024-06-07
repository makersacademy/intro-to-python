# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=214

from lib.helpers import check_that_these_are_equal

# Filtering is going through a list and keeping only some of
# the items, typically according to a condition of some
# kind. This is useful when you only want to keep some of
# the items in your list.

# For example:

# * Filtering a list of products to only items under £5
# * Filtering a list of numbers to remove minus numbers
# * Removing 'junk' data from a list

# Here's an example:

# Imagine someone didn't put their age in
raw_ages = [32, 40, None, 1, 32]

clean_ages = [] # This is our accumulator again

for age in raw_ages: # We go through each age
  # We combine a for with an if to remove 'None' items
  if age != None:
    clean_ages.append(age)

print(raw_ages)
print(clean_ages)

# @TASK: run this program to see what it does.

# @TASK: Complete this exercise.

print("")
print("Function: only_positive_numbers")

# Return a new list with only the positive numbers
def only_positive_numbers(numbers):
  pass

check_that_these_are_equal(
  only_positive_numbers([-4, 4, -3, 3]), [4, 3])
check_that_these_are_equal(
  only_positive_numbers([-100]), [])

# When you're done, move on to 037_dicts.py
