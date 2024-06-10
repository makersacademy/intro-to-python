# Video alternative: https://vimeo.com/954334424/6e40d11ef1#t=300

# There's another kind of loop — the `for` loop.

# It looks like this:

for letter in ["a", "b", "c"]:
  print(f"This letter is {letter}")

# @TASK: Run this file and see what it does.

# In programming jargon: the Python for loop iterates over a
# list.

# In everyday language: the Python for loop takes each item
# one by one and runs its block of code with that item.

# It's pretty nice. And there's another Python helper that
# makes it even more useful:

def print_numbers_in_range():
  for number in range(0, 10):
    print(f"This number is {number}")

# `range` more or less creates a list of the numbers from
# its first parameter to one below its last parameter. So:
# the numbers 0-9.

# Compare this to the `while` version which does the same
# thing:

def print_numbers_in_range_with_a_while():
  number = 0
  while number < 10:
    print(f"This number is {number}")
    number = number + 1

# The `for` and `range` version is a bit more concise.

# You're probably expecting an exercise now. But not just
# yet. Lists and loops are very powerful tools and we're
# going to go through three different ways of using them:

# * Summarising: Using a loop to distil a list into one
#   value.

# * Mapping: Using a loop to convert each item to another
#   item.

# * Filtering: Using a loop to pick out only some items from
#   a list.

# To start summarising, go to 034_summarising.py
