# 포기...

import sys

n, _ = map(int, sys.stdin.readline().split());
board = [];
for _ in range(2**n):
    board.append(list(map(int, sys.stdin.readline().split())));
qs = list(map(int, sys.stdin.readline().split()));

def rotate(board, n):
    # 1 2 3
    # 4 5 6
    # 7 8 9
    newBoard = [];
    for i in range(n):
        newRow = [row[i] for row in list(reversed(board))];
        newBoard.append(newRow);
    return newBoard;


def divideAndRotate(board, n, l):
    divided = 2**(n - l);
    newBoard = [[] for _ in range(2**n)];
    for i in range(divided):
        for j in range(divided):
            semiBoard = [];
            for k in range((2**l)*i, (2**l)*(i + 1)):
                semiRow = [];
                for m in range((2**l)*j, (2**l)*(j + 1)):
                    semiRow.append(board[k][m]);
                semiBoard.append(semiRow);
            semiBoard = rotate(semiBoard, 2**l);
            # for idx, row in enumerate(semiBoard):
            #     newBoard[i*(2**l) + idx].append(row);
    return newBoard;



for q in qs:
    board = divideAndRotate(board, n, q);