import pygame
from cell import Cell

# pygame setup
# ~ pygame.init()
# ~ screen = pygame.display.set_mode((W, H))
pygame.init()
LEFT = 1
RIGHT = 3
W = 700
H = 700
NUMBER_OF_MINES = 5
IS_GAME_OVER = False
ROWS = 10
COLS = 10
OF_SET = 2
FONT_OF_SET = W / ROWS / 3
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont(None, 50)
game_over_font = pygame.font.SysFont(None, 140)

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
        img = font.render("F", True, "green")
        screen.blit(img, (theCell.theRect.left + FONT_OF_SET, theCell.theRect.top + FONT_OF_SET))
    elif not theCell.isOpen and not theCell.isFlaged:                
        pygame.draw.rect(screen, theCell.theColor, theCell.theRect)

