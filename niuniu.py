from cmath import pi, sin


def getTwoDimensionListIndex(L,value):   
    for i in range(len(L)):  
        for j in range(len(L[i])):  
            if L[i][j] == value :
                return i,j 


mn_map = [[0]*10]*10
for i in range(10):
    mn_map[i] = input()   
fx, fy = getTwoDimensionListIndex(mn_map,'F')
cx, cy = getTwoDimensionListIndex(mn_map,'C')
m = 0
n = 0
cout = 0
while(1):
    if (fx+sin((pi/2)*n))>9 or (fx+sin((pi/2)*n))<0 or (fy+sin(pi/2 + (pi/2)*n))>9 or (fy+sin(pi/2 + (pi/2)*n))<0 or mn_map[fx+sin((pi/2)*n)][fy+sin(pi/2 + (pi/2)*n)]=='*':
        n += 1
    if (cx+sin((pi/2)*m))>9 or (cx+sin((pi/2)*m))<0 or (cy+sin(pi/2 + (pi/2)*m))>9 or (cy+sin(pi/2 + (pi/2)*m))<0 or mn_map[cx+sin((pi/2)*m)][cy+sin(pi/2 + (pi/2)*m)]=='*':
        m += 1
    fx += sin((pi/2)*n)
    fy += sin(pi/2 + (pi/2)*n)
    cx += sin((pi/2)*m)
    cy += sin(pi/2 + (pi/2)*m)
    cout += 1
    if fx == cx and fy ==cy:
        break
print(cout)

