# Ignore this bit for now. It imports some helper code for
# us.
from lib.helpers import show_us_the_output_of

# Video alternative: ...

# Start reading here:

def identity(num):
    return num

# This is a function. A function is a reusable block of
# code.
#
# Think of functions as little machines. It takes an input,
# processes it in some way, and then returns an output.
#
# This `identity` function has:
#
# * A name: `identity` that we can use to call it
# * A parameter: `num` that it takes as input
# * A body: `return num` that returns the input as output
#
# `identity` is a very simple function, it doesn't do very
# much. It takes a piece of data as input, and returns it as
# output.
#
# Let's use it:

print("identity(4) is:") # <-- This just prints a message

show_us_the_output_of(  # <-- This helps us see the output of...
    identity(4) # <-- This is the important part
)

# @TASK: Run this program by opening the shell in the
# right-hand panel and running:
#
# ```
# python 011_identity.py
# ```
#
# If you don't see the shell, watch this video to to get set
# up: @TODO
#
# After running the command, you should see:
#
# ```
# identity(4) is:
# 4
# ```
#
# This shows us that when we call the `identity` function
# with the input parameter `4` — it gives us `4` back.
#
# Now move on to 012_add_one.py
