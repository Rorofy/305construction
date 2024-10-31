from src import globals as glb

def convertFloat(duration):
    for tsk in glb.store:
        nextDuration = duration
        for curr in glb.store:
            if tsk in glb.store[curr][2] and nextDuration > glb.store[curr][3]:
                nextDuration = glb.store[curr][3]
        glb.store[tsk][5] = nextDuration - glb.store[tsk][4]