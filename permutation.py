def permute(inputData, outputSoFar=[]):
    outputSizeToReach = len(inputData)
    for elem in inputData:
        if elem not in outputSoFar:
            outputSoFar.append(elem)
            if len(outputSoFar) == outputSizeToReach:
                yield outputSoFar
            else:
                for v in permute(inputData, outputSoFar):
                    yield v
            outputSoFar.pop()

for i in permute([1,2,3,4]):
    print (i)