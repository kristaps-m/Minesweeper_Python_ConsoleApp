import pygame
from pygame_helper import *

# pygame setup is inside py_game_help.py file

new_game_button = pygame.Rect(NEW_GAME_BUTTON_X, NEW_GAME_BUTTON_Y, 200, 80)
decrease_mines_btn = pygame.Rect(W + 50, 300, 80, 80)
add_more_mines_btn = pygame.Rect(W + 200, 300, 80, 80)
flaged_cells_counter = 0

def render_text(font_size, text, color, x, y):
    the_font = pygame.font.SysFont(None, font_size)
    img = the_font.render(text, True, color)
    screen.blit(img, (x, y))

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
                        if event.button == LEFT and not m.check_if_game_won() and not IS_GAME_OVER:
                            m.cell_simulate_left_click(f_col.row, f_col.col)
                            if m.isGameOver:
                                # ~ running = False
                                IS_GAME_OVER = True
                                break
                        elif event.button == RIGHT and not f_col.isOpen and f_col.isFlaged and not IS_GAME_OVER:
                            f_col.isFlaged = False
                            flaged_cells_counter -= 1
                        elif event.button == RIGHT and not f_col.isOpen and not IS_GAME_OVER:
                            f_col.isFlaged = True
                            flaged_cells_counter += 1
            
            if add_more_mines_btn.collidepoint(mouse_pos) and (IS_GAME_OVER or m.check_if_game_won()):
                if NUMBER_OF_MINES < ROWS * COLS - 1:
                    NUMBER_OF_MINES += 1

            if decrease_mines_btn.collidepoint(mouse_pos) and (IS_GAME_OVER or m.check_if_game_won()):
                if NUMBER_OF_MINES > 1:
                    NUMBER_OF_MINES -= 1
                
            if new_game_button.collidepoint(mouse_pos):
                print("Create New Game Here!!!!")
                # ~ create_new_game()
                IS_GAME_OVER = False
                game_field = generate_game_field()
                m = Minesweeper(ROWS, COLS, NUMBER_OF_MINES, game_field, IS_GAME_OVER)
                m.add_mines_to_game_field()
                m.add_big_numbers_near_mines()
                flaged_cells_counter = 0
                # ~ print(f"{IS_GAME_OVER}")

        # Keyboard events:
        # if event.type == pygame.KEYUP:
            # if event.key == pygame.K_F11:
            #     print("K F11 pressed")

    SHOW_MINES_CHEAT = get_multiple_keys_pressed() # sets true if 2 secret keys on keyboard are pressed
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    for f_row in m.field:
        for f_col in f_row:
            if_cell_is_open_function(f_col, IS_GAME_OVER)
    
    if SHOW_MINES_CHEAT:
        show_mines_if_cheat_key_pressed(m.field) # draws square where mines if cheat is on :P
            
    pygame.draw.rect(screen, "yellow", new_game_button)
    pygame.draw.rect(screen, "#93f59d", decrease_mines_btn)
    render_text(200, "-", "white", W + 60, 270)
    pygame.draw.rect(screen, "#f59b93", add_more_mines_btn)
    render_text(200, "+", "white", W + 200, 265)

    render_text(40, "Decrease or Add mines\n when Game is Over!", "white", W + 25, 210)

    img = new_game_font.render("New Game", True, "brown")
    screen.blit(img, (NEW_GAME_BUTTON_X + 15, NEW_GAME_BUTTON_Y + 25))
            
    render_text(50, "F: " + str(flaged_cells_counter), "white", W+65, 100)
                    
    render_text(60, f"mines: {NUMBER_OF_MINES}", "red",W+65, 10)
            
    if IS_GAME_OVER:
        img = game_over_font.render(" GAME OVER!! ", True, "red")
        screen.blit(img, (0, H / 2))        

    if m.check_if_game_won() and not IS_GAME_OVER:
        img = game_over_font.render(" VICTORY!!! ", True, "green")
        screen.blit(img, (0, H / 2))
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
