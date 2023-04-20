from lib.helpers import show_us_the_output_of

# Video alternative: ...

# So far we've seen functions that take only one input. They
# can actually take two, or even more, inputs. Take a look
# at this:

# Notice two items and the comma below
def multiply_numbers(num_a, num_b):
    return num_a * num_b # That `*` means multiply_numbers

# And let's use it:

print("multiply_numbers(2, 3) is:")

show_us_the_output_of(
    multiply_numbers(2, 3)
)

print("multiply_numbers(3, 5) is:")

show_us_the_output_of(
    multiply_numbers(3, 5)
)

# @TASK: Run these in the shell using:
# python 014_multiply_numbers.py

# As a reminder, these inputs are called parameters.

# Now move on to 015_add_numbers.py to write your own.
