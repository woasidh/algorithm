# dfs 너무 약한듯...
# idx 조건 잘보자
# 1시간은 걸린듯...

import sys
n = int(sys.stdin.readline());
schedules = [];
for _ in range(n):
    day, cost = map(int, sys.stdin.readline().split());
    schedules.append((day, cost));

answer = -1;

def dfs(currentDay, currentCost, path):
    global visited, schedules, answer;
    for i in range(currentDay, n):
        day, cost = schedules[i];
        if i + day > n: continue;
        dfs(i + day, currentCost + cost, path + str(i + 1));
    answer = max(answer, currentCost);

dfs(0, 0, '');
print(answer);