print("SAT SRI AKAAL ")
print()
print("KYA HAAL HAI ?")
input()
print("Aao Zero Kaata Khelen")

board =["_","_","_",
         "_","_","_",
         "_","_","_" ]
player1= input("Player 1 enter your Name ")
player2= input("Player 2 enter your Name ")
print(player1 + "is X and " + player2 + "is O")
game_still_going = True
winner= None
current_player ="X"
def displayy():
    print(board[0] + " " + board[1] + " " + board[2] )
    print(board[3] + " " + board[4] + " " + board[5] )
    print(board[6] + " " + board[7] + " " + board[8] )

def play_game():
    displayy()
    

    while game_still_going:
    
        kiderchlanahai(current_player)
    
        check_gameover()

        flip_player()


    if winner == "X" or winner=="O":
        if winner =="X":
            print(player1 + " won")   
        else:
             print(player2 + " won")   
    elif winner==None:
        print("tie")
    if winner == None:
        print("YOU BOTH PLAYED WELL")
    else:
        if winner =="X":
            print("CONGRATULATIONS " + player1)
            print("BETTER LUCK NEXT TIME " + player2)
        else:
            print("CONGRATULATIONS " + player2)
            print("BETTER LUCK NEXT TIME " + player1)   


def kiderchlanahai(player):
    if player=="X":
        print(player1 + "'s turn")
    else :
        print(player2 + "'s turn")
    choose =input("enter a number(1-9):")
    valid = False
    while not valid:
        while choose not in ["1","2","3","4","5","6","7","8","9"]:
            choose =input("         INVALID INPUT.enter a number(1-9) ")

        choose =int(choose) -1
        if board[choose] == "_":
            valid = True
        else:
            print("IDHR CHALA HUA HAI. KHI AUR CHALAO" )


    board[choose]=player
    displayy()

def check_gameover():
    checkwin()
    checktie()

def checkwin():
    global winner
    
    rowwin =checkrow()
    columnwin =checkcolumn()
    diagonalwin =checkdiagonals()
    if rowwin:
        winner =rowwin
    elif columnwin:
        winner =columnwin
    elif diagonalwin:
        winner =diagonalwin
    else:
        winner =None
    return
def checkrow():
    global game_still_going

    row1= board[0] == board[1]== board[2] !="_"
    row2= board[3] == board[4]== board[5] !="_"
    row3= board[6] == board[7]== board[8] !="_"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def checkcolumn():
    global game_still_going
    column1= board[0] == board[3]== board[6] !="_"
    column2= board[1] == board[4]== board[7] !="_"
    column3= board[2] == board[5]== board[8] !="_"
    if column1 or column2 or column3:
        game_still_going =False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def checkdiagonals():
    global game_still_going
    diagonal1= board[0] == board[4]== board[8] !="_"
    diagonal2= board[6] == board[4]== board[2] !="_"
    
    if diagonal1 or diagonal2:
        game_still_going =False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return 



def checktie():
    global game_still_going

    if "_" not in board:
        game_still_going =False
    return

def flip_player():
    global current_player

    if current_player =="X":
        current_player ="O"
    elif current_player =="O":
        current_player ="X"
    return

play_game()

print("HAVE A NICE DAY")
print("THANKS FOR PLAYING")
print("                                                                                                                                 GAME BY 'AGAMJOT SINGH'")