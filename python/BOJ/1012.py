import sys
from collections import deque

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];

def bfs(graph, x, y):
    if graph[x][y] == 0: return False;
    row, col = len(graph), len(graph[0]);
    q = deque([]);
    q.append((x, y));
    graph[x][y] = 0;

    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or nx >= row or ny < 0 or ny >= col: continue;
            if graph[nx][ny] == 0: continue;
            q.append((nx, ny));
            graph[nx][ny] = 0;
    return True;


def runBfs(graph):
    val = 0;
    for i in range(n):
        for j in range(m):
            if bfs(graph, i, j):
                val += 1;
    print(val);

case = int(sys.stdin.readline());
for _ in range(case):
    n, m, k = map(int, (sys.stdin.readline().split()));
    graph = [[0 for i in range(m)] for j in range(n)];
    for _ in range(k):
        x, y = map(int, (sys.stdin.readline().split()));
        graph[x][y] = 1;
    runBfs(graph);


