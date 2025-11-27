import sweeperGame
import terminalOutput
import terminalInput

myGame = sweeperGame.sweeperGame(4, 4)
myGame.setBombCount(1)
myTerminalOutput = terminalOutput.terminalOutput()
myTerminalInput = terminalInput.terminalInput()

myGame.addOutput(myTerminalOutput)
myGame.addInput(myTerminalInput)

myGame.startGame(0, 0)


while True:
    myGame.update()