# Video alternative: https://vimeo.com/954334103/0aed500d39#t=0

# Congratulations! You've covered all of the key syntax,
# concepts, and ideas necessary to succeed in your
# assessment. You can take it now if you like, though you
# might be a little stronger if you do these extra
# challenges.

# Each challenge focuses on a new technique or approach. It
# starts with an example, and then leads into an exercise.

# We'll start with combining filtering, mapping, and
# summarising into one super-brilliant pipeline.

# I'll demonstrate for you a function that:
#
# * Gets rid of junk data
# * Converts negative integers to positive numbers
# * Creates a graph of how frequently each number shows up
#
# If you've not used the videos so far, you might want to
# do so for this one. It will show you how I build up the
# program piece by piece.

example_numbers = [1, 2, 3, -2, -2, 2, None, -3, 4, 4, None, 3, 3, 2, 2, 1]

# Desired output:
# 1: xx
# 2: xxxxxx
# 3: xxxx
# 4: xx

# First I'll show you the function that will combine all
# the other functions together to create the graph.
# This will give you an idea of the flow of the program.
def generate_frequency_graph(numbers):
  integers = get_only_integers(numbers)
  positive_integers = convert_negatives_to_positives(integers)
  number_frequency = calc_frequency_of_numbers(positive_integers)
  graph = format_graph(number_frequency)
  return graph

# Here we'll use filtering to get rid of the None values
def get_only_integers(numbers):
  integers = []
  for number in numbers:
    if number != None:
      integers.append(number)
  return integers

# Here we'll use mapping to convert negative numbers to
# positive numbers
def convert_negatives_to_positives(numbers):
  positive_integers = []
  for number in numbers:
    if number < 0:
      # Note that a negative number multiplied by -1
      # will be its positive equivalent
      positive_integers.append(number * -1)
    else:
      positive_integers.append(number)
  return positive_integers

# Here we'll use dictionary summarising to create a graph of
# how frequently each number shows up
def calc_frequency_of_numbers(numbers):
  number_frequency = {}
  for number in numbers:
    if number not in number_frequency:
      number_frequency[number] = 1
    else:
      number_frequency[number] += 1
  return number_frequency

# Here we'll use summarising and mapping in the same loop to
# format the graph.
def format_graph(number_frequency):
  graph = ""
  for number in number_frequency:
    # Note the cool use of 'string multiplication' here!
    # 'x' * 3 will give you 'xxx'
    graph += f"{number}: {'x' * number_frequency[number]}\n"
  return graph

# Now let's use it!
print(generate_frequency_graph(example_numbers))

# @TASK Run this file to see the result.

# Once you're done, move on to 040_challenge_1_exercise.py
