import sweeperGame
import terminalOutput
import terminalInput

myGame = sweeperGame.sweeperGame(4, 4)
myGame.set_bomb_count(2)
myTerminalOutput = terminalOutput.terminalOutput()
myTerminalInput = terminalInput.terminalInput()

myGame.add_output(myTerminalOutput)
myGame.add_input(myTerminalInput)

myGame.start_game(0, 0)


while True:
    myGame.update()