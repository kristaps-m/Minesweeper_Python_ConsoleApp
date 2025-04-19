class Cell:
    def __init__(self, isMine=False, isOpen=False, isFlaged=False,numOfMines=0, row=0, col=0):
        self.isMine = isMine
        self.isOpen = isOpen
        self.isFlaged = isFlaged
        self.numOfMines = numOfMines
        self.row = row
        self.col = col
        
    def print_all(self):
        print(f"""isMine: {self.isMine} isOpen: {self.isOpen}
        isFlaged: {self.isFlaged} N: {self.numOfMines}
        row: {self.row} col: {self.col}
        """)
