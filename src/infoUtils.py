def errorGraph():
    raise RuntimeError("Graph Error")

def errorFile():
    raise RuntimeError("File Error")

def errorSyntax():
    raise ValueError("Syntax Error")

def displayUsage():
    raise BaseException("\nUSAGE:\n\t./305construction file\nDESCRIPTION:\n\tfile\tThe file you want to use.\n\n")