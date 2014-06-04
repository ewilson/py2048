import os
from board import Board
from term_io import display, get_input

def display_new_board(b):
    os.system('cls' if os.name == 'nt' else 'clear')
    print display(b)
    print b.score

if __name__ == '__main__':
    b = Board()
    success = b.place_random()
    success = b.place_random()
    while success:
        display_new_board(b)
        direction = get_input()
        if b.slide(direction):
            b.place_random()
        success = b.check_for_moves()
    else:
        display_new_board(b)
        print "Game Over"
