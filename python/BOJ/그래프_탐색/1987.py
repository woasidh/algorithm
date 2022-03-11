import copy
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split());
board = [];

for _ in range(n):
    board.append(list(sys.stdin.readline().strip()));

dx = [0, 0, 1, -1];
dy = [-1, 1, 0, 0];
answer = -1;

# def bfs(board, x, y):
#     global answer;
#     q = deque([]);
#     q.append((x, y, board[x][y], 1));
#     while q:
#         x, y, path, count = q.popleft();
#         answer = max(answer, count);
#         for i in range(4):
#             nx = x + dx[i];
#             ny = y + dy[i];
#             if not (0 <= nx < n and 0 <= ny < m): continue;
#             if not board[nx][ny] in path:
#                 q.append((nx, ny, path+board[nx][ny], count + 1));

def dfs(board, x, y, path, count):
    global answer;
    answer = max(answer, count);
    for i in range(4):
        nx = x + dx[i];
        ny = y + dy[i];
        if not (0 <= nx < n and 0 <= ny < m): continue;
        if not path[board[nx][ny]]:
            path[board[nx][ny]] = True;
            dfs(board, nx, ny, path, count + 1);
            path[board[nx][ny]] = False;

path = {};
for i in range(65, 91):
    path[chr(i)] = False;
path[board[0][0]] = True;
dfs(board, 0, 0, path, 1);
# bfs(board, 0, 0);
print(answer);