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
                point += 1;
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
        return checkLine(board, x, y, dir) + checkLine(board, x, y, dir + 1);
    elif cctv[2] == 4:
        return checkLine(board, x, y, dir) + checkLine(board, x, y, dir + 1) + checkLine(board, x, y, dir + 2);
    else:
        return checkLine(board, x, y, dir) + checkLine(board, x, y, dir + 1) + checkLine(board, x, y, dir + 2) + checkLine(board, x, y, dir + 3);

cctvs = [];
safeZones = n * m;
for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            safeZones -=1;
            cctvs.append([i, j, 0, 0]);
        elif board[i][j] == 6:
            safeZones -= 1;

pointTypes = [(1, 0), (1, 1), (1, 2), (1, 2), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (5, 0)];
products = list(product(pointTypes, repeat=len(cctvs)));
answer = [];
for product in products:
    print(product);
    tmpBoard = copy.deepcopy(board);
    for idx in range(len(cctvs)):
        cctvs[idx][2], cctvs[idx][3] = product[idx][0], product[idx][1];
    point = 0;
    for cctv in cctvs:
        point += checkAllArea(tmpBoard, cctv);
    # print(point);
    # for row in tmpBoard:
    #     print(row);
    # print();
    answer.append(safeZones - point);
# print();
print(max(answer));


