class terminalOutput:
    def __init__(self):
        pass

    def display(self, gameState, gamePhase):
        if gamePhase == "play":
            for rowNum, row in enumerate(gameState):
                for colNum, cell in enumerate(row):
                    if 'f' in cell:  # flagged cells
                        print('🚩 ', end='')
                    elif 'u' in cell:    # unchecked cells
                        print('▢ ', end='')
                    elif cell == 'c':   # checked cells
                        bombCount = self.count_bombs(gameState, colNum, rowNum)
                        print(bombCount, end=' ')
                print()
        elif gamePhase == "loss":
            self.detonate(gameState)
        elif gamePhase == "win":
            print("You won!")
    
    def displayCheat(self, gameState):
        for row in gameState:
            for item in row:
                print("{:<2}".format(item), end=' ')
            print()
    
    def blank(self, gameState):
        pass

    def count_bombs(self, gameState, x, y):
        """
        Count how many cells bordering (row, col) contain target_value.
        Checks all 8 surrounding cells (edges and corners).
        """
        rows = len(gameState)
        cols = len(gameState[0]) if rows > 0 else 0
        
        count = 0
        
        # Check all 8 directions: top-left to bottom-right
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the center cell itself
                if dr == 0 and dc == 0:
                    continue
                
                # Calculate neighbor position
                r, c = y + dr, x + dc
                
                # Check if neighbor is within bounds
                if 0 <= r < rows and 0 <= c < cols:
                    if 'b' in gameState[r][c]:
                        count += 1

        return count
    
    def detonate(self, gameState):
        print("Oh no you hit a bomb!")
        for row in gameState:
            for cell in row:
                if cell == 'f':  # flagged cells without bombs
                    print('f ', end='')
                elif cell == 'fb':    # flagged cells with bombs
                    print('🚩 ', end='')
                elif cell == 'ub':   # unchecked bombs
                    print('💣', end=' ')
                else:
                    print('O', end=' ')
            print()