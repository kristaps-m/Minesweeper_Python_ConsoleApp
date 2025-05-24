import pygame
from cell import Cell
from minesweeper import Minesweeper

# pygame setup
# ~ pygame.init()
# ~ screen = pygame.display.set_mode((W, H))
pygame.init()
LEFT = 1
RIGHT = 3
W = 700
H = 700
ADD_W_FOR_MENU = 350
NUMBER_OF_MINES = 15
IS_GAME_OVER = False
ROWS = 10
COLS = 10
OF_SET = 2
FONT_OF_SET = W / ROWS / 3
screen = pygame.display.set_mode((W + ADD_W_FOR_MENU, H))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont(None, 50)
game_over_font = pygame.font.SysFont(None, 140)
new_game_font = pygame.font.SysFont(None, 50)



class PyGameCell(Cell):
    def __init__(self, isMine=False, isOpen=False, isFlaged=False,numOfMines=0, row=0, col=0, theColor="red", theRect=pygame.Rect(0,0,0,0)):
        super().__init__(isMine, isOpen, isFlaged, numOfMines, row, col)
        self.theColor = theColor
        self.theRect = theRect

# define field
def generate_game_field():
    new_field = []
    for r in range(ROWS):
        temp_array = []
        for c in range(COLS):
            # append full cell, because we need to add row and col cordinates
            theRect = pygame.Rect(r*70+OF_SET, c*70+OF_SET, 70-OF_SET, 70-OF_SET)
            temp_array.append(PyGameCell(False, False, False, 0, r, c, "pink", theRect))
        new_field.append(temp_array)
        
    return new_field


def if_cell_is_open_function(theCell, is_game_over):
    if theCell.isOpen:
        # ~ print(f"{is_game_over}")
        if not is_game_over:
            theCell.theColor = "gray"
        elif is_game_over and theCell.isMine:
            theCell.theColor = "red"
        elif is_game_over and not theCell.isMine:
            theCell.theColor = "gray"
        pygame.draw.rect(screen, theCell.theColor, theCell.theRect)
        if theCell.numOfMines > 0:
            img = font.render(str(theCell.numOfMines), True, "black")
            screen.blit(img, (theCell.theRect.left + FONT_OF_SET, theCell.theRect.top + FONT_OF_SET))
    elif not theCell.isOpen and theCell.isFlaged:                
        pygame.draw.rect(screen, theCell.theColor, theCell.theRect)
        img = font.render("F", True, "darkgreen")
        screen.blit(img, (theCell.theRect.left + FONT_OF_SET, theCell.theRect.top + FONT_OF_SET))
    elif not theCell.isOpen and not theCell.isFlaged:                
        pygame.draw.rect(screen, theCell.theColor, theCell.theRect)


game_field = generate_game_field()
m = Minesweeper(ROWS, COLS, NUMBER_OF_MINES, game_field, IS_GAME_OVER)
m.add_mines_to_game_field()
m.add_big_numbers_near_mines()


def create_new_game():
    IS_GAME_OVER = False
    game_field = generate_game_field()
    m = Minesweeper(ROWS, COLS, NUMBER_OF_MINES, game_field, IS_GAME_OVER)
    m.add_mines_to_game_field()
    m.add_big_numbers_near_mines()
