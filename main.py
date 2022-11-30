# Initials for who did what, Edward Hong as EH, Alden Panicker as AP, and Noah Yacoub as NY -NY
import pygame  #importing the pygame module -NY
import random  #Importing the random module -NY
def gameboard_drawing(board):
    #This function will 'draw' the game board as a list of 16 (4x4) instead of the usual 9 (3x3) -NY
    print(board[13]) + '|' + print(board[14]) +'|' + print(board[15]) + '|' + print(board[16])
    print('_______')  #Just a horizontal line to separate the rows and make it look a little cleaner -NY
    print(board[9]) + '|' + print(board[10]) + '|' + print(board[11]) + '|' + print(board[12])
    print('_______')
    print(board[5]) + '|' + print(board[6]) + '|' + print(board[7]) + '|' + print(board[8])
    print('_______')
    print(board[1]) + '|' + print(board[2]) + '|' + print(board[3]) + '|' + print(board[4])

















# This function defines whether the player or the computer gets the first turn. - EH
def whoGoesFirst():
# Goes through random #s, prints out random dialogue
    if (random.randint(0,7) == 0):
        return "Computer goes first!"
    elif (random.randint(0,7) == 1):
        return "Computer, you're up!"
    elif (random.randint(0,7) == 2):
        return "Beep boop, "
    elif (random.randint(0, 7) == 3):
        return "00100011 00110001"
    elif (random.randint(0, 7) == 4):
        return "Player goes first!"
    elif (random.randint(0, 7) == 5):
        return "Make us proud, player!"
    elif (random.randint(0, 7) == 6):
        return "Let's see what humanity is capable of!"
    else:
        return "Player, you're up!"

# adds appropriate piece to the designated spot - EH
def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):






            )