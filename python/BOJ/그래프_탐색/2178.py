import sys
import heapq

n, m = map(int, sys.stdin.readline().split());
board = [];
for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline())[:-1])));

dx = [-1, 1, 0, 0];
dy = [0, 0, 1, -1];

visited = [[False for _ in range(m)] for _ in range(n)];
visited[0][0] = True;

# def dfs(board, visited, x, y, count):
#     global answer, n;
#     if count >= answer: return;
#     if x == n -1 and y == m - 1:
#         answer = min(answer, count);
#         return;
#
#     for i in range(4):
#         nx = x + dx[i];
#         ny = y + dy[i];
#         if not (0 <= nx < n and 0 <= ny < m): continue;
#         if visited[nx][ny] or board[nx][ny] == 0: continue;
#         visited[nx][ny] = True;
#         dfs(board, visited, nx, ny, count + 1);
#         visited[nx][ny] = False;

def bfs(board, visited, x, y):
    global n;
    hq = [];
    heapq.heappush(hq, (1, x, y));
    visited[x][y] = True;
    while hq:
        count, x, y = heapq.heappop(hq);
        if x == n -1 and y == m - 1:
            return count;
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if not (0 <= nx < n and 0 <= ny < m): continue;
            if visited[nx][ny] or board[nx][ny] == 0: continue;
            visited[nx][ny] = True;
            heapq.heappush(hq, (count + 1, nx, ny));

print(bfs(board, visited, 0, 0));