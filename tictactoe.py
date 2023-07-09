import random

#defing the variables
board = ['-','-','-',
       '-','-','-',
       '-','-','-']

currentPlayer = 'X'
gameRunning = True
winner = None


#creating the game board
def printBoard(board):
    print(board[0]," | ",board[1]," | ",board[2])
    print("----------")
    print(board[3]," | ",board[4]," | ",board[5])
    print("----------")
    print(board[6]," | ",board[7]," | ",board[8])



#taking player input
def playerInput(board):
    playerin=int(input("Enter a spot in board 1-9:"))
    if board[playerin-1] == '-':
        board[playerin-1]=currentPlayer
    else:
        print("Oops! The spot is already occupied..")



#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] != '-':
        winner=board[0]
        return True
    elif board[3] == board[4] == board[5] != '-':
        winner=board[3]
        return True
    elif board[6] == board[7] == board[8] != '-':
        winner=board[6]
        return True
    
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] != '-':
        winner=board[0]
        return True
    elif board[1] == board[4] == board[7] != '-':
        winner=board[1]
        return True
    elif board[2] == board[5] == board[8] != '-':
        winner=board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[7] != '-':
        winner=board[0]
        return True
    elif board[6] == board[4] == board[3] != '-':
        winner=board[6]
        return True
    
def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning=False

    elif checkVertical(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning=False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning=False

def checkIfTie(board):
    global gameRunning5
    if '-' not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning=False



#switching player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer='O'
    else:
        currentPlayer='X'



#computer' turn
def compTurn(board):
    while currentPlayer == 'O':
        spot = random.randint(0,8)
        if board[spot] == '-':
            board[spot] = 'O'
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    compTurn(board)
    checkIfWin(board)
    checkIfTie(board)
else:
    print("The game has ended..")


