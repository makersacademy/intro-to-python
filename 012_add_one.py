from lib.helpers import show_us_the_output_of

# Video alternative: ...

# Let's create a more useful function:

def add_one(num):
    return num + 1

# Here is how it used (but don't run it just yet):

print("add_one(6) is:")
show_us_the_output_of(
    add_one(6) # <-- Calling the function
)

# @TASK: Run this code in the shell:
#
# ```
# python 012_add_one.py
# ```

# `add_one` is a function (little machine) that takes an
# input of a number, adds one to it, and then returns the
# result.

# Now move on to 013_add_two.py
