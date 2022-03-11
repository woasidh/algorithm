import sys
from collections import deque

n = int(sys.stdin.readline());
board = [];
for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline())[:-1])));

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];

def bfs(board, x, y):
    if board[x][y] == 0: return 0;
    area = 1;
    q = deque([]);
    board[x][y] = 0;
    q.append((x, y));
    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if not (0 <= nx < n and 0 <= ny < n): continue;
            if board[nx][ny] == 0: continue;
            area += 1;
            board[nx][ny] = 0;
            q.append((nx, ny));

    return area;

totalArea = 0;
areas = [];
for i in range(n):
    for j in range(n):
        area = bfs(board, i, j);
        if area != 0:
            totalArea += 1;
            areas.append(area);

print(totalArea);
areas.sort();
for area in areas:
    print(area);