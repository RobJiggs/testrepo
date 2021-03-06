#display board
#play game
#check win
#check tie
#flip player
board=[ "-","-","-",
        "-","-","-",
        "-","-","-"

]
currentplayer = "X"
game_going= True
winner = ""
def displayboard():
    print(board[0]+"|"
          +board[1]+"|"
          +board[2])
    print(board[3]+"|"
          +board[4]+"|"
          +board[5])
    print(board[6]+"|"
          +board[7]+"|"
          +board[8]
          )
def handleturn(str):
    global currentplayer
    print("It's "+ currentplayer +"'s turn." )
    position= input("choose a position from 1-9: ")
    valid= False
    while not valid:
        while position not in ["1","2","3","4","5","6","7", "8","9"]:
            position = input(" Invalid input.Try, again. Choose a position from 1-9: ")
        position=(int(position)-1)
        if board[position] == "-":
            valid= True
        else:
            print("You cant go there. That spot is taken")
    board[position]= currentplayer
    displayboard()
def check_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    rowwin=check_row()
    colwin=check_col()
    diawin=check_dia()

    if rowwin:
        winner=rowwin
    elif colwin:
        winner=colwin
    elif diawin:
        winner=diawin
    else:
        winner=None




def check_if_tie():
    global game_going
    global winner
    if "-" not in board:
        game_going=False


def flipplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer="O"
    elif currentplayer == "O":
        currentplayer= "X"
    return

def check_row():
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    global game_going
    if row1 or row2 or row3:
        game_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return
def check_col():
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    global game_going
    if col1 or col2 or col3:
        game_going=False
    if col1:
        return board[0]
    if col2:
        return board[1]
    if col3:
        return board[2]

    return



def check_dia():
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"

    global game_going
    if dia1 or dia2 :
        game_going = False
    if dia1:
        return board[0]
    elif dia2:
        return board[2]
    return


def playgame():
    global currentplayer
    displayboard()
    while game_going:
        handleturn(currentplayer)
        check_game_over()
        flipplayer()
    if winner == "X" or winner =="O":
        print(winner + " has won the game")
    elif winner != "X" or "O":
        print("tie game")
playgame()
