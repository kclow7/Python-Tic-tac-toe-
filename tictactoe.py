import random
import string

def DrawBoard(board):
    print "   |   |   "
    print " " + board[1] + " | " + board[2] + " | " + board[3] + " "
    print "   |   |   "
    print "-----------"
    print "   |   |   "
    print " " + board[4] + " | " + board[5] + " | " + board[6] + " "
    print "   |   |   "
    print "-----------"
    print "   |   |   "
    print " " + board[7] + " | " + board[8] + " | " + board[9] + " "
    print "   |   |   "

def InputPlayerLetter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        letter = raw_input("Do you want X or O? ")
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def WhoGoesFirst():
    if random.randint(0, 1) == 0:
        return "player"
    else:
        return "computer"

def PlayAgain():
    print "Do you want to play again? (yes or no) "
    return input().lower().startswith("y")

def MakeMove(board, letter, move):
    board[move] = letter

def IsWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le)
    or (bo[4] == le and bo[5] == le and bo[6] == le)
    or (bo[7] == le and bo[8] == le and bo[9] == le)
    or (bo[1] == le and bo[5] == le and bo[9] == le)
    or (bo[3] == le and bo[5] == le and bo[7] == le)
    or (bo[1] == le and bo[4] == le and bo[7] == le)
    or (bo[2] == le and bo[5] == le and bo[8] == le)
    or (bo[3] == le and bo[6] == le and bo[9] == le))

def GetBoardCopy(board):
    DupBoard = []
    for i in board:
        DupBoard.append(i)
    return DupBoard

def IsSpaceFree(board, move):
    return board[move] == " "

def GetPlayerMove(board):
    move = " "
    while move not in range(1,10) or not IsSpaceFree(board, int(move)):
        print "What is your next move? (1 to 9) "
        move = input()
    return int(move)

def ChooseRandomMoveFromList(board, movesList):
    possiblemoves = []
    for i in movesList:
        if IsSpaceFree(board, i):
            possiblemoves.append(i)
    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)
    else:
        return None

def GetComputerMove(board, computerletter):
    if computerletter == "X":
        playerletter = "O"
    else:
        playerletter = "X"

    for i in range(1, 10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy, i):
            MakeMove(copy, computerletter, i)
            if IsWinner(copy, computerletter):
                return i
    for i in range(1, 10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy, i):
            MakeMove(copy, playerletter, i)
            if IsWinner(copy, playerletter):
                return i
    move = ChooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if IsSpaceFree(board, 5):
        return 5

    return ChooseRandomMoveFromList(board, [2, 4, 6, 8])

def IsBoardFull(board):
    for i in range(1, 10):
        if IsSpaceFree(board, i):
            return False
    return True

print "Welcome to tic-tac-toe!"
while True:
    theBoard = [" "]*10
    playerletter, computerletter = InputPlayerLetter()
    turn = WhoGoesFirst()
    print "The " + turn + " will go first."
    GameIsPlaying = True
    while GameIsPlaying:
        if turn == "player":
            DrawBoard(theBoard)
            move = GetPlayerMove(theBoard)
            MakeMove(theBoard, playerletter, move)
            if IsWinner(theBoard, playerletter):
                DrawBoard(theBoard)
                print "Congratulations, you have defeated the PC!"
                GameIsPlaying = False
            else:
                if IsBoardFull(theBoard):
                    DrawBoard(theBoard)
                    print "It's a tie!"
                    break
                else:
                    turn = "computer"
        else:
            move = GetComputerMove(theBoard, computerletter)
            MakeMove(theBoard, computerletter, move)
            if IsWinner(theBoard, computerletter):
                DrawBoard(theBoard)
                print "HA! You lost to the computer."
                GameIsPlaying = False
            else:
                if IsBoardFull(theBoard):
                    DrawBoard(theBoard)
                    print "It's a tie!"
                    break
                else:
                    turn = "player"
    if not PlayAgain():
        break
