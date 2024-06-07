# Video alternative: https://vimeo.com/954334266/1ad4327868

# Start reading here:

def just_return_it(num):
  return num

# This is a function. A function is a reusable block of
# code.

# Think of a function as a little machine. It takes an
# input, processes it in some way, and then returns an
# output.

# This `just_return_it` function has:

# * A name: `just_return_it` that we can use to call it

# * A parameter: `num` that it takes as input. You might
#   also hear these informally referred to as 'arguments'

# * A body: `return num` that processes the input and
#   returns the result as output. Python uses spaces at the
#   start of each line to indicate what's the body and what
#   isn't

# `just_return_it` is a very simple function, it doesn't do
# very much. It takes a piece of data as input, and returns
# it as output.

# We call a function like this:

just_return_it(4)
# Returns 4

# In the code above, the argument `4` goes into the
# `just_return_it` function and takes the place of `num` in
# the function body.

# Want to see? Here, we can use `print` to show you:

print("just_return_it(4) returns:")
print(just_return_it(4))

# @TASK: Run this program in the right-hand shell panel:
#
#   python 011_identity.py
#
# If you don't see the shell, watch this video:
# https://vimeo.com/954334352/1f0dee9379
#
# After running the command, you should see:
#
# ```
# just_return_it(4) returns:
# 4
# ```
#
# This shows us that when we call the `just_return_it`
# function with the input parameter `4` — it gives us `4`
# back.
#
# Now move on to 012_add_one.py
