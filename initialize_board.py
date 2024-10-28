def initialize_board():
  board = []
  for i in range(9):
    initial_board = []
    for j in range(9):
      initial_board.append(0)
    board.append(initial_board)
  return board
