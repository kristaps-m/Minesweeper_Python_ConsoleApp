import pygame
import math
from cell import Cell
from minesweeper import Minesweeper
# ~ print("Is PyGame imported?")

# pygame setup
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
# ~ img = font.render('hello', True, BLUE)
# ~ screen.blit(img, (20, 20))


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


# ~ game_cell = PyGameCell()
# ~ rect = pygame.Rect(10, 20, 30, 30)

game_field = generate_game_field()

m = Minesweeper(ROWS, COLS, NUMBER_OF_MINES, game_field, IS_GAME_OVER)
m.add_mines_to_game_field()
m.add_big_numbers_near_mines()
# ~ m.cell_simulate_left_click(0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"rMP =  {mouse_pos[0]},{mouse_pos[1]}")
            # ~ if rect.collidepoint(mouse_pos):
                # ~ print("rect.collidepoint(mouse_pos) WORKS?!")
                # ~ game_cell.theColor = "gray"
            for f_row in game_field:
                for f_col in f_row:
                    if f_col.theRect.collidepoint(mouse_pos):
                        if event.button == LEFT:
                                # ~ f_col.theColor = "gray"
                            m.cell_simulate_left_click(f_col.row, f_col.col)
                            if m.isGameOver:
                                running = False
                            if m.check_if_game_won():
                                print("- VICTORY!!!!!!!!! -")
                                break
                        elif event.button == RIGHT and not f_col.isOpen and f_col.isFlaged:
                            f_col.isFlaged = False
                        elif event.button == RIGHT and not f_col.isOpen:
                            f_col.isFlaged = True

                        print(f"{f_col.isFlaged}")
            
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # ~ pygame.draw.rect(screen, game_cell.theColor, rect)
    for f_row in m.field:
        for f_col in f_row:
            # ~ pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
            """ ADD THIS ALL BELOW IN FUNCTION? """
            if f_col.isOpen:
                f_col.theColor = "gray"
                pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
                if f_col.numOfMines > 0:
                    img = font.render(str(f_col.numOfMines), True, "black")
                    screen.blit(img, (f_col.theRect.left + FONT_OF_SET, f_col.theRect.top + FONT_OF_SET))
            elif not f_col.isOpen and f_col.isFlaged:                
                pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
                img = font.render("F", True, "green")
                screen.blit(img, (f_col.theRect.left + FONT_OF_SET, f_col.theRect.top + FONT_OF_SET))
            elif not f_col.isOpen and not f_col.isFlaged:                
                pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
                # ~ img = font.render("F", True, "green")
                # ~ screen.blit(img, (f_col.theRect.left + FONT_OF_SET, f_col.theRect.top + FONT_OF_SET))
            elif not f_col.isOpen:
                f_col.theColor = "pink"
                pygame.draw.rect(screen, f_col.theColor, f_col.theRect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
