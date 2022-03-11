# 와 미쳤다...
# baord에 일자 저장하면 됨

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split());
board = [];
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())));

ripedList = [];
noRipes = 0;
for i in range(n):
    for j in range(m):
        if board[i][j] == 0: noRipes += 1;
        elif board[i][j] == 1: ripedList.append([i, j]);

answer = 0;

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];

def spreadTomatoCell(board, visited, x, y, toSpread):
    global ripedList;
    if board[x][y] == 0: return 0;
    if board[x][y] == -1: return 0;
    q = deque([]);
    q.append((x, y));
    visited[x][y] = True;
    spreaded = 0;
    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if not (0 <= nx < n and 0 <= ny < m): continue;
            if board[nx][ny] == -1: continue;
            elif board[nx][ny] == 0:
                ripedList.append([nx, ny]);
                toSpread.add(str(nx)+':'+str(ny));
                spreaded += 1;
            elif not visited[nx][ny]:
                visited[nx][ny] = True;
                q.append((nx, ny));
    return spreaded;


def spreadTomato(board):
    global n, m, ripedList;
    toSpread = set([]);
    visited = [[False for _ in range(m)] for _ in range(n)];

    for riped in ripedList:
        x, y = riped;
        spreadTomatoCell(board, visited, x, y, toSpread);

    ripedList = [];

    for coordinateStr in toSpread:
        x, y = map(int, coordinateStr.split(':'));
        board[x][y] = 1;
        ripedList.append([x, y]);

    return len(toSpread);

while True:
    count = spreadTomato(board);
    if count == 0: break;
    noRipes -= count;
    answer += 1;

print(answer if noRipes == 0 else -1);