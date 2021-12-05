import sys
from collections import deque
n, m = list(map(int, sys.stdin.readline().split()));
graph = [];
visited = [];
for _ in range(0, n):
    graph.append(list(map(int, list(''.join(sys.stdin.readline().split())))));
    visited.append([False] * m);

answer = -1;
q = deque([]);
dx = [-1, 1, 0, 0];
dy = [0, 0, -1, 1];
def bfs(graph, x, y):
    global answer;
    q.append((x, y, 1));
    while q:
        x, y, dist = q.popleft();
        if x == n -1 and y == m -1:
            answer = max(answer, dist);
            continue;
        for i in range(0, 4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue;
            if graph[nx][ny] == 0: continue;
            if visited[nx][ny]: continue;
            q.append((nx, ny, dist + 1));
            visited[nx][ny] = True;
    return answer;

print(bfs(graph, 0, 0));