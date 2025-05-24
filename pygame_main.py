import pygame
from minesweeper import Minesweeper
from pygame_helper import *

# pygame setup is inside py_game_help.py file

game_field = generate_game_field()

m = Minesweeper(ROWS, COLS, NUMBER_OF_MINES, game_field, IS_GAME_OVER)
m.add_mines_to_game_field()
m.add_big_numbers_near_mines()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            for f_row in game_field:
                for f_col in f_row:
                    if f_col.theRect.collidepoint(mouse_pos):
                        if event.button == LEFT and not m.check_if_game_won():
                            m.cell_simulate_left_click(f_col.row, f_col.col)
                            if m.isGameOver:
                                # ~ running = False
                                IS_GAME_OVER = True
                                break
                        elif event.button == RIGHT and not f_col.isOpen and f_col.isFlaged:
                            f_col.isFlaged = False
                        elif event.button == RIGHT and not f_col.isOpen:
                            f_col.isFlaged = True
            
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    for f_row in m.field:
        for f_col in f_row:
            if_cell_is_open_function(f_col, IS_GAME_OVER)
            
    if IS_GAME_OVER:
        img = game_over_font.render(" GAME OVER!! ", True, "red")
        screen.blit(img, (0, H / 2))        

    if m.check_if_game_won():
        # ~ print("- VICTORY!!!!!!!!! -")
        img = game_over_font.render(" VICTORY!!! ", True, "green")
        screen.blit(img, (0, H / 2))
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


# -----------------------------
            # ~ if f_col.isOpen:
                # ~ f_col.theColor = "gray"
                # ~ pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
                # ~ if f_col.numOfMines > 0:
                    # ~ img = font.render(str(f_col.numOfMines), True, "black")
                    # ~ screen.blit(img, (f_col.theRect.left + FONT_OF_SET, f_col.theRect.top + FONT_OF_SET))
            # ~ elif not f_col.isOpen and f_col.isFlaged:                
                # ~ pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
                # ~ img = font.render("F", True, "green")
                # ~ screen.blit(img, (f_col.theRect.left + FONT_OF_SET, f_col.theRect.top + FONT_OF_SET))
            # ~ elif not f_col.isOpen and not f_col.isFlaged:                
                # ~ pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
                # ~ # img = font.render("F", True, "green")
                # ~ # screen.blit(img, (f_col.theRect.left + FONT_OF_SET, f_col.theRect.top + FONT_OF_SET))
            # ~ elif not f_col.isOpen:
                # ~ f_col.theColor = "pink"
                # ~ pygame.draw.rect(screen, f_col.theColor, f_col.theRect)
