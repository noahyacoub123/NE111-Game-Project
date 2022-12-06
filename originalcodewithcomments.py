
import random  #Importing the random module for later use in the code -NY


#A.P are the initials of Alden Panicker, NY for Noah Yacoub, and EH for Edward Hong
def drawBoard(board):
    #this code draws a tic tac toe 3x3 board by printing the indexes of a list and printing lines between them. A.P
    print(board[7] + '|' + board[8] + '|' + board[9]) #The "|" printed is just a boundary to make the board look cleaner -NY
    print('-+-+-') #This line does something similar to the last, prints a board bondary to make the look a little cleaner -NY
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    #creates a variable to represent the letter 'X' or 'O' that the player can play as A.P
    while not (letter == 'X' or letter == 'O'): # this loop checks to make sure that the player can only choose between X or O to play as A.P
        print('Do you want to be X or O?')
        letter = input().upper() #Makes sure the letter chosen by the player is uppercase no matter what (to prevent issues later on when the chosen character needs to be called) -NY
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
    #Number must be an integer since .randint is used, so there is a 50/50 chance for whoever will go first -NY
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
#This is because a new board will need to be printed each time a move is executed, it simply appends, or adds, the player or computers character into the board and then prints it again with the updated status _NY
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
    possibleMoves = [] #Initializing the list so that the possible moves can be added to it for the computer later -NY
    for i in movesList: #This loop calls the function isSpaceFree to check all the possible spaces that are available for the computer to go to, then adds them to a list that will later be referenced -NY
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0: #Checks if there are actually available moves, if there are, randomly chooses one from the list of possible moves -NY
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter): #function for choosing a move for the computer. A.P
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
#sets playerLetter equal to whatever letter the computer is not
    for i in range(1,10): #Since there are only 9 options of where to go on the board, and the range functions is exclusive in its second argument, it must be from 1-10 -NY
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
            #the above lines check if a space is free to make a move, and if the computer is a winner A.P
    for i in range(1,10): #Same as above, only 9 options and range is exclusive on its second argument -NY
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
        # the above lines check if a space is free to make a move, and if the player is a winner A.P
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) #Since these are the corner values of the board, checks if those are free first (Since it gives the biggest strategic advantage) -NY
    if move!= None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
# above lines first check if the corners of the board are empty, if they are, it checks the center, finally it will pick whatever is remaining if it cannot get the corner or center. A.P
def isBoardFull(board):
    #this function checks to ensure that all of the board is not taken by letters. A.P
    for i in range(1, 10): #This loop calls the isSpaceFree function and checks each position to see if there are empty slots, if there are, returns False, but if there are no slots available, returns True
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic-Tac-Toe!') #functions have all been created so this line prints the starting sentence. A.P

while True: #This is the start of the game, from here-on, all of the code is just instructions for the game and player -NY
    theBoard = [' '] * 10 #Prints 10 empty lists to later append the moves into -NY
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst() #Calling the function whoGoesFirst to let the player know whos turn it is -NY
    #some variables for the board, computer and players letters as well as who's turn it is are initialized. A.P
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True #Lets our later code know that the game is actually running -NY
    #this variable starts the game as the following loop will run only when it is true and when it is false the code wont run. A.P

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            #if its the players turn, the board will be printed, the player will be asked for their move, and then the function to make the players move will be called. A.P
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
                #this checks if the player is a winner, if it is the board will be printed and a message will be sent to inform the player of thier win. The game will also stop running. A.P
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                    #this checks if the board is full. if it is, then it will print that the game is a tie and stop the code. A.P
                else:
                    turn = 'computer'
                    #if not, it will become the computers turn to move. A.P
        else:
#this all runs when its the computers turn A.P
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
#makes a move for the computer A.P
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
                #checks if computer won. then prints message and ends game. A.P
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                    #checks for a tie. then prints message and ends code. A.P
                else:
                    turn = 'player'
                    #if the board isnt full, it returns to being the players turn. A.P
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
        #asks the player if they want to play again. as long as the answer starts with a y, the game will restart. if not the code will stop running. A.P