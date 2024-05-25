def findcirclenum(isConnected):
    connectedlist = []
    provincenum = len(isConnected)
    for i in range(len(isConnected)):
        for j in range(len(isConnected[i])):
            if (j>i) and (isConnected[i][j]==1):
                provincenum -= 1
                inlist = False
                for k in range(len(connectedlist)):
                    if (str(i) in connectedlist[k]) and (str(j) in connectedlist[k]): 
                        provincenum += 1
                        inlist = True
                    elif (str(i) in connectedlist[k]): #j not in connectedlist[k]
                        connectedlist[k] += str(j)
                        inlist = True
                    elif (str(j) in connectedlist[k]): #i not in connectedlist[k]
                        connectedlist[k] += str(i)
                        inlist = True
                if inlist == False:
                    connectedlist.append(str(i)+str(j))
                
    return provincenum

print(findcirclenum([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]]))
