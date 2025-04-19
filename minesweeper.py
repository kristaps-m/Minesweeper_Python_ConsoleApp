from cell import Cell
import random
DIRECTIONS = [
  # Define adjacent positions
  { "row": -1, "col": 0 },
  { "row": 1, "col": 0 },
  { "row": 0, "col": -1 },
  { "row": 0, "col": 1 },
  # Define Corner positions
  { "row": -1, "col": -1 },
  { "row": 1, "col": 1 },
  { "row": -1, "col": 1 },
  { "row": 1, "col": -1 },
];

class Minesweeper:
    def __init__(self, rows= 9, cols= 9, number_of_mines= 10, field =[], isGameOver= False):
        self.rows = rows
        self.cols = cols
        self.number_of_mines = number_of_mines
        self.field = field
        self.isGameOver = isGameOver
        
        
    # ~ def print_field(self):
        # ~ for row in field:
            # ~ for oneCell in row:
                # ~ oneCell.print_all()
        
    def random_mines_cordinates(self):
        list_of_all_cords = [];
        
        for r in range(self.rows):
            for c in range(self.cols):
                list_of_all_cords.append({"r":r, "c":c})
                
        
        random.shuffle(list_of_all_cords)
        
        return list_of_all_cords[0:self.number_of_mines]
# end of random_mines_cordinates function


    def add_mines_to_game_field(self):
        rand_m_cords = self.random_mines_cordinates()
        
        for c in rand_m_cords:
            self.field[c["r"]][c["c"]].isMine = True
# end of add_mines_to_game_field


    def add_big_numbers_near_mines(self):
        def helper(the_r, the_c):
            mines_c = 0
            
            for r in range(-1, 2):
                for c in range(-1, 2):
                    new_r = the_r+r
                    new_c = the_c+c
                    if new_r >= 0 and new_r < self.rows and new_c >= 0 and new_c < self.cols:
                        if self.field[the_r+r][the_c+c].isMine:
                            mines_c+=1
                    
            return mines_c
        # end of helper()
        
        
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if self.field[r][c].isMine == False:
                    self.field[r][c].numOfMines = helper(r,c)
# end of add_big_numbers_near_mines



    def show_one_cell(self, c):
        if c.isOpen == False:
            return "#"
        elif c.isOpen == True and c.isMine:
            return "*"
        elif c.isOpen == True and c.isFlaged == False:
            return f"{c.numOfMines if c.numOfMines > 0 else ' '}"
        elif c.isOpen:
            return " "       
# end of show_one_cell



    def show_amazing_field(self):
        print("   "+f"{'   '.join([f"{y}" for y in range(self.cols)])}")
        for index, row in enumerate(self.field):
            print(f"{self.field[index][0].row}|"+"|".join([f" {self.show_one_cell(x)} " for x in row]))
            # ~ print("|".join([f" {'*' if x.isMine else x.numOfMines if x.numOfMines > 0 else ' '} " for x in row]))
            print("---" * (len(row)+1) + "-------")
# end of show_amazing_field



    def check_if_game_won(self):
        opened_cells = 0
        
        for row in self.field:
            for one_cell in row:
                if one_cell.isOpen:
                    opened_cells += 1
                    
        return opened_cells == self.rows * self.cols - self.number_of_mines
# end of check_if_game_won
    
    
    
    def cell_simulate_left_click(self, the_row, the_col):
        # isMine=False, isOpen=False, isFlaged=False,numOfMines=0, row=0, col=0
        c = self.field[the_row][the_col]
        c.row = the_row
        c.col = the_col
        # what to do if NOT flaged but IS mine
        if c.isMine and not c.isFlaged:
            print("GAME OVER")
            self.field[c.row][c.col].isOpen = True
            self.isGameOver = True
            # ~ print(isGameOver)
        else:
            # now lets see what hapends when game is not over
            QUEUE = [c] # add clicked cell to queue 
            
            while len(QUEUE) > 0:
                NEW_CELL = QUEUE.pop() # remove LAST element of list and return it
                
                if NEW_CELL:
                    row = NEW_CELL.row
                    col = NEW_CELL.col
                    
                    if not self.field[row][col].isOpen and not self.field[row][col].isFlaged:
                        self.field[row][col].isOpen = True
                        
                        if self.field[row][col].numOfMines == 0 and not self.field[row][col].isFlaged:
                            for d in DIRECTIONS:
                                new_row = row + d["row"]
                                new_col = col + d["col"]
                                
                                if new_row >= 0 and new_row < self.rows and new_col >= 0 and new_col < self.cols:
                                    QUEUE.append(Cell(False, False, False, 0, new_row, new_col))
# end of cell_simulate_left_click ----------------------------------



    def play_game(self):
        self.add_mines_to_game_field()
        self.add_big_numbers_near_mines()
        
        print("-----------------------------------------------")
        # user input and game loop
        while not self.isGameOver:
            
            user_input = input("please enter (row col): ")

            print("input 'row col' please")
            print(user_input)

            user_row = int(user_input.split(" ")[0])
            user_col = int(user_input.split(" ")[1])

            self.cell_simulate_left_click(user_row, user_col)

            isGameWon = self.check_if_game_won()

            self.show_amazing_field()
            
            if isGameWon:
                print("YOU HAVE WON\nCongratulations!")    
                self.isGameOver = True
                
            print("-----------------------------------------------")
