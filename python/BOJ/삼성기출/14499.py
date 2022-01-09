import sys

dx = [0, 0, -1, 1];
dy = [1, -1, 0, 0];
def run(dice, globalMap, move):
    global x, y;
    nx = x + dx[move - 1];
    ny = y + dy[move - 1];
    if not (0 <= nx < n and 0 <= ny < m): return;
    updateDice(dice, move);
    if globalMap[nx][ny] == 0:
        globalMap[nx][ny] = dice[1][1];
    else:
        dice[1][1] = globalMap[nx][ny];
        globalMap[nx][ny] = 0;
    x, y = nx, ny;
    print(dice[3][1]);
    return;

def updateDice(dice, move):
    if move == 1:
        arr = dice[1] + [dice[3][1]];
        dice[1] = arr[1:];
        dice[3][1] = arr[0];
    elif move == 2:
        arr = dice[1] + [dice[3][1]];
        dice[1] = [arr[-1]] + arr[:2];
        dice[3][1] = arr[2];
    elif move == 3:
        arr = [row[1] for row in dice];
        arr = [arr[3]] + arr;
        del arr[4];
        for i in range(4):
            dice[i][1] = arr[i];
    else:
        arr = [row[1] for row in dice];
        arr.append(arr[0]);
        del arr[0];
        for i in range(4):
            dice[i][1] = arr[i];

dice = [[0] * 3 for i in range(4)];
moves = None;
n, m, x, y, k = map(int, sys.stdin.readline().split());
globalMap = [];
for _ in range(n):
    globalMap.append(list(map(int, sys.stdin.readline().split())));
moves = list(map(int, sys.stdin.readline().split()));
for move in moves:
    run(dice, globalMap, move);


