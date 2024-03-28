ANSI_RESET = "\u001B[0m"
ANSI_BLACK = "\u001B[30m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
ANSI_CYAN = "\u001B[36m"
ANSI_WHITE = "\u001B[37m"

def genLine(color, text):
    return color + text + ANSI_RESET

def genRedLine(text):
    return genLine(ANSI_RED, text)
def genBlackLine(text):
    return genLine(ANSI_BLACK, text)

def genGreenLine(text):
    return genLine(ANSI_GREEN, text)

def genYellowLine(text):
    return genLine(ANSI_YELLOW, text)

def genBlueLine(text):
    return genLine(ANSI_BLUE, text)

def genPurpleLine(text):
    return genLine(ANSI_PURPLE, text)

def genCyanLine(text):
    return genLine(ANSI_CYAN, text)

def genWhiteLine(text):
    return genLine(ANSI_WHITE, text)
