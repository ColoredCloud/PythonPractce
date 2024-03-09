A = B = [1,1,0,0]
C = D = [0,1,1,0]
s = input().split('+')
space = [[0]*4 for i in range(4)]

trans = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
for i in s:

    for x in range(4):
        for y in range(4):
            flag = True
            for a,b in zip(['A','B','C','D'],[A,B,C,D]):

                if a in i:
                    if a == 'A' or a == 'C':
                        if (b[x] == 1 and '~'+a in i )or (b[x] == 0 and '~'+a not in i):
                            flag = False

                    else:
                        if (b[y] == 1 and '~'+a in i )or (b[y] == 0 and '~'+a not in i):
                            flag = False
            if flag == True:
                space[y][x] = 1
print(''.join(map(lambda x: trans[x],map(lambda x: int(x, 2),[''.join(map(str,s)) for s in space]))))