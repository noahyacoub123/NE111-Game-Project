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

def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board,int(move)):
        print("What is your next move? (1-16)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board,movesList):
    possibleMoves =[]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves)!= 0:
        return random.choice(possibleMoves)
    else:
        return None


