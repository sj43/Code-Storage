# 10+10+0.52+0.3+0.59+10+10+10+0.65+10

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
        if num_recursed > minimumDistance:
            if len(ffpos) < firefightersAvailable:
                if isDistanceOkay(fireInceptionRowIndex, fireInceptionColumnIndex,r,c,minimumDistance):
                    ffpos.append([r,c])
        curPos = terrainMap[r][c]
        if curPos != onFire and curPos != 0:
            if curPos == 1:
                atRisk[0] += 1
            elif curPos == 2:
                atRisk[1] += 1
            terrainMap[r][c] = onFire
            if r>=1 : num_recursed = floodFill(r-1, c, num_recursed)
            if r+1 < numRow: num_recursed = floodFill(r+1, c,num_recursed)
            if c>=1 : num_recursed = floodFill(r, c-1, num_recursed)
            if c+1 < numCol : num_recursed = floodFill(r, c+1, num_recursed)
        return num_recursed
    floodFill(fireInceptionRowIndex, fireInceptionColumnIndex, 0)
    return ffpos
