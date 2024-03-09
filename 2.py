'''def spiralize(size):
    L = [ [0]* size for _ in range(size)]
    d,pos = [0,1], [0,-1]
    while any(L[pos[0]+t[0]][pos[1]+t[1]] != 1 for t in [d,[min(1,1-d[0]),min(1,1-d[1])]]):

        pos[0] += d[0]
        pos[1] += d[1]
        L[pos[0]][pos[1]] = 1
        try:
            if L[pos[0]+d[0]][pos[1]+d[1]] ==1:
                d = [min(1,1-d[0]),min(1,1-d[1])]
        except:
            d = [d[0]-1,  d[1]-1]
            if d[0] == -2: d[0] =1
            if d[1] == -2: d[1] = 1
    return L
print(spiralize(5))'''


def spiralize(size):
    L = [[0] * size for _ in range(size)]
    pos = [0, 0]
    flag = True
    while flag:
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            if flag == False:break
            for i in range(size+1):
                try:
                    if L[max(pos[0]+d[0],0)][max(pos[1]+d[1],0)] == 1 and pos[0]+d[0]>= 0 and pos[1]+d[1] >= 0:

                        if L[pos[0]][pos[1]] == 1:
                            l = [[0,1],[1,0],[0,-1],[-1,0]]
                            l.remove(d)
                            if any(L[max(pos[0]+j[0],0)][max(pos[1]+j[1],0)] == 1 for j in l):
                                L[pos[0]][pos[1]] = 0
                            flag = False
                        else:
                            pos = [pos[0] - d[0], pos[1] - d[1]]
                        break

                except:
                    break

                L[pos[0]][pos[1]] = 1
                pos = [max(pos[0]+d[0],0),max(pos[1]+d[1],0)]
    return '\n'.join(''.join(map(str, l)) for l in L)
print(spiralize(5))