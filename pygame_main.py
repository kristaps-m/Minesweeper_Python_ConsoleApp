import pygame
from pygame_helper import *

# pygame setup is inside py_game_help.py file

new_game_button = pygame.Rect(W+50,H/2,200,80)

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
            
                
            if new_game_button.collidepoint(mouse_pos):
                print("Create New Game Here!!!!")
                # ~ create_new_game()
                IS_GAME_OVER = False
                game_field = generate_game_field()
                m = Minesweeper(ROWS, COLS, NUMBER_OF_MINES, game_field, IS_GAME_OVER)
                m.add_mines_to_game_field()
                m.add_big_numbers_near_mines()
                print(f"{IS_GAME_OVER}")
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    for f_row in m.field:
        for f_col in f_row:
            if_cell_is_open_function(f_col, IS_GAME_OVER)
            
    pygame.draw.rect(screen, "yellow", new_game_button)
    img = new_game_font.render("New Game", True, "brown")
    screen.blit(img, (W+65,H/2 + 25))
            
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
