from src import globals as glb
from src import calcUtils as cUtils

def addTask(tsk):
    taskLen = 0
    paths = []
    for i in glb.array:
        temp = pathingAlgorithm(tsk, i)
        if temp: paths += temp
    for p in paths:
        duration = 0
        for j in p[1:]:
            duration+= glb.store[j][1]
        temp = duration
        if temp > taskLen: taskLen = temp
    return taskLen

def getDuration():
    duration = 0
    for tsk in glb.store:
        glb.store[tsk][3] = addTask(tsk)
        glb.store[tsk][4] = glb.store[tsk][3] + glb.store[tsk][1]
        if (glb.store[tsk][4] > duration):
            duration = glb.store[tsk][4]
    cUtils.convertFloat(duration)
    if (duration > 1):
        print("total duration of construction:", duration,"weeks")
    else:
        print("total duration of construction:", duration,"week")
    print()

def pathingAlgorithm(begin, end, path=[]):
    path = path + [begin]
    if begin == end:
        return [path]
    if begin not in glb.store:
        return []
    paths = []
    for i in glb.store[begin][2]:
        if i not in path:
            newpaths = pathingAlgorithm(i, end, path)
            for j in newpaths:
                paths.append(j)
    return paths

def ganttAlgorithm():
    getDuration()
    temp = []
    for curr in glb.store:
        temp.append([curr, glb.store[curr][3], glb.store[curr][1], glb.store[curr][5]])
    temp = sorted(temp, key=lambda elem: (elem[1], elem[2], elem[3]))
    for e in temp:
        curr = e[0]
        if glb.store[curr][5] > 0:
            print(curr, "must begin between",
                  "t=" + str(glb.store[curr][3]), "and",
                  "t=" + str(glb.store[curr][3] + glb.store[curr][5]))
        else:
            print(curr, "must begin at" , "t=" + str(glb.store[curr][3]))
    print()
    for e in temp:
        curr = e[0]
        print(curr + "\t" + "(" + str(glb.store[curr][5])
              + ")" + "\t" + str(" "*glb.store[curr][3])
              + str("="*glb.store[curr][1]))