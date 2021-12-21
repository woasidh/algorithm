import sys
from collections import deque

dx = [0, 0, 1, -1];
dy = [-1, 1, 0, 0];
def bfs(graph, x, y):
    n, m = len(graph), len(graph[0]);
    visited = [[False] * m for i in range(n)];
    q = deque([]);
    q.append((x, y));
    visited[x][y] = True;
    while q:
        x, y = q.popleft();
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i];
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == True: continue;
                if graph[nx][ny] == 'X':
                    s.add((nx, ny));
                elif graph[nx][ny] == '.':
                    visited[nx][ny] = True;
                    q.append((nx, ny));
                else: return True;
    return False;

def findStart(graph):
    x1, y1, x2, y2 = None, None, None, None;
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'L':
                if not x1 and not y1:
                    x1, y1 = i, j;
                else:
                    x2, y2 = i, j;
                    return (x1, y1, x2, y2);

r, c = map(int, sys.stdin.readline().split());
graph = [];
for _ in range(r):
    graph.append(list(''.join(sys.stdin.readline().split())));

startX, startY, endX, endY = findStart(graph);
answer = 0;
while True:
    s = set([]);
    if bfs(graph, startX, startY) or bfs(graph, endX, endY):
        print(answer);
        break;
    for comb in s: graph[comb[0]][comb[1]] = '.';
    answer += 1;




