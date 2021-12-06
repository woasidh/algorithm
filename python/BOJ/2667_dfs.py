import sys
n = int(sys.stdin.readline());
graph = [];
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().split()[0]))));

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];
count = None;
def dfs(grpah, x, y):
    if graph[x][y] == 0: return False;
    global count;
    count += 1;
    graph[x][y] = 0;
    for i in range(4):
        nx = x + dx[i];
        ny = y + dy[i];
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0: continue;
            dfs(graph, nx, ny);
    return True;

total = 0;
arr = [];
for i in range(n):
    for j in range(n):
        count = 0;
        val = dfs(graph, i, j);
        if val != 0:
            arr.append(count);
            total += 1;
arr.sort();
print(total);
for val in arr:
    print(val);
