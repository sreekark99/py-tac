def display(board):
    row = 0
    for i in range(0, 5, 1):
        if i % 2 == 0:
            for j in range(0, 3, 1):
                if j == 2:
                    print(board[row][j], end="")
                    continue
                else:
                    print(board[row][j], end="|")
            row += 1
        else:
            print("\n"+"-"*5)
    print()


def display_demo():
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            print("row" + str(i+1) + " col" + str(j+1), end="|")
        if i == 2:
            continue
        else:
            print("\n"+"-"*30)
    print()


def row_check(board):
    # Check for non-complete rows
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if board[i][j] == " ":
                break
            else:
                continue
        if j == 2:
            #row is complete
            res = (board[i][0] == board[i][1] == board[i][2])
            if res == True:
                return True
    return False


def col_check(board):
    # check for non-complete  columns
    for j in range(0, 3, 1):
        for i in range(0, 3, 1):
            if board[i][j] == " ":
                break
            else:
                continue
        if i == 2:
            #col is complete
            res = (board[0][j] == board[1][j] == board[2][j])
            if res == True:
                return True
    return False


def one_diag_check(board):
    i = j = 0
    while(i < 3) and (j < 3):
        if board[i][j] == " ":
            return False
        i += 1
        j += 1
    return board[0][0] == board[1][1] == board[2][2]


def two_diag_check(board):
    i = 0
    j = 2
    while(i < 3) and (j > -1):
        if board[i][j] == " ":
            return False
        i += 1
        j -= 1
    return board[0][2] == board[1][1] == board[2][0]


def is_empty(board, row, col):
    if(board[row-1][col-1] == " "):
        return True
    return False


def user(board, p1, p2):
    res = -1
    ctr = 0
    while(ctr < 9):
        if(ctr % 2) == 0:
            # player 1
            input_flag = False
            while(input_flag != True):
                display_demo()
                looper = False
                while(looper != True):
                    try:
                        row, col = map(int, input(
                            f">> Enter row and column number for 'X', {p1}: ").split())
                    except ValueError:
                        print(
                            f">> Check what you have typed {p1}. Type again carefully <<")
                    else:
                        looper = True
                print()`
                if((row > 3) or (row < 1)) or ((col > 3) or (col < 1)):
                    print(f">> Please enter a valid number, {p1} <<")
                    print()
                    input_flag = False
                else:
                    if(is_empty(board, row, col) == True):
                        input_flag = True
                    else:
                        print(
                            f">> Position already occupied, {p1}. Choose another place <<")
                        print()
                        input_flag = False
            board[row-1][col-1] = "X"
            display(board)
            if(row_check(board) == True) or (col_check(board) == True) or (one_diag_check(board) == True) or (two_diag_check(board) == True):
                res = "P1"
                return res
        else:
            # player 2
            input_flag = False
            while(input_flag != True):
                display_demo()
                looper = False
                while(looper != True):
                    try:
                        row, col = map(int, input(
                            f">> Enter row and column number for 'O', {p2}: ").split())
                    except ValueError:
                        print(
                            f">> Check what you have typed {p2}. Type again carefully <<")
                    else:
                        looper = True
                print()
                if((row > 3) or (row < 1)) or ((col > 3) or (col < 1)):
                    print(f">> Please enter a valid number, {p2} <<")
                    print()
                    input_flag = False
                else:
                    if(is_empty(board, row, col) == True):
                        input_flag = True
                    else:
                        print(
                            f">> Position already occupied, {p2}. Choose another place <<")
                        print()
                        input_flag = False
            board[row-1][col-1] = "O"
            display(board)
            if(row_check(board) == True) or (col_check(board) == True) or (one_diag_check(board) == True) or (two_diag_check(board) == True):
                res = "P2"
                return res
        ctr += 1
        print("_"*35)


print("Hello There!")
while(True):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    p1_name = input(">> What's your name, Player 1? ").split()
    while(len(p1_name) != 1):
        print("Enter your name! Don't worry I won't store it")
        p1_name = input(">> What's your name, Player 1? ").split()
    p1_name = p1_name[0]
    p2_name = input(">> What's your name, Player 2? ").split()
    while(len(p2_name) != 1):
        print("Enter your name! Don't worry I won't store it")
        p2_name = input(">> What's your name, Player 2? ").split()
    p2_name = p2_name[0]
    print()
    print(p1_name + " goes X")
    print(p2_name + " goes O")
    print()
    res = user(board, p1_name, p2_name)
    print("^"*35)
    if res == "P1":
        print(f"Hooray! {p1_name} Wins!")
    elif res == "P2":
        print(f"Hooray! {p2_name} Wins!")
    else:
        print(f"DRAW, Good Game {p1_name} and {p2_name}!")
    print("^"*35)
    print("Type 'EXIT' to leave the game (or) Press any other key to start playing again!")
    if (input().lower() == "exit"):
        break
