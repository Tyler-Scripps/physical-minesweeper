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

    def add_output(self, outputObject):
        self.outputs.append(outputObject)
    
    def add_input(self, inputObject):
        self.inputs.append(inputObject)

    def update_outputs(self):
        # if self.gamePhase == "play":
        for output in self.outputs:
            output.display(self.gameState, self.gamePhase)
        # else:
        #     for output in self.outputs:
        #         pass

    def update_inputs(self):
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
                    self._check_tile(y, x)
                elif action == "r":
                    pass
            else:   # handle input when game is over
                if action == 'c':
                    self.start_game(x, y)
        
        ubCount = 0
        for row in self.gameState:
            for cell in row:
                if cell == 'ub':
                    ubCount += 1
        if ubCount == 0:
            self.gamePhase = "win"

    def set_bomb_count(self, numBombs):
        # make sure numBombs isn't too big
        if numBombs > (self.gameHeight * self.gameWidth - 1):
            numBombs = self.gameHeight * self.gameWidth
        self.numBombs = numBombs
    
    def start_game(self, safeX, safeY):
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
        self.update_outputs()
        
    def update(self):
        self.update_inputs()
        self.update_outputs()

    def _count_bombs(self, row, col):
        """
        Count how many cells bordering (row, col) contain bombs.
        Checks all 8 surrounding cells (edges and corners).
        """
        
        count = 0
        
        # Check all 8 directions: top-left to bottom-right
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the center cell itself
                if dr == 0 and dc == 0:
                    continue
                
                # Calculate neighbor position
                r, c = row + dr, col + dc
                
                # Check if neighbor is within bounds
                if 0 <= r < self.gameHeight and 0 <= c < self.gameWidth:
                    if 'b' in self.gameState[r][c]:
                        count += 1

        return count
    
    def _count_flags(self, row, col):
        """
        Count how many cells bordering (row, col) contain flagged cells.
        Checks all 8 surrounding cells (edges and corners).
        """
        
        count = 0
        
        # Check all 8 directions: top-left to bottom-right
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the center cell itself
                if dr == 0 and dc == 0:
                    continue
                
                # Calculate neighbor position
                r, c = row + dr, col + dc
                
                # Check if neighbor is within bounds
                if 0 <= r < self.gameHeight and 0 <= c < self.gameWidth:
                    if 'f' in self.gameState[r][c]:
                        count += 1

        return count
    
    def _check_tile(self, row, col):
        print("checking:", col, row)
        tileValue = self.gameState[row][col] 
        if tileValue == 'c':
            if self._count_bombs(row, col) == self._count_flags(row, col):
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        # Skip the center cell itself
                        if dr == 0 and dc == 0:
                            continue
                        
                        # Calculate neighbor position
                        r, c = row + dr, col + dc
                        
                        # Check if neighbor is within bounds
                        if 0 <= r < self.gameHeight and 0 <= c < self.gameWidth and self.gameState[r][c] != 'c':
                            self._check_tile(r, c)
        elif tileValue == 'f' or tileValue == 'fb':
            pass
        elif tileValue == 'u':
            self.gameState[row][col] = 'c'
            if self._count_bombs(row, col) == 0:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        # Skip the center cell itself
                        if dr == 0 and dc == 0:
                            continue
                        
                        # Calculate neighbor position
                        r, c = row + dr, col + dc
                        
                        # Check if neighbor is within bounds
                        if 0 <= r < self.gameHeight and 0 <= c < self.gameWidth and self.gameState[r][c] != 'c':
                            self._check_tile(r, c)

        elif tileValue == 'ub':     # hit a bomb
            self.gamePhase = "loss"
            return False