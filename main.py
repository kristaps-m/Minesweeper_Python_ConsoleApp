from cell import Cell
from minesweeper import Minesweeper

NUMBER_OF_MINES = 5; # 10 mines is standart beginer setting
ROWS = 9
COLS = 9
IS_GAME_OVER = False

print("Welcome to Minesweeper")
print("MINE: * ")
print("Closed Cell: # ")
print("Opened Cell: |  | ")
print("Number of mines: | 3 | ")

# define field
def generate_game_field():
    new_field = []
    for r in range(ROWS):
        temp_array = []
        for c in range(COLS):
            # append full cell, because we need to add row and col cordinates
            temp_array.append(Cell(False, False, False, 0, r, c))
        new_field.append(temp_array)
        
    return new_field
    
field = generate_game_field()

# Simple Field for testing or to demonstrate how field looks
# ~ field = [
    # ~ [Cell(),Cell(),Cell(),Cell(),Cell()],
    # ~ [Cell(),Cell(),Cell(),Cell(),Cell()],
    # ~ [Cell(),Cell(),Cell(),Cell(),Cell()],
    # ~ [Cell(),Cell(),Cell(),Cell(),Cell()],
    # ~ [Cell(),Cell(),Cell(),Cell(),Cell()]
# ~ ]

# rows = 9, cols = 9, number_of_mines = 10, field
m = Minesweeper(ROWS, COLS, NUMBER_OF_MINES, field, IS_GAME_OVER)
m.play_game()


