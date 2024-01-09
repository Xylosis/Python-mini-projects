class Board:
    def __init__(self):
        self.board = [
            ['.'],['.'],['.'],
            ['.'],['.'],['.'],
            ['.'],['.'],['.']
        ]
        self.turn = 'x'
        self.moveCount = 0
        self.gameOver = False
        self.winner = '-1'
        self.moveList = []

    def printBoard(self):
        counter = 0
        for tile in self.board:
           if (counter % 3 == 0 and counter != 0):
               print('\n')
           print(tile[0], end=" ")
           counter += 1
        print('\n')

    def checkForWin(self, move):
        if self.moveCount < 5:
            return False
        match move:
            case 0:
                if self.board[1][0] == self.board[2][0] == self.board[move][0]:
                    return True
                elif self.board[3][0] == self.board[6][0] == self.board[move][0]:
                    return True
                elif self.board[4][0] == self.board[8][0] == self.board[move][0]:
                    return True
            case 1:
                if self.board[0][0] == self.board[2][0] == self.board[move][0]:
                    return True
                elif self.board[4][0] == self.board[7][0] == self.board[move][0]:
                    return True
            case 2:
                if self.board[0][0] == self.board[1][0] == self.board[move][0]:
                    return True
                elif self.board[5][0] == self.board[8][0] == self.board[move][0]:
                    return True
                elif self.board[4][0] == self.board[6][0] == self.board[move][0]:
                    return True
            case 3:
                if self.board[0][0] == self.board[6][0] == self.board[move][0]:
                    return True
                elif self.board[4][0] == self.board[5][0] == self.board[move][0]:
                    return True
            case 4:
                if self.board[3][0] == self.board[5][0] == self.board[move][0]:
                    return True
                elif self.board[1][0] == self.board[7][0] == self.board[move][0]:
                    return True
                elif self.board[0][0] == self.board[8][0] == self.board[move][0]:
                    return True
                elif self.board[2][0] == self.board[6][0] == self.board[move][0]:
                    return True
            case 5:
                if self.board[2][0] == self.board[8][0] == self.board[move][0]:
                    return True
                elif self.board[3][0] == self.board[4][0] == self.board[move][0]:
                    return True
            case 6:
                if self.board[0][0] == self.board[3][0] == self.board[move][0]:
                    return True
                elif self.board[7][0] == self.board[8][0] == self.board[move][0]:
                    return True
                elif self.board[4][0] == self.board[2][0] == self.board[move][0]:
                    return True
            case 7:
                if self.board[1][0] == self.board[4][0] == self.board[move][0]:
                    return True
                elif self.board[6][0] == self.board[8][0] == self.board[move][0]:
                    return True
            case 8:
                if self.board[6][0] == self.board[7][0] == self.board[move][0]:
                    return True
                elif self.board[2][0] == self.board[5][0] == self.board[move][0]:
                    return True
                elif self.board[0][0] == self.board[4][0] == self.board[move][0]:
                    return True
            case _:
                return False

    def makeMove(self, piece, move):
        if self.gameOver:
            return
        elif self.moveCount == 9:
            self.winner = 'draw'
            self.gameOver = True
            return
        elif piece.lower() != self.turn:
            print('Not your turn, ' + str(piece))
            return
        if(move == None):
            while True:
                try:
                    index = int(input('Enter the number 1-9 that would like to place your square\n > '))
                    index = index - 1
                except ValueError:
                    print('Please enter a valid number.')
                    continue
                if (index < 0) or (index > 8):
                    print('Please enter a valid number.')
                    continue
                if (self.board[index][0] != '.'):
                    print('Board spot already occupied, please choose another.')
                    continue
                break
        else:
            index = move

        self.board[index][0] = piece.upper()
        self.moveList.append(index)
        self.moveCount += 1
        self.gameOver = self.checkForWin(index)
        if self.gameOver:
            self.winner = self.turn
            return

        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    
    def unmakeMove(self, move):
        self.board[move][0] = '.'
        try:
            self.moveList.remove(move)
        except ValueError:
            pass
        self.moveCount -= 1
        self.gameOver = False
        if self.winner != '-1':
            self.winner = '-1'
        if self.turn == 'x':
            self.turn = 'o'
        elif self.turn == 'o':
            self.turn = 'x'
        return

class Player:
    def __init__(self, piece):
        if (piece.lower() != 'x' and piece.lower() != 'o'):
            print(piece.lower())
            return
        self.piece = piece.lower()
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    def getPiece(self):
        return self.piece

    def claimWin(self):
        self.wins += 1
    
    def claimLoss(self):
        self.losses += 1

    def claimDraw(self):
        self.draws += 1
        

class AI:
    def __init__(self, boardObj, piece):
        self.possibleMoves = [0,1,2,3,4,5,6,7,8]
        self.realBoardObj = boardObj
        self.tempBoardObj = Board()
        self.piece = piece.lower()
        self.history = []
        self.winningDictionary = {}
        self.winDictIndex = 0

    def updatePossibleMoves(self):
        self.updateTempBoard()
        self.possibleMoves.remove(self.realBoardObj.moveList[-1])
        print(self.possibleMoves)
    
    def updateTempBoard(self):
        self.tempBoardObj.makeMove( 'x' if self.piece == 'o' else 'o', self.realBoardObj.moveList[-1])
        print('TEMP BOARD:')
        self.tempBoardObj.printBoard()

    def evaluate(self, possibleMoveList, depth):
        eval = 0
        self.displayTempBoard()
        print(self.winningDictionary)
        print(self.tempBoardObj.turn)
        if self.tempBoardObj.winner != '-1':
            if self.tempBoardObj.winner == self.piece:
                eval += 1
            elif self.tempBoardObj.winner == 'draw':
                eval += 0
            elif self.tempBoardObj.winner == 'x' if self.piece == 'o' else 'o': 
                eval -= 1
            #print(eval)
            return eval
        if depth == 0:
            return eval
        if self.tempBoardObj.turn == self.piece:
            for move in possibleMoveList:
                eval = 0
                self.tempBoardObj.makeMove(self.piece, move)
                tempMoveList = possibleMoveList[:]
                tempMoveList.remove(move)
                self.history.append(move)
                eval += self.evaluate(tempMoveList, depth= depth-1)
                self.tempBoardObj.unmakeMove(move)
                if(eval > 0): 
                    self.winningDictionary[self.winDictIndex] = self.history[:]
                    self.winDictIndex += 1
                elif (eval < 0):
                    pass
                self.history.pop()
                #print(eval)

        else:
            for move in possibleMoveList:
                eval = 0
                self.tempBoardObj.makeMove('x' if self.piece == 'o' else 'o', move)
                tempMoveList = possibleMoveList[:]
                tempMoveList.remove(move)
                self.history.append(move)
                eval += self.evaluate(tempMoveList, depth=depth-1)
                self.tempBoardObj.unmakeMove(move)
                if(eval > 0): 
                    self.winningDictionary[self.winDictIndex] = self.history
                    self.winDictIndex += 1
                elif (eval < 0):
                    pass
                self.history.pop()
                
            
        #print(eval)
        return eval
    
    def displayTempBoard(self):
        self.tempBoardObj.printBoard()
        print('\n')

if __name__ == "__main__":
    over = False
    obj = Board()
    playerX = Player('x')
    playerO = Player('o')
    playerAI = AI(obj, 'o')
    print(playerX.getPiece())
    #playerAI.evaluate(playerAI.possibleMoves, 1)
    
    while not obj.gameOver:
        obj.printBoard()
        obj.makeMove(playerX.piece, None)
        playerAI.updatePossibleMoves()
        playerAI.evaluate(playerAI.possibleMoves, 4)
        obj.printBoard()
        obj.makeMove(playerO.piece, playerAI.possibleMoves[0])
        playerAI.updatePossibleMoves()


    print('Final Board:')
    obj.printBoard()
    print('WINNER IS ' + obj.winner)

    if obj.winner == 'x':
        playerX.claimWin()
        playerO.claimLoss()
    elif obj.winner == 'o':
        playerO.claimWin()
        playerX.claimLoss()
    elif obj.winner == 'draw':
        playerX.claimDraw()
        playerO.claimDraw()

    print('Move List:', obj.moveList)
    
