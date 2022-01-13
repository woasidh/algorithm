# js로 쌉가능
# 왜 사과 없어지는 거 생각 못했는지....

import sys

n = int(sys.stdin.readline());
board = [[0 for i in range(n)] for i in range(n)];
k = int(sys.stdin.readline());
apples = [];
for _ in range(k):
    apples.append(list(map(int, sys.stdin.readline().split())));
for apple in apples:
    board[apple[0] - 1][apple[1] - 1] = 1;
l = int(sys.stdin.readline());
commands = [];
for _ in range(l):
    commands.append(list(sys.stdin.readline().split()));
for i in range(len(commands)):
    commands[i][0] = int(commands[i][0]);

def getNextBlock(block, dir):
    x, y = block;
    if dir == 0:
        return (x, y + 1);
    elif dir == 1:
        return (x + 1, y);
    elif dir == 2:
        return (x, y - 1);
    else:
        return (x -1, y);

currentBlock = (0, 0);
path = [(0, 0)];
# 0 1 2 3 동 남 서 북
time = 0;
dir = 0 # 동으로 시작
while True:
    x, y = getNextBlock(currentBlock, dir);
    if not (0 <= x < n and 0 <= y < n): break;
    if (x, y) in path: break;

    #사과 있는 지 확인
    path.append((x, y));
    if board[x][y] == 0: del path[0];
    else: board[x][y] = 0;

    time += 1;
    if commands and time == commands[0][0]:
        if commands[0][1] == 'D':
            dir = (dir + 1) % 4;
        else:
            dir = (dir - 1) % 4;
        del commands[0];
    currentBlock = (x, y);

print(time + 1);
