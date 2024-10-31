import os
import sys
from src import infoUtils as infoUt
from src import globals as glb
from csv import reader

def errorHandler():
    if (len(sys.argv) != 2):
        infoUt.errorSyntax()
    if sys.argv[1] == "-h":
        infoUt.displayUsage()
    if not os.path.isfile(sys.argv[1]):
        infoUt.errorFile()

def csvHandler():
    with open(sys.argv[1], newline='') as csvfile:
        csvText = reader(csvfile, delimiter=';')
        for row in csvText:
            if len(row) != 0:
                temp = []
                if len(row) < 4:
                    glb.array.append(row[0])
                temp.append(row[1])
                temp.append(int(row[2]))
                temp.append(row[3:])
                temp.extend((0,0,0))
                if row[0] in glb.store:
                    infoUt.errorGraph()
                glb.store[row[0]] = temp