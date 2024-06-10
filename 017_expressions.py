# Video alternative: https://vimeo.com/954334376/0c486313d0#t=0

# Now, let's look at expressions. You've actually already
# seen them a lot!

added = 2 + 3

# Is this an expression? Not quite. It does contain an
# expression though.

# The expression part is this:

2 + 3

# The expression is the fundamental unit of computation in
# your program. It is the combination of data and operators
# (and some other things) to produce a result.

# Here are some more examples of expressions:

2            # Evaluates to: 2
2 + 3        # Evaluates to: 5
2 * 3        # Evaluates to: 6
2 + 3 * 4    # Evaluates to: ...???

# Well, what is that last one?
#
# Do we take 2 + 3 making 5, then multiply by 4 to get 20?
#
# Or do we multiply 3 * 4 to get 12, then add 2 to get 14?
#
# @TASK: You can find out by running `python` in your
# shell and typing that code into it. You'll see
# something like this:
#
# ```
# Python 3.10.9 (main, Dec 15 2022, 10:44:50) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 2 + 3 * 4
# 14
# >>>
# ```
#
# You can then type in 'exit()' to leave Python.
#
# So we get 14! Python executes the multiplication first,
# and then the addition. We can control this using brackets.
#
# @TASK: Try this using `python` in the shell:

(2 + 3) * 4

# As you can see, we can use brackets to control the order
# the expressions are evaluated.

# That handy "`python` in the shell" thing is called the
# Python REPL. REPL stands for Read, Evaluate, and Print
# Loop. It reads the code you type in, evaluates the
# expression, prints the result, and then does that forever
# in a loop.
#
# You can use it to find out what different expressions
# evaluate to, and generally play around with Python to see
# what it does.

# I'm going to reintroduce the `add_one` function:

def add_one(num):
  return num + 1

# Here are some more expressions:

add_one(2)          # Evaluates to 3
add_one(3)          # Evaluates to 4
add_one(4) * 3      # Evaluates to 15
2 + add_one(4) * 3  # Evaluates to 17

# What to take from this? Calling a function is also an
# expression! Many things in Python are expressions, and we
# can combine data, operators, and function calls into some
# very advanced expressions.

# @TASK: Try those expressions yourself. Run:
#
#   python -i 017_expressions.py
#
# And then type in some of the above expressions.
#
# The `-i` flag means 'open a REPL that can use the code in
# this file'

# To finish off, here's a real mind-bender:

add_one(add_one(add_one(add_one(add_one(add_one(1))))))

# @TASK: What do you think that evaluates to? And why? Give
# it a go and find out.

# @TASK: Play around with building complex expressions in
# the space below.

# EXPRESSIONS PLAYGROUND BEGINS



# EXPRESSIONS PLAYGROUND ENDS

# When you're done, move on to 018_statements.py
