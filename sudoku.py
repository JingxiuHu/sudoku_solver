#Jingxiu Hu 872825747
#Sudoku solver for 6*6 puzzles
import copy
import display

class puzzle:
    def __init__(self,board):
        '''Take a two dimensional array of ints as parameter.
           Then solve the 6*6 sudoku.'''
        # set the board attribute with a deep copy of the board parameter
        self.board = copy.deepcopy(board)
        #if the given board is not a list containing six lists of integers
        #between 0 and 6
        if type(board) is not list or (len(board) != 6):
            raise ValueError(f'type of board is not list or length of boad'
                             f'is not 6')
        if not all(type(row) is list for row in board):
            raise ValueError(f'type of row is not list')
        if not all(len(row) == 6 for row in board):
            raise ValueError(f'length of row is not 6')
        for row in board:
            if not all(type(num) is int for num in row):
                raise ValueError('type of num is not int')
            if any(num > 6 for num in row) or any(num < 0 for num in row):
                raise ValueError('num is not between 0 and 6')


    def __str__(self):
        # return a human-readable string representation of the board.
        str_board = ''
        #add newline to end at every two row
        for i,sub_list in enumerate(self.board):
            if i % 2 == 0 and i != 0:
                str_board += '\n'
            #seperate each column to 3 and 3
            for i,element in enumerate(sub_list):
                if i == 3:
                    str_board += ' '
                #0 is represent by '_'
                if element == 0:
                    element = '_'
                str_board += str(element)
                str_board += ' '
            #new line at the end of evey row
            str_board += '\n'
        #get rid of the last row of new line
        str_board = str_board[:-1]
        return str_board

    def options(self,row,col):
        '''Take two parameter, an int represent the row and a int represent the
            column. Then return a set of all possible value could legally fit
            in the given row and column.'''
        options_set = {1,2,3,4,5,6}
        #set the upper_let coordinate according to row and col
        if row <= 1 and col <= 2:
            upper_left_x = 0
            upper_left_y = 0
        elif 2 <= row <= 3 and col <= 2:
            upper_left_x = 2
            upper_left_y = 0
        elif 4 <= row <= 5 and col<= 2:
            upper_left_x = 4
            upper_left_y = 0
        elif row <= 1 and 3 <= col <= 5:
            upper_left_x = 0
            upper_left_y = 3
        elif 2 <= row <= 3 and 3 <= col <= 5:
            upper_left_x = 2
            upper_left_y = 3
        elif 4 <= row <= 5 and 3 <= col <= 5:
            upper_left_x = 4
            upper_left_y = 3
        #if that space is already filled, it should return an empty set
        if self.board[row][col] != 0:
            options_set = set()
            return options_set
        else:
            #If that space is blank, it should return a set of all values that
            #could be legally placed into this square.
            for i in range(6):
                #get rid of int that are in the given row and column
                options_set.discard(self.board[row][i])
                options_set.discard(self.board[i][col])
            #get rid of the int that are given in the 2*3 square
            for i in range(2):
                for j in range(3):
                    options_set.discard(self.board[upper_left_x+i][upper_left_y+j])
            return options_set

    def solve(self):
        '''Recursively solve the puzzle.  return a boolean stating whether or
            not the puzzle was solved. It should return True if a solution was
            found, and False if no solution exists'''
        #display the puzzle
        display.display(puzzle(self.board))
        have_blank_space = False
        #serach for blank space
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == 0:
                    have_blank_space = True
        #if no blank space is find return True
        if have_blank_space == False:
            return True
        else:
            #if there is blank space
            for i in range(6):
                for j in range(6):
                    if self.board[i][j] == 0:
                        # calculate all possible values that could go in the space
                        possible_value = puzzle(self.board).options(i,j)
                        #If none of the previous values worked, reset this
                        #coordinate to blank and return False
                        if possible_value == set():
                            return False
                        else:
                            #fill in the blank space with that value
                            for n in possible_value:
                                self.board[i][j] = n
                                if puzzle(self.board).solve() == False:
                                    pass
                                else:
                                    return True
                            return False

def main():
    puzzle_board = []
    #Loads a puzzle from a file and fill puzzle_board with them
    with open('puzzle2.txt') as f:
        for line in f:
            row = line[:-1].split()
            row = [int(i) for i in row]
            puzzle_board.append(row)

    #solves that Puzzle with the solve() method.
    puzzle(puzzle_board).solve()

#Script runs the main() function if executed, but not if it is imported.
if __name__ == '__main__':
    main()
