

def surveyArea(terrainMap):
    forest_and_residential = [0,0]
    for xaxis in terrainMap:
        for yaxis in xaxis:
            if yaxis==1:
                forest_and_residential[0] += 1
            elif yaxis == 2:
                forest_and_residential[1] += 1
    return forest_and_residential

def isDistanceOkay(x1,y1,x2,y2,dist):
    return (abs(x1-x2)+abs(y1-y2))>=dist

def predictFire(terrainMap, fireInceptionRowIndex, fireInceptionColumnIndex, maxFF, maxRecur):
    atRisk = [0,0]
    numRow, numCol = len(terrainMap), len(terrainMap[0])
    # let onFire status be 3.
    onFire = 3
    ffpos = []
    def floodFill(r, c, num_recursed, maxFF, maxRecur):
        if r<0 or c<0 or r >= numRow or c >= numCol:
            return num_recursed
        num_recursed += 1
        if num_recursed > maxRecur:
            if len(ffpos) < maxFF:
                if isDistanceOkay(fireInceptionRowIndex, fireInceptionColumnIndex,r,c,maxRecur):
                    ffpos.append([r,c])
        curPos = terrainMap[r][c]
        if curPos != onFire and curPos != 0:
            if curPos == 1:
                atRisk[0] += 1
                #areaHit[1].append(tuple(r,c))
            elif curPos == 2:
                atRisk[1] += 1
                #areaHit[2].append(tuple(r,c))
            terrainMap[r][c] = onFire
            if r>=1 : num_recursed = floodFill(r-1, c, num_recursed, maxFF, maxRecur)
            if r+1 < numRow: num_recursed = floodFill(r+1, c,num_recursed, maxFF, maxRecur)
            if c>=1 : num_recursed = floodFill(r, c-1, num_recursed, maxFF, maxRecur)
            if c+1 < numCol : num_recursed = floodFill(r, c+1, num_recursed, maxFF, maxRecur)
        return num_recursed
    floodFill(fireInceptionRowIndex, fireInceptionColumnIndex, 0, maxFF, maxRecur)
    return ffpos
    #return atRisk, areaHit

def coordinateFirefighters(terrainMap, fireInceptionRowIndex, fireInceptionColumnIndex, firefightersAvailable, minimumDistance):
    # areaHit = {1:[],2:[]}
    #atRisk, areaHit,
    return predictFire(terrainMap, fireInceptionRowIndex, fireInceptionColumnIndex, firefightersAvailable, minimumDistance)
    
    # forestHit = areaHit[1]
    # residentialHit = areaHit[2]
