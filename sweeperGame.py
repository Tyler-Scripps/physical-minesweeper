import random

class sweeperGame:
    def __init__(self, width, height):
        self.outputs = []
        self.inputs = []
        self.gameWidth = width
        self.gameHeight = height
        self.gameState = [] # accessed as self.gameState[y][x]
        self.bombLocations = []
        self.numBombs = 0
        self.gamePhase = "play"

    def addOutput(self, outputObject):
        self.outputs.append(outputObject)
    
    def addInput(self, inputObject):
        self.inputs.append(inputObject)

    def updateOutputs(self):
        # if self.gamePhase == "play":
        for output in self.outputs:
            output.display(self.gameState, self.gamePhase)
        # else:
        #     for output in self.outputs:
        #         pass

    def updateInputs(self):
        for input in self.inputs:
            action, x, y = input.update()
            # print("action: ", action, ", x: ", x, ", y: ", y)
            if self.gamePhase == "play":
                tileValue = self.gameState[y][x] 
                # print("tileValue: ", tileValue)
                if action == "f":
                    if tileValue == 'c':
                        break
                    elif tileValue == 'u':
                        self.gameState[y][x] = 'f'
                    elif tileValue == 'f':
                        self.gameState[y][x] = 'u'
                    elif tileValue == 'ub':
                        self.gameState[y][x] = 'fb'
                    elif tileValue == 'fb':
                        self.gameState[y][x] = 'ub'
                elif action == "c":
                    if tileValue == 'f' or tileValue == 'c' or tileValue == 'fb':
                        break
                    elif tileValue == 'u':
                        self.gameState[y][x] = 'c'
                    elif tileValue == 'ub':     # hit a bomb
                        self.gamePhase = "loss"
                elif action == "r":
                    pass
            else:   # handle input when game is over
                if action == 'c':
                    self.startGame(x, y)
        
        ubCount = 0
        for row in self.gameState:
            for cell in row:
                if cell == 'ub':
                    ubCount += 1
        if ubCount == 0:
            self.gamePhase = "win"

    def setBombCount(self, numBombs):
        # make sure numBombs isn't too big
        if numBombs > (self.gameHeight * self.gameWidth - 1):
            numBombs = self.gameHeight * self.gameWidth
        self.numBombs = numBombs
    
    def startGame(self, safeX, safeY):
        print("width:", self.gameWidth, "height:", self.gameHeight)
        self.gamePhase = "play"

        # set gameState array up
        self.gameState = [['u' for _ in range(self.gameWidth)] for _ in range(self.gameHeight)]

        placedBombs = 0
        while placedBombs < self.numBombs:
            testX = random.randint(0, self.gameWidth-1)
            testY = random.randint(0, self.gameHeight-1)
            # print("testx:", testX, "testY:", testY)
            if (testX != safeX or testY != safeY) and self.gameState[testY][testX] == 'u':
                self.gameState[testY][testX] = 'ub'
                placedBombs += 1
        self.outputs[0].displayCheat(self.gameState)
        self.updateOutputs()
        
    def update(self):
        self.updateInputs()
        self.updateOutputs()