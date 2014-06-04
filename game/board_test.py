from board import Board

def test_board_slide_left_without_merge():
    b = Board()
    b.tiles[(0,1)]= 2
    b.tiles[(0,3)]= 4
    b.tiles[(1,1)]= 2
    b.tiles[(3,2)]= 8

    b.slide_left()

    assert b.tiles == {(0,0):2,(0,1):4,(1,0):2,(3,0):8}

def test_board_slide_right_without_merge():
    b = Board()
    b.tiles[(0,1)]= 2
    b.tiles[(0,3)]= 4
    b.tiles[(1,1)]= 2
    b.tiles[(3,2)]= 8

    b.slide_right()

    assert b.tiles == {(0,2):2,(0,3):4,(1,3):2,(3,3):8}

def test_board_slide_up_without_merge():
    b = Board()
    b.tiles[(0,1)]= 2
    b.tiles[(0,3)]= 4
    b.tiles[(2,1)]= 3
    b.tiles[(3,2)]= 8

    b.slide_up()

    assert b.tiles == {(0,1):2,(0,3):4,(1,1):3,(0,2):8}

def test_board_slide_down_without_merge():
    b = Board()
    b.tiles[(0,1)]= 2
    b.tiles[(0,3)]= 4
    b.tiles[(2,1)]= 3
    b.tiles[(3,2)]= 8

    b.slide_down()

    assert b.tiles == {(2,1):2,(3,3):4,(3,1):3,(3,2):8}