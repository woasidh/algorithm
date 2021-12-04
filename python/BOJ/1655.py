import heapq
import sys

hq1 = [];
hq2 = [];

n = int(sys.stdin.readline());
for idx, _ in enumerate(range(0, n)):
    num = int(sys.stdin.readline());
    if len(hq1) == len(hq2):
        heapq.heappush(hq1, (-num, num));
    else:
        heapq.heappush(hq2, (num, num));
    if hq2 and hq1[0][1] > hq2[0][1]:
        max = heapq.heappop(hq1)[1];
        min = heapq.heappop(hq2)[1];
        heapq.heappush(hq2, (max, max));
        heapq.heappush(hq1, (-min, min));
    print(hq1[0][1]);


