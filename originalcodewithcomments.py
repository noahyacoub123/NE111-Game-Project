import pygame  #importing the pygame module -NY
import random  #Importing the random module -NY


#A.P are the initials of Alden Panicker
def drawBoard(board):
    #this code draws a tic tac toe 3x3 board by printing the indexes of a list and printing lines between them. A.P
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    #creates a variable to represent the letter 'X' or 'O' that the player can play as A.P
    while not (letter == 'X' or letter == 'O'): # this loop checks to make sure that the player can only choose between X or O to play as A.P
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    #returns a list with the players choice as the first index and the opposite as the second index A.P
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    #this function takes a random number between 0 and 1 to decide whether the computer or player will go first. A.P

def makeMove(board,letter,move):
    board[move] = letter
#this function makes a move for the player by taking the list of 'board' (which corresponds to the nine empty spaces on the board) and the number from 1-9 which is the input by the player and setting it equal to the letter of the player. A.P
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))
#this function returns true if either the player or computer have three spaces of the same letter in a line. checks if there is a winner to the game. A.P
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
#this function creates a copy of the board. A.P
def isSpaceFree(board,move):
    return board[move] == ''
#this function checks if the space on the board that the player wants to choose is empty or not as a boolean value. A.P
def getPlayerMove(board):
    #this function gets the players move by setting it the players input equal to the variable 'move'. A.P
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        #loop checks if the player chose a number that is allowed (correct number and must be an empty space) A.P
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # this function makes a list of the possible moves the computer can make by checking if each space on the board is empty. it then randomly chooses one choice. A.P
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter): #function for choosing a move for the computer. A.P
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
#sets playerLetter equal to whatever letter the computer is not
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
            #the above lines check if a space is free to make a move, and if the computer is a winner A.P
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
        # the above lines check if a space is free to make a move, and if the player is a winner A.P
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move!= None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
# above lines first check if the corners of the board are empty, if they are, it checks the center, finally it will pick whatever is remaining if it cannot get the corner or center. A.P
def isBoardFull(board):
    #this function checks to ensure that all of the board is not taken by letters. A.P
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic-Tac-Toe!') #functions have all been created so this line prints the starting sentence. A.P

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break