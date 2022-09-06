def solveCarProblem(distance, speedA, speedB, timeLimit):
    ''' calculate the actual time
        compare actual time against given time limit
        return True or False
    '''
    actualTime = distance / (speedA + speedB)
    print(actualTime)
    if actualTime <= timeLimit:
        return True
    else:
        return False

print(solveCarProblem(1000, 50, 60, 9))