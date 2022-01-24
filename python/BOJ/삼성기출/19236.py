# 문제 제대로 안 읽어서 2시간 반걸림
# n = 4니까 효율적인거 생각안나면 그냥 바로 풀자 (물고기 순서 저장하는 거)

import sys
import copy

board = [];
for i in range(4):
    arr = list(map(int, sys.stdin.readline().split()));
    row = [];
    for j in range(4):
        row.append((arr[j * 2], arr[j * 2 + 1] - 1));
    board.append(row);

dx = [-1, -1, 0, 1, 1, 1, 0, -1];
dy = [0, -1, -1, -1, 0, 1, 1, 1];

def moveFish(board):
    for i in range(1, 17):
        moveOneFish(board, i);

def moveOneFish(board, i):
    for x in range(4):
        for y in range(4):
            # 물고기 하나 이동
            if board[x][y][0] == i:
                idx, dir = board[x][y];
                for r in range(8):
                    nx = x + dx[(dir + r) % 8];
                    ny = y + dy[(dir + r) % 8];
                    if not (0 <= nx < 4 and 0 <= ny < 4): continue;
                    if board[nx][ny][0] == 17:
                        continue;
                    else:
                        board[x][y], board[nx][ny] = board[nx][ny], board[x][y];
                        board[nx][ny] = (board[nx][ny][0], (dir + r) % 8);
                        break;
                return;

def play(board, x, y, dir, point):
    global answer;
    moveFish(board);

    for i in range(1, 4):
        nx = x + dx[dir] * i;
        ny = y + dy[dir] * i;
        if not (0 <= nx < 4 and 0 <= ny < 4):
            answer = max(answer, sum(point));
            break;
        if board[nx][ny][0] == 0: continue;
        tmpBoard = copy.deepcopy(board);
        tmpBoard[x][y] = (0, 0);
        tmpBoard[nx][ny] = (17, board[nx][ny][1]);
        play(tmpBoard, nx, ny, board[nx][ny][1], point + ([board[nx][ny][0]]));

    answer = max(answer, sum(point));

answer = board[0][0][0];
board[0][0] = (17, board[0][0][1]);
play(board, 0, 0, board[0][0][1], [answer]);
print(answer);



