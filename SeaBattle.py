class Board:
    def __init__(self, size=10):
        self.size = size
        self.cell_width = 3
        self.cells = [['   ' for _ in range(size)] for _ in range(size)]
        
    def print_separator(self):
        separator = '   ' + '-'*self.cell_width*self.size + '\n'
        print(separator.rstrip())
        
    def print_board(self):
        # Print column headers
        print('  |', end='')
        for col in range(self.size):
            print('{:^{}}|'.format(col, self.cell_width), end='')
        print()
        
        self.print_separator()

        # Print each row and row number
        for row in range(self.size):
            print('{:>2}|'.format(row), end='')
            for col in range(self.size):
                print('{:^{}}|'.format(self.cells[row][col], self.cell_width), end='')
            print()
            
            self.print_separator()
             # Создание игрового поля
board = Board()

# Вывод игрового поля
board.print_board()