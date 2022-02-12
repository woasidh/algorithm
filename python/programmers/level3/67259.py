# dfs도 최적화시킬 수 있음
# 가는 곳마다 board에 값 저장해서 더 크면 안가는 걸로

import math

visited = None;
answer = None;


def solution(board):
    global visited, answer;
    n = len(board);
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: board[i][j] = math.inf;
    # visited = [[False for i in range(n)] for i in range(n)];
    # visited[0][0] = True;
    dfs(board, 0, 0, 0, n, -1);
    return board[n - 1][n - 1];


dx = [0, 1, 0, -1];
dy = [1, 0, -1, 0];


def dfs(board, cost, x, y, n, currentDir):
    global visited, answer;
    if answer and cost > answer: return;
    if [x, y] == [n - 1, n - 1]:
        board[x][y] = min(board[x][y], cost);
        return;

    for i in range(4):
        nx = x + dx[i];
        ny = y + dy[i];
        if not (0 <= nx < n and 0 <= ny < n): continue;
        if board[nx][ny] == 1: continue;
        # if visited[nx][ny]: continue;
        addCost = 100 if i == currentDir or currentDir == -1 else 600;
        if board[nx][ny] < cost + addCost: continue;
        board[nx][ny] = cost + addCost;
        # visited[nx][ny] = True;
        dfs(board, cost + addCost, nx, ny, n, i);
        # visited[nx][ny] = False;