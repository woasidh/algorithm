import math
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split());
board = [];
waters = [];
s, d = None, None;

for _ in range(n):
    board.append(list(sys.stdin.readline().strip()));

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            waters.append([i, j]);
        elif board[i][j] == 'S':
            s = [0, i, j];

visited = [[False for _ in range(m)] for _ in range(n)];

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];
def flow(board):
    global waters, n, m;
    newWaters = [];
    for water in waters:
        x, y = water;
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 'S' or board[nx][ny] == '.' and [nx, ny] not in newWaters:
                    newWaters.append([nx, ny]);

    for water in newWaters:
        x, y = water;
        board[x][y] = '*';

    waters = newWaters;

answer = math.inf;

def move(board, visited):
    global q, answer;
    newQ = deque([]);
    while q:
        count, x, y = q.popleft();
        # print(x, y, count, '노드에서 꺼냄')
        if board[x][y] == '*': continue;
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if 0 <= nx < n and 0 <= ny < m:
                # print(visited, i, board[nx][ny]);
                if visited[nx][ny]: continue;
                if board[nx][ny] == '.':
                    # print(nx, ny, count + 1, '큐에 넣음')
                    newQ.append([count + 1, nx, ny]);
                    visited[nx][ny] = True;
                elif board[nx][ny] == 'D':
                    # print(nx, ny, count + 1, '찾음');
                    answer = min(answer, count + 1);
    q = newQ;
    return len(newQ);

q = deque([]);
q.append(s);
visited = [[False for _ in range(m)] for _ in range(n)];

while True:
    created = move(board, visited);
    if created == 0: break;
    flow(board);

print(answer if answer != math.inf else 'KAKTUS');


