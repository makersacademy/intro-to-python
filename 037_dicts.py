# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=510

# Here are the data structures we've met so far:

# * Strings: A sequence of characters
# * Lists: A sequence of any item

# We're going to add another one:

# * Dictionaries: A collection of keys mapped to values

# You know how in a dictionary you look up a word and it
# provides a definition? In that sense, the 'word' is the
# key, and the 'definition' is the value.

# We'll use that example for a programming dictionary too:

my_dictionary = {
  "String": "A sequence of characters",
  "List": "A sequence of any item",
}

# Note that:
#
# * We use braces `{` and `}` to tell Python that this is a
#   dictionary
# * We use commas `,` to separate pairs
# * We use colons `:` to separate keys and values

# Now let's look something up. It's just like a list:

print("A String is:")
print("  " + my_dictionary["String"])

print("A List is:")
print("  " + my_dictionary["List"])

# @TASK: Add a definition for a "Dictionary" to our
# dictionary above by editing the code around line 21. Then
# print out the value below.

print("A Dictionary is:")
# ...

# Once you're done, move on to 038_dict_operations.py
