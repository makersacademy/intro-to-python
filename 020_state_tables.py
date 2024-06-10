# Video alternative: https://vimeo.com/954334376/0c486313d0#t=720

# Let's take a look at this program again.

a = 10
b = 20
a = b
print(f"a is {a}")
print(f"b is {b}")

# Python programs execute line by line, starting at the top.

# We're going to go through this code line by line and I'll
# explain what's happening.

# Initially the state is empty.

# Python executes the line:
#   a = 10
#
# Python assigns the value `10` to the variable `a`
#
# The state is now:
# | Name | Value |
# | ---- | ----- |
# | a    | 10    |

# Python executes the line:
#   b = 20
#
# Python assigns the value `20` to the variable `b`
#
# The state is now:
# | Name | Value |
# | ---- | ----- |
# | a    | 10    |
# | b    | 20    |

# Python executes the line:
#   a = b
#
# Python looks up the value of `b` in the expression on the
# right.
#
# It sees that it is `20`.
#
# It assigns the value `20` to the variable `a`
#
# Note that `b` does not change.
#
# The state is now:
# | Name | Value |
# | ---- | ----- |
# | a    | 20    |
# | b    | 20    |

# Python then prints the results and ends the program.

# So what happened to that `10`? It was overwritten, just
# like if you selected some text in this file and started
# typing — it would replace what was already there.

# Move onto 021_two_step.py to continue
