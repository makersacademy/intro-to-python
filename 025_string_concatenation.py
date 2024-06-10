# Video alternative: https://vimeo.com/954334279/dd2abfbdd7#t=1098

from lib.helpers import check_that_these_are_equal

# Concatenation means 'joining together'.

# We can join strings together in a few ways. Here's one:

my_string = "Ant" + "eater"
print(my_string)

# As you can see, string concatenation uses the same `+`
# operator that we used for addition.

# However, this expression won't work:

# my_string = "Forty" + 2

# Python doesn't like us mixing the concatenation of strings
# and the addition of numbers. To make it do this, we need
# to explicitly convert the number to a string using the
# `str` function built-in to Python.

my_string = "Forty" + str(2)
print(my_string)

# There is another way to concatenate strings which is more
# convenient. They are called f-strings, and are a feature
# of Python 3 (which replit.com uses).

# Here's what they look like:

my_name = "Kay"
print(f"Hello, {my_name}!")

# Note the `f` before the first quote, and the use of `{`
# and `}` to create space you can put a variable into. In
# fact, you can put any expression in there:

print(f"Your name is {len(my_name)} characters long")

# If you're particularly attentive, you might be asking how
# come Python didn't complain about us concatenating a
# number with a string. This is because f-strings in Python
# perform that `str` conversion for us. Very handy!

# f-strings are a form of what's called string
# interpolation.

# @TASK: Run this code using `python 025_string_concatenation.py`
# to see what it does, and then move onto the exercise below.

# == Exercise One ==

print("")
print("Function: greet")

def greet(name):
	# Return the string "Hello, Kay!" where "Kay" is the
	# name provided
	pass

check_that_these_are_equal(
	greet("Chuang-tzu"),
	"Hello, Chuang-tzu!"
)

check_that_these_are_equal(
	greet("Crab"),
	"Hello, Crab!"
)

# When you're done, move on to 026_ifs.py
