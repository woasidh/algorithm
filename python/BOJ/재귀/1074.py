import sys

n, r, c = map(int, sys.stdin.readline().split());

dx = [0, 0, 1, 1];
dy = [0, 1, 0, 1];

def recordRecursive(board, n, offsetX, offsetY, currentCount):
    if n == 1:
        for i in range(4):
            board[offsetX + dx[i]][offsetY + dy[i]] = (currentCount);
            currentCount += 1;
        return 4;
    a = 0;
    for i in range(4):
        a += recordRecursive(board, n - 1, offsetX + 2**(n - 1)*dx[i], offsetY + 2**(n - 1)*dy[i], currentCount + a);

    return a;

def solution(n, r, c):
    if n == 1: return 0;
    board = [[-1 for _ in range(2**n)] for _ in range(2**n)];
    currentCount = 0;
    for i in range(4):
        currentCount += recordRecursive(board, n - 1, 2 ** (n - 1) * dx[i], 2 ** (n - 1) * dy[i], currentCount);

    return board[r][c];

print(solution(n, r, c));