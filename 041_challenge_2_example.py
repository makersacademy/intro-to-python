# Video alternative: https://vimeo.com/954334009/67af9910fc#t=0

# Nice work on that last one! You might well want to
# consider taking the assessment at this point.

# However, if you did want some more challenge, here it is.

# We're going to tackle something really sophisticated.
# We're going to build a tic tac toe game!

# This will introduce us to lists of lists. Here's one:

a_list_of_lists = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# And to get items out we index in twice:
a_list_of_lists[0][0] # Evaluates to 1
a_list_of_lists[0][1] # Evaluates to 2
a_list_of_lists[0][2] # Evaluates to 3
a_list_of_lists[1][0] # Evaluates to 4
# Et cetera.

# Looks kind of like a grid right? We can use it to
# represent a tic-tac-toe board:

completed_board = [
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["O", "X", "O"]
]

# We're going to implement a little game. We'll need three
# functions:

# 1. A function to format the board for the user.
# 2. A function to make a move.
# 3. A function to check if the game is over.

# Let's start with formatting the board:

def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

# Let's test it out:

starter_board = [
  [".", ".", "."],
  [".", ".", "."],
  [".", ".", "."]
]

print("Our starting board:")
print(print_board(starter_board))

# Now let's write a function to make a move:

def make_move(board, row, column, player):
  board[row][column] = player
  return board

# And try it out:

print("After a move:")
print(print_board(make_move(starter_board, 0, 0, "X")))

# Now let's write a few functions to check if the game is
# over:

# This function will extract three cells from the board
def get_cells(board, coord_1, coord_2, coord_3):
  return [
    board[coord_1[0]][coord_1[1]],
    board[coord_2[0]][coord_2[1]],
    board[coord_3[0]][coord_3[1]]
  ]

# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return "." not in cells

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return cells[0] == cells[1] and cells[1] == cells[2]

# We'll make a list of groups to check:

groups_to_check = [
  # Rows
  [(0, 0), (0, 1), (0, 2)],
  [(1, 0), (1, 1), (1, 2)],
  [(2, 0), (2, 1), (2, 2)],
  # Columns
  [(0, 0), (1, 0), (2, 0)],
  [(0, 1), (1, 1), (2, 1)],
  [(0, 2), (1, 2), (2, 2)],
  # Diagonals
  [(0, 0), (1, 1), (2, 2)],
  [(0, 2), (1, 1), (2, 0)]
]

def is_game_over(board):
  # We go through our groups
  for group in groups_to_check:
    # If any of them are empty, they're clearly not a
    # winning row, so we skip them.
    if is_group_complete(board, group[0], group[1], group[2]):
      if are_all_cells_the_same(board, group[0], group[1], group[2]):
        return True # We found a winning row!
        # Note that return also stops the function
  return False # If we get here, we didn't find a winning row

# Now let's put it all together:

def play_game():
  board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
  ]
  player = "X"
  while not is_game_over(board):
    print(print_board(board))
    print("It's " + player + "'s turn.")
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    board = make_move(board, row, column, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")

# And try it out:

print("Game time!")
play_game()

# @TASK Run this file to play the game.

# Once you're done, move on to 042_challenge_2_exercise.py
