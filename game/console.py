from board import Board

def display(board):
    rows = []
    for row in range(4):
        row_list = []
        for col in range(4):
            if (row,col) in board.tiles:
                row_list.append(' %4d ' % board.tiles[(row,col)])
            else:
                row_list.append(' '*6)

        rows.append('|'.join(row_list))
    w = len(rows[0])
    row_delim = '\n' + '-'*w + '\n'
    return row_delim.join(rows)

if __name__ == '__main__':
    b = Board()
    b.tiles = {(0,0):4,(0,1):2,(0,2):2,
               (1,0):4,(1,1):8,(1,2):2,(1,3):128,
               (2,0):16,(2,1):8,(2,2):4,(2,3):8,
               (3,0):4,(3,1):8,(3,3):2}
    print display(b)