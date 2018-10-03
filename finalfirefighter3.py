# 60+0.43+0.9+0.59+0.4

def isDistanceOkay(x1,y1,x2,y2,dist):
    return (abs(x1-x2)+abs(y1-y2))>=dist

def coordinateFirefighters(terrainMap, fireInceptionRowIndex, fireInceptionColumnIndex, firefightersAvailable, minimumDistance):
    atRisk = [0,0]
    numRow, numCol = len(terrainMap), len(terrainMap[0])
    # let onFire status be 3.
    onFire = 3
    ffpos = []
    def floodFill(r, c, num_recursed):
        if r<0 or c<0 or r >= numRow or c >= numCol:
            return num_recursed
        num_recursed += 1
        if (num_recursed > minimumDistance) and (len(ffpos) < firefightersAvailable) and ([r,c] not in ffpos) and isDistanceOkay(fireInceptionRowIndex, fireInceptionColumnIndex,r,c,minimumDistance):
            ffpos.append([r,c])
        curPos = terrainMap[r][c]
        if curPos != onFire and curPos != 0:
            terrainMap[r][c] = onFire
            if r>=1 : num_recursed = floodFill(r-1, c, num_recursed)
            if c+1 < numCol : num_recursed = floodFill(r, c+1, num_recursed)
            if r+1 < numRow: num_recursed = floodFill(r+1, c,num_recursed)
            if c>=1 : num_recursed = floodFill(r, c-1, num_recursed)
        return num_recursed
    floodFill(fireInceptionRowIndex, fireInceptionColumnIndex, 0)
    return ffpos
