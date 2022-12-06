# Initials for who did what, Edward Hong as EH, Alden Panicker as AP, and Noah Yacoub as NY -NY
import random  #Importing the random module -NY

def drawBoard(board):
    #This function will 'draw' the game board as a list of 16 (4x4) instead of the usual 9 (3x3) -NY
    #this function takes a list 'board' with 16 strings that correspond to a four by four grid and prints it, including dividers, to create a visual board drawing for the tictactoe board -AP
    print(board[13] + ' |' + board[14] + ' |' + board[15] + ' |' + board[16])
    print('_______')  #Just a horizontal line to separate the rows and make it look a little cleaner -NY
    print(board[9] + ' |' + board[10] + ' |' + board[11] + ' |' + board[12])
    print('_______')
    print(board[5] + ' |' + board[6] + ' |' + board[7] + ' |' + board[8])
    print('_______')
    print(board[1] + ' |' + board[2] + ' |' + board[3] + ' |' + board[4])

def InputPlayerLetter():
    #This function will let the player choose which letter they want to be in the game, then choosing the computers letter based on that

    letter = "" #Initializing the letter variable
    while not (letter == 'X' or letter == 'O'):
        print("Hello player, do you want to be X or O? ")
        letter = input().upper() #making sure that the letter chosen will be an upper case letter for simplicity
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"] #Players letter will be shown as the first index and the computer will be the second

#determines whether the player or computer goes on the first turn
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

#updates the board
def makeMove(board, letter, move):
    board[move] = letter


#receives input from player, and places their X or O onto the board
def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)): #Since there is a bigger board, needs to be more available moves so now goes from 1-16 instead of 1-9 -NY
        print("What is your next move? (1-16)")
        move = input()
    return int(move)

#randomly places X or O on behalf of computer (computer's moves)
def chooseRandomMoveFromList(board,movesList):
    possibleMoves =[]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves)!= 0:
        return random.choice(possibleMoves)
    else:
        return None

def isWinner(bo, le): #Checks if the player or computer has placed three X's or O's in a row, winning the game. Checks every single case for this -NY and EH
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or (bo[2] == le and bo[3] == le and bo[4] == le) or (bo[5] == le and bo[6] == le and bo[7] == le) or (bo[6] == le and bo[7] == le and bo[8] == le) or (bo[9] == le and bo[10] == le and bo[11] == le) or (bo[10] == le and bo[11] == le and bo[12] == le) or (bo[13] == le and bo[14] == le and bo[15] == le) or (bo[14] == le and bo[15] == le and bo[16] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[5] == le and bo[9] == le and bo[13] == le) or (bo[2] == le and bo[6] == le and bo[10] == le) or (bo[6] == le and bo[10] == le and bo[14] == le) or (bo[3] == le and bo[7] == le and bo[11] == le) or (bo[7] == le and bo[11] == le and bo[15] == le) or (bo[4] == le and bo[8] == le and bo[12] == le) or (bo[8] == le and bo[12] == le and bo[16] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[4] == le and bo[7] == le and bo[10] == le) or (bo[7] == le and bo[10] == le and bo[13] == le) or (bo[8] == le and bo[11] == le and bo[14] == le) or (bo[2] == le and bo[7] == le and bo[12] == le) or (bo[1] == le and bo[6] == le and bo[11] == le) or (bo[6] == le and bo[11] == le and bo[16] == le) or (bo[5] == le and bo[10] == le and bo[15] == le))

#brings a blank slate of the game board
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

#determines if the board space is free (checks if there's an X or O on a section or not)
def isSpaceFree(board, move):
    return board[move] == ''

#Now it's time to code the artificial intelligence for our game, which will be split up in sections among the three of us -NY
def getComputerMove(board, computerLetter): #Verifies that the players chosen letter will be the opposite of the computer -NY
    if computerLetter == "X":
        playerLetter == "O"
    else:
        playerLetter == "X"

    for i in range(1, 17): #Like with the original code, the second argument of the range function is exclusive so tho there are only 16 spaces, need to write 17 since its not counted -NY
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    for i in range(1, 17):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 4, 13, 16])
    if move != None:
        return move

    #No center so cannot have computer put X or O there

    return chooseRandomMoveFromList(board, [2, 3, 5, 9, 14, 15, 8, 12, 6, 7, 10, 11])

#checks if the board is full (no free space(s))
def isBoardFull(board):
    for i in range(1, 17):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic-Tac-Toe, Player!\nHere are some rules we would like you to follow!\n")

#prints out a random dialogue from a pool of options - EH
def dialogueFirst(turn):
    if turn == 'computer':
        if random.randint(0, 3) == 0:
            return "Computer goes first!"
        elif random.randint(0, 3) == 1:
            return "Computer goes 00100011 00110001! (#1)"
        elif random.randint(0, 3) == 2:
            return "Computer, make us proud!"
        elif random.randint(0, 3) == 3:
            return "Beep-boop, you're up, computer!"
    else:
        if random.randint(4, 6) == 4:
            return "Player goes first!"
        elif random.randint(4, 6) == 5:
            return "Player, show us what you got!"
        elif random.randint(4, 6) == 6:
            return "Player is up!"
        else:
            return "Player, it's your time to shine!"

print("Rule #1: Each player (computer & user) will be alternatively taking turns.\nRule #1b: Whoever goes first will be randomly determined.\nRule #2: The player will choose either X or O as their ‘character’ for the game.\nRule #2b: The player will choose a slot to place their piece (X or O) on a 4 x 4 grid board.\nRule #2c: There will be an option for the player to choose a number between 1 to 16.\nRule #2d: The player is NOT allowed to overwrite a pre-existing piece, no matter if it’s their own piece or not.\nRule #2e: Only 1 piece will be allowed to be placed per each player’s own turn.\nRule #3: First player to place 3 of their pieces in a row (horizontal, vertical or diagonal) wins the game!\nRule #3b: It does not matter which part of the grid the row is present on, as long as there are 3 pieces connected to each other through the aforementioned method.\nRule #4: Enjoy and make sure to have fun! It’s a game after all!\n")

#while the player is willing to play, executes the game
while True:
    theBoard = ['']*17 #Needs to be larger again, since the board is larger -NY
    playerLetter, computerLetter = InputPlayerLetter()
    turn = whoGoesFirst()

    print(dialogueFirst(turn))

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
                    print("The game is a tie!")
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                 drawBoard(theBoard)
                 print("The computer has beaten you! You lose!")
                 gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    #asks if the player would like to play again, and repeats the same game or ends the game depending on the player's input/answer
    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break





