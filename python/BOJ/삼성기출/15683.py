import sys
from itertools import product
import copy

n, m = map(int, sys.stdin.readline().split());
board = [];
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())));

# 0 1 2 3 오른쪽부터 시작
# 1 2 3 4 5 타입

def checkLine(board, x, y, dir):
    point = 0;
    if dir == 0:
        for i in range(y + 1, m):
            if board[x][i] == '#': continue;
            elif board[x][i] == 6: break;
            elif board[x][i] == 0:
                point += 1;
                board[x][i] = '#';
            elif board[x][i] > 0:
                continue;
            else: print('error');
    elif dir == 1:
        for i in range(x + 1, n):
            if board[i][y] == '#': continue;
            elif board[i][y] == 6: break;
            elif board[i][y] == 0:
                point += 1;
                board[i][y] = '#';
            elif board[i][y] > 0: continue;
            else: print('error');
    elif dir == 2:
        for i in range(y - 1, -1, -1):
            if board[x][i] == '#':
                continue;
            elif board[x][i] == 6:
                break;
            elif board[x][i] == 0:
                point += 1;
                board[x][i] = '#';
            elif board[x][i] > 0:
                continue;
            else:
                print('error');
    else:
        for i in range(x -1, -1, -1):
            if board[i][y] == '#': continue;
            elif board[i][y] == 6: break;
            elif board[i][y] == 0:
                point += 1;
                board[i][y] = '#';
            elif board[i][y] > 0: continue;
            else: print('error');
    return point;

# point 0 0 0 0 좌표 타입 방향

def checkAllArea(board, cctv):
    x, y, dir = cctv[0], cctv[1], cctv[3];
    if cctv[2] == 1:
        return checkLine(board, x, y, dir);
    elif cctv[2] == 2:
        return checkLine(board, x, y, dir) + checkLine(board, x, y, (dir + 2) % 4);
    elif cctv[2] == 3:
        return checkLine(board, x, y, dir) + checkLine(board, x, y, (dir + 1) % 4);
    elif cctv[2] == 4:
        return checkLine(board, x, y, dir) + checkLine(board, x, y, (dir + 1) % 4) + checkLine(board, x, y, (dir + 2) % 4);
    else:
        return checkLine(board, x, y, dir) + checkLine(board, x, y, (dir + 1) % 4) + checkLine(board, x, y, (dir + 2) % 4) + checkLine(board, x, y, (dir + 3) % 4);

cctvs = [];
safeZones = n * m;
for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            safeZones -=1;
            cctvs.append([i, j, board[i][j], 0]);
        elif board[i][j] == 6:
            safeZones -= 1;

cctvTypes = {
    1: [(1, 0), (1, 1), (1, 2), (1, 3)],
    2: [(2, 0), (2, 1)],
    3: [(3, 0), (3, 1), (3, 2), (3, 3)],
    4: [(4, 0), (4, 1), (4, 2), (4, 3)],
    5: [(5, 0)]
}

answer = [];

def dfs(cctvIdx, board, count):
    global cctvs;
    if cctvIdx == len(cctvs):
        answer.append(safeZones - count);
        return;

    cctv = cctvs[cctvIdx];
    dirs = cctvTypes[cctv[2]];
    for dir in dirs:
        ncctv = copy.deepcopy(cctv);
        ncctv[3] = dir[1];
        tmpBoard = copy.deepcopy(board);
        area = checkAllArea(tmpBoard, ncctv);
        dfs(cctvIdx + 1, tmpBoard, count + area);

dfs(0, board, 0);
print(min(answer));


