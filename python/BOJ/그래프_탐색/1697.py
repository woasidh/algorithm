import sys
import heapq

n, m = map(int, sys.stdin.readline().split());
visited = [False for _ in range(100001)];
visited[n] = True;

def bfs(n, m):
    hq = [];
    heapq.heappush(hq, (0, n));
    while hq:
        count, x = heapq.heappop(hq);
        if x == m:
            print(count);
            return;
        if (0 <= x - 1 < 100001) and not visited[x - 1]:
            visited[x - 1] = True;
            heapq.heappush(hq, (count + 1, x - 1));
        if (0 <= x + 1 < 100001) and not visited[x + 1]:
            visited[x + 1] = True;
            heapq.heappush(hq, (count + 1, x + 1));
        if (0 <= 2 * x < 100001) and not visited[2 * x]:
            visited[2 * x] = True;
            heapq.heappush(hq, (count + 1, 2 * x));

bfs(n, m);
