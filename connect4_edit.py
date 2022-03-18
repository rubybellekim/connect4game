import random

# the winner name will be written in the 'connect4_winner.txt'

# differences from tic-tac-toe
# 1. winning condition (3 -> 4)
# 2. input move is different
# 3. field size is different

def input_players():
    player1 = input("please enter player1's name: ")
    player2 = input("please enter player2's name: ")
    return player1, player2

def display_gamefield(field):
    # field = [["X", "O", "X"],
    #         ["X", "O", "X"],
    #         ["X", "O", "X"]]
    w = len(field[0])  #decide width (0 index of the field(->["X", "O", "X"])
    h = len(field)  #decide height
    divider = "----" * (w + 1)

    print("")
    print("")

    #column numbers
    print("   |", end="")
    for c in range(w):
        print(f" {c + 1} ", end="")
        #print '|' until last col
        if c != w - 1:
            print("|", end="")
    print(f"\n{divider}")

    for r in range(h):
        #print row numbers
        print(f" {r + 1} |", end="")
        for c in range(w):
            curValue = field[r][c]
            if curValue == "":
                curValue = " "
            print(f" {curValue} ", end="")
            if c != w - 1:
                print("|", end="")
        print("")
        if r != h - 1:
            print(divider)


def input_move(field, player):
    while True:
        move = input(f"{player} Enter the index of your next movement(column) : ")
        r = -1
        c = int(move)
        rows_count = len(field)
        cols_count = len(field[0])

        if c <= cols_count and c > 0:
            c -= 1
            # decide which row is available
            a = rows_count - 1
            while a >= 0:
                #do stuff
                if field[a][c] == "":
                    r = a
                    break
                a -= 1
            # found row index
            if r >= 0:
                break
    return (r, c)


# check we have a winning condition in the game field
# return "X" if X is a winner
# return "O" if O is a winner
# return "D" if it's a draw
# return "" if game should continue
def result_game(field):
    result = ""
    rowsCount = len(field)
    colsCount = len(field[0])

    # print("TEST ROWS")
    r = 0
    # r from ZERO till rows count (len of fields)
    while r < rowsCount:
        # currentRow = field[r]
        # winner can be: "X", "O", ""
        winner = check_items_count(field[r], 4)
        if winner != "":
            return winner
        c = 0
        # c from ZERO till columns count (len of current row)
        while c < colsCount:
            # print(f"({field[r][c]}) ", end="")
            c += 1
        # print()
        r += 1

    # print()
    # print("TEST COLS")

    c = 0
    while c < colsCount:
        r = 0
        col_items = []
        while r < rowsCount:
            # print(f"({field[r][c]}) ", end="")
            col_items.append(field[r][c])
            r += 1
        # print()
        winner = check_items_count(col_items, 4)
        if winner != "":
            return winner
        c += 1

    # print()
    # print("TEST DIAGONAL (\)")

    r = 0
    while r < rowsCount:
        c = 0
        while c < colsCount:
            d_r = r
            d_c = c
            diag_items = []
            while d_c < colsCount and d_r < rowsCount:
                # print(f"({field[d_r][d_c]}) ", end="")
                diag_items.append(field[d_r][d_c])
                d_r += 1
                d_c += 1
            # print()
            c += 1
            winner = check_items_count(diag_items, 4)
            if winner != "":
                return winner
        r += 1

    # print()
    # print("TEST DIAGONAL (/)")

    r = 0
    while r < rowsCount:
        c = 0
        while c < colsCount:
            d_r = r
            d_c = c
            diag_items = []
            while d_c >= 0 and d_r < rowsCount:
                # print(f"({field[d_r][d_c]}) ", end="")
                diag_items.append(field[d_r][d_c])
                d_r += 1
                d_c -= 1
            # print()
            winner = check_items_count(diag_items, 4)
            if winner != "":
                return winner
            c += 1
        r += 1

    # if we are here then we dont have winners
    # but we need to check if feald is FULL or NOT
    # to decide DRAW
    for row in field:
        if "" in row:
            return ""
    return "D"


def create_field(w, h):
    return [ ["" for c in range(w)] for r in range(h)]
    # return [["", "", ""], ["", "", ""], ["", "", ""]]

    # [ [] for r in range(h)] => [["". "", ""], [], []]
    # [x + 1 for x in range(3)] => [1, 2, 3]

    # l = []
    # for x in range(3):
    #     l.append(x)


def check_items_count(items, count):
    search_value = items[0]
    counter = 0
    for x in items:
        if x == search_value:
            counter += 1
            # check if we have found right amount of items
            if counter == count:
                break
        else:
            search_value = x
            counter = 1
    # counter is 1
    # search value is 2
    if counter != count:
        search_value = ""
    return search_value


def winner_list(player):
    with open("./connect4_winner.txt", "a") as f:
        f.write(f"the winner is {player}" + "\n")



# a = ["a", "b", "b", "b", "E", "E", "b", "E", "c", "c", "c", "d"]
# a = ["", "X", "O", "O", "O", "O", "X"]
# result = check_items_count(a, 4)
# if result == "O":
#     print("OK")
# else:
#     print(f"ERROR. should be c, but got ({result})")
# exit()

# field = [["X", "O", "X", "", "X", ""],
#         ["X", "O", "X", "", "", "O"],
#         ["", "O", "X", "", "X", ""],
#         ["X", "X", "X", "X", "", ""],
#         ["X", "O", "X", "", "", "O"]]
# field = []
# for r in range(5):
#     field.append([])
#     for c in range(7):
#         field[r].append(r * 7 + c)
# result_game(field)
#
# exit()

(player1, player2) = input_players()

continueGame = True

while continueGame == True:
    player_num = random.randint(1, 2)
    if 1 == player_num:
        current_player = player1
    else:
        current_player = player2

    field = create_field(6, 7)
    while True:
        display_gamefield(field)

        (r, c) = input_move(field, current_player)
        if current_player == player1:
            field[r][c] = "X"
        elif current_player == player2:
            field[r][c] = "O"

        display_gamefield(field)

        status = result_game(field)

        if status == "D":
            print("The game is draw")
            break
        elif status == "O" or status == "X":
            print("")
            print(f"****** Player '{current_player}' is win ! ******")
            # write winner to file ./winners.txt
            winner_list(current_player)
            print("")
            break
        else:
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
    # continue or exit
    user_exit = input("Enter 'c' to continue, 'x' to quit: ")
    if user_exit == "x":
        break


    # if user_exit == "c":
    #     if continueGame == True:
    #
    # elif user_exit == "x":
    #     break


