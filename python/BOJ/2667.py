import sys
from collections import deque

n = int(sys.stdin.readline());
graph = [];
for _ in range(0, n):
    str = sys.stdin.readline().split()[0];
    graph.append(list(map(int, list(str))));

dx = [0, 0, -1, 1];
dy = [-1, 1, 0, 0];

def bfs(graph, x, y):
    total = 1;
    q = deque([]);
    if graph[x][y] == 0: return 0;
    q.append((x, y));
    graph[x][y] = 0;
    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue;
            if graph[nx][ny] == 0: continue;
            q.append((nx, ny));
            graph[nx][ny] = 0;
            total += 1;
    return total;

total = 0;
arr = [];
for i in range(n):
    for j in range(n):
        val = bfs(graph, i, j);
        if val > 0:
            total += 1;
            arr.append(val);

arr.sort();
print(total);
for val in arr:
    print(val);