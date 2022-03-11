# visited 2중 배열로 하기

import sys
import heapq

n, m = map(int, sys.stdin.readline().split());
board = [];

for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline().strip()))));

visited = [[[False, False] for _ in range(m)] for _ in range(n)];

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];

def bfs(board, x, y, visited):
    hq = [];
    visited[x][y][1] = True;
    # 이동횟수 / x / y / 남은 벽 뚫는 기회
    heapq.heappush(hq, (1, x, y, 1));
    while hq:
        count, x, y, life = heapq.heappop(hq);

        if x == n -1 and y == m - 1:
            return count;

        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if not (0 <= nx < n and 0 <= ny < m): continue;
            if board[nx][ny] == 1 and life >= 1:
                if visited[nx][ny][0]: continue;
                visited[nx][ny][0] = True;
                heapq.heappush(hq, (count + 1, nx, ny, life - 1));
            if board[nx][ny] == 0:
                if visited[nx][ny][life]: continue;
                visited[nx][ny][life] = True;
                heapq.heappush(hq, (count + 1, nx, ny, life));

    return -1;

print(bfs(board, 0, 0, visited));