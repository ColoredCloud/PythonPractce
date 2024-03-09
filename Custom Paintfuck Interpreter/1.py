#https://www.codewars.com/kata/5868a68ba44cfc763e00008d/train/python

def find(code,nowI,direction):
    obtacle = 0
    i = nowI
    while obtacle != -1:
        i += direction
        if code[i] == ']':
            if direction == 1:
                obtacle -= 1
            else:
                obtacle += 1
        if code[i] == '[' :
            if direction == -1:
                obtacle -= 1
            else:
                obtacle += 1
        if i < 0 or i >= len(code): return None
    return i
def interpreter(code, iterations, width, height):
    #return str([code, iterations, width, height])
    space = [[0]*width for i in range(height)]
    #print(space)
    nowProcesing = 0
    Point = [0,0]
    while iterations != 0 and nowProcesing < len(code):
        if code[nowProcesing] in 'nesw[]*':
            iterations-=1

        if Point[0] not in range(0,height):
            if Point[0] >= height:
                Point[0] -= height
            else:
                Point[0] += height
        if Point[1] not in range(0,width):
            if Point[1] >= width:
                Point[1] -= width
            else:
                Point[1] += width
        if code[nowProcesing] == 'n':
            Point[0]-=1
            nowProcesing+=1
        elif code[nowProcesing] == 's':
            Point[0]+=1
            nowProcesing+=1
        elif code[nowProcesing] == 'w':
            Point[1]-=1
            nowProcesing+=1
        elif code[nowProcesing] == 'e':
            Point[1]+=1
            nowProcesing+=1

        elif code[nowProcesing] == '*':
            space[Point[0]][Point[1]] = 1-space[Point[0]][Point[1]]
            nowProcesing+=1
        elif code[nowProcesing] == '[' and space[Point[0]][Point[1]] == 0:
            nowProcesing = find(code,nowProcesing,1)+1
        elif code[nowProcesing] == ']' and space[Point[0]][Point[1]] == 1:
            nowProcesing = find(code,nowProcesing,-1)+1
        else:
            nowProcesing += 1


    ans = [''.join(map(str,lst))for lst in space]
    #print(list(ans))
    return '\r\n'.join(ans)
print(interpreter("*[s[e]*]", 5, 5, 5))