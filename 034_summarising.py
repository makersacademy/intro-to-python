# Video alternative: https://vimeo.com/954334424/6e40d11ef1#t=501

from lib.helpers import check_that_these_are_equal

# Summarising is processing down a list to a single value.
# It is sometimes also called 'reduce' — like reducing a
# broth to a thick soup.

# Here are some examples:

# * Summing a list of numbers
# * Counting the number of 'q's in a string
# * Concatenating a list of strings

# I'm going to implement the last one, so you can see it at
# work:

lines = [
  "My King,",
  "I need another five years.",
  "Then your crab will be ready.",
  "Sincerely,",
  "Chuang-tzu"
]

text = "" # This is called the accumulator variable
          # It's where we put our summary value
          # It starts off blank.

for line in lines: # We go through lines item by item
  # Inside this loop, `line` is the individual line
  text = text + line # We append the line to our text
  text = text + "\n" # We add an `\n`, which means 'new line'

print(text)

# We have taken the list of strings and joined them all
# together into one text (the accumulator) with some new
# lines in it.

# There's actually a Python function that does this too:

another_text = "\n".join(lines)
# Uncomment this next line if you want to see it
# print(another_text)

# `join` is actually little smarter — it only adds the `\n`
# character between lines, not at the end also.

# @TASK: Complete this exercise

print("")
print("Function: add_up_numbers")

# Add up all the numbers in the list
def add_up_numbers(numbers):
  pass

check_that_these_are_equal(
  add_up_numbers([1, 2, 3, 4]), 10)
check_that_these_are_equal(
  add_up_numbers([2, 3, 4, 5]), 14)

# When you're done, move on to 035_mapping.py
