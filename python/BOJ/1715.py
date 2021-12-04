import sys
import heapq
n = int(sys.stdin.readline());
nums = [];
for _ in range(0, n):
    heapq.heappush(nums, int(sys.stdin.readline()));

answer = 0;
while nums:
    if len(nums) == 1:
        break;
    else:
        n1 = heapq.heappop(nums);
        n2 = heapq.heappop(nums);
        heapq.heappush(nums, n1 + n2);
        answer += (n1 + n2);
print(answer);


