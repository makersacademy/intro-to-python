# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

#def report_long_words(words):
  #my_report = []
 # for word in words:
  #   count_chars = len(word)
  #   is_word_too_long = count_chars > 10
   #   is_word_hyphenated = "-" in word
    #  if is_word_too_long and not is_word_hyphenated:
     #   my_report.append(word)

      #is_word_way_too_long = count_chars > 15
      #if is_word_way_too_long:
       # word.shorten(count_chars, 15)
        #word.join("...", [-1])
   
 # return my_report

def report_long_words(words):
    my_report = []
    for word in words:
        if len(word) > 10 and "-" not in word:
            my_report.append(word)
    return my_report

def shorten_very_long_words(words):
    new_words = []
    for word in words:
      if len(word) > 15:
       shortened_word = word[0:15] + "..."
       new_words.append(shortened_word)
    else:
     new_words.append(word)
    return new_words        


check_that_these_are_equal(
    report_long_words([
        'hello',
        'nonbiological',
        'Kay',
        'this-is-a-long-word',
        'antidisestablishmentarianism'
    ]),
    "nonbiological, antidisestablishm..."
)

      
      
  #pass

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
