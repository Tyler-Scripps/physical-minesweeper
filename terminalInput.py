class terminalInput:
    def __init__(self):
        pass

    def update(self):
        usrInput = input("enter action: ")
        vals = usrInput.split()

        if vals[0] == "flag" or vals[0] == "f":
            return 'f', int(vals[1]), int(vals[2])
        elif vals[0] == "check" or vals[0] == "c":
            return 'c', int(vals[1]), int(vals[2])
        elif vals[0] == "restart" or vals[0] == "r":
            return 'r', 0, 0
        else:
            print("invalid input")
            return 0, 0, 0