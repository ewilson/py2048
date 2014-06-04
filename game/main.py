import os
from board import Board
from term_io import display, get_input

if __name__ == '__main__':
    b = Board()
    success = b.place_random()
    success = b.place_random()
    while success:
        os.system('cls' if os.name == 'nt' else 'clear')
        print display(b)
        direction = get_input()
        if b.slide(direction):
            success = b.place_random()
