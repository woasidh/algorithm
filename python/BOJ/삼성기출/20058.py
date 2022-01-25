import sys

n, q = map(int, sys.stdin.readline().split());
board = [];
for _ in range(2**n):
    board.append(list(map(int, sys.stdin.readline().split())));
qs = list(map(int, sys.stdin.readline().split()));

def rotate(board, n):
    # 1 2 3
    # 4 5 6
    # 7 8 9


def divideAndRotate(board, n, l):
    print(n, l);

for q in qs:
    divideAndRotate(board, n, q);