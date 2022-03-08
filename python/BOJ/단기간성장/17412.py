import sys

def dfs(pathMap, start, end, path, visited):
    global pathIncluded, answer;
    if start == end:
        answer += 1;
        for i in range(len(path) - 1):
            start, end = path[i], path[i + 1];
            pathIncluded[str(start)+str(end)] = True;
        return;

    destinations = pathMap[start];
    for destination in destinations:
        if visited[destination]: continue;
        if str(start) + str(destination) in pathIncluded: continue;
        visited[destination] = True;
        dfs(pathMap, destination, end, path + [destination], visited);
        visited[destination] = False;

n, p = map(int, sys.stdin.readline().split());
pathMap = {};
for i in range(1, n + 1):
    pathMap[i] = [];

for _ in range(p):
    start, end = map(int, sys.stdin.readline().split());
    pathMap[start].append(end);

pathIncluded = {};
answer = 0;
visited = [False for _ in range(n + 1)];
dfs(pathMap, 1, 2, [1], visited);

print(answer);