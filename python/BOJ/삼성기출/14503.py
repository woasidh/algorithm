# 30분 이내로 품

import sys
n, m = map(int, sys.stdin.readline().split());
x, y, d = map(int, sys.stdin.readline().split());
globalMap = [];
for _ in range(n):
    globalMap.append(list(map(int, sys.stdin.readline().split())));

def isAvailableClean(x, y):
    global n, m, globalMap;
    if not (0 <= x < n and 0 <= y < m): return False;
    return True if globalMap[x][y] == 0 else False;

def isBlocked(x, y):
    global n, m, globalMap;
    if not (0 <= x < n and 0 <= y < m): return True;
    return True if globalMap[x][y] == 1 else False;

dx = [-1, 0, 1, 0];
dy = [0, 1, 0, -1];
globalMap[x][y] = 2;
answer = 1;
while True:
    cleanAvailable = False;
    for i in range(1, 5):
        nd = (d - i) % 4;
        nx = x + dx[nd];
        ny = y + dy[nd];
        if isAvailableClean(nx, ny):
            cleanAvailable = True;
            break;
    if cleanAvailable:
        globalMap[nx][ny] = 2;
        x, y = nx, ny;
        answer += 1;
        d = nd;
    else:
        oppositeX, oppositeY = (x + dx[(d + 2) % 4], y + dy[(d + 2) % 4])
        if isBlocked(oppositeX, oppositeY): break;
        else: x, y = oppositeX, oppositeY;

print(answer);




