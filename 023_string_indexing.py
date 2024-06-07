# Video alternative: https://vimeo.com/954334279/dd2abfbdd7#t=410

from lib.helpers import check_that_these_are_equal

# In the earlier material, we focused on numbers.

# Numbers are a very simple data type — they represent a
# single value.

# Strings are more complex. They're a basic form of what, in
# programming, we call a 'data structure'.

# This means they've got more than one thing in them, and
# they're organised in a specific way depending on what type
# of data structure they are.

# A string has a number of characters inside it in a
# particular order.

# Take this string:

note = "The Most Perfect Crab"
print(note)

# We can access the first character like this:

print(note[0])
# In programming, we count from zero — 'T' is the zeroth
# character.

# And the last character like this:

print(note[-1])

# And any in the middle like this:

print(note[6])

# You can also get a 'slice' of the string like this:

print(note[0:3])
# This gets the portion of the string between index 0 and 3:
# 'The'

# @TASK: Complete the following exercises. You can check
# them as you go by running: python 023_string_indexing.py

# == Exercise One ==

print("")
print("Function: get_first_letter")

def get_first_letter(the_str):
  # Return the first letter of the string
  pass

check_that_these_are_equal(
  get_first_letter("The king granted them"),
  "T"
)

check_that_these_are_equal(
  get_first_letter("Five years later"),
  "F"
)

# == Exercise Two ==

print("")
print("Function: get_last_letter")

def get_last_letter(the_str):
  # Return the last letter of the string
  pass

check_that_these_are_equal(
  get_last_letter("The king granted them"),
  "m"
)

check_that_these_are_equal(
  get_last_letter("Five years later"),
  "r"
)

# == Exercise Three ==

print("")
print("Function: get_nth_letter")

def get_nth_letter(the_str, n):
  # Return the letter of the string at the specified index
  pass

check_that_these_are_equal(
  get_nth_letter("The king granted them", 4),
  "k"
)

check_that_these_are_equal(
  get_nth_letter("Five years later", 7),
  "a"
)

# == Exercise Four ==

print("")
print("Function: get_letters_between_four_and_eight")

def get_letters_between_four_and_eight(the_str):
  # Return the section of the string between indexes four
  # and eight
  pass

check_that_these_are_equal(
  get_letters_between_four_and_eight("The king granted them"),
  "king"
)

check_that_these_are_equal(
  get_letters_between_four_and_eight("Five years later"),
  " yea"
)

# When you're done, move on to 024_string_operations.py
