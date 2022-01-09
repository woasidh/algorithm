import sys
import copy

def move(globalMap, move):
    global n, answer;
    for i in range(n):
        if move == 0: row = globalMap[i];
        elif move == 1: row = list(reversed(globalMap[i]));
        elif move == 2: row = [row[i] for row in globalMap];
        else: row = [row[i] for row in list(reversed(globalMap))];
        visited = [False] * n;
        for colIdx in range(n - 1, -1, -1):
            if row[colIdx] == 0: continue;
            moveIdx = colIdx;
            while moveIdx + 1 < n and row[moveIdx + 1] == 0:
                moveIdx += 1;
            row[colIdx], row[moveIdx] = row[moveIdx], row[colIdx];
            # 같으면 합치고 다르면 냅두기
            if moveIdx == n - 1: continue;
            if row[moveIdx + 1] == row[moveIdx] and not visited[moveIdx + 1]:
                visited[moveIdx + 1] = True;
                row[moveIdx + 1] = row[moveIdx] * 2;
                answer = max(answer, row[moveIdx] * 2);
                row[moveIdx] = 0;
        if move == 0:
            globalMap[i] = row;
        elif move == 1:
            globalMap[i] = list(reversed(row));
        elif move == 2:
            for j in range(n):
                globalMap[j][i] = row[j];
        else:
            for j in range(n):
                globalMap[j][i] = list(reversed(row))[j];

# 0, 1, 2, 3 - 동, 서, 남, 북
def run(globalMap, dir, count):
    if count == 4: return;
    move(globalMap, dir);

    for i in range(4):
        run(copy.deepcopy(globalMap), i, count + 1);

answer, moveCount = 0, 0;
n = int(sys.stdin.readline());
globalMap = [];
for _ in range(n):
    globalMap.append(list(map(int, sys.stdin.readline().split())));
answer = max([max(row) for row in globalMap]);
for i in range(4):
    run(copy.deepcopy(globalMap), i, 0);
print(answer);
