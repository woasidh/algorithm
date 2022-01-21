# boolean 2차원 배열로 생각하자
# PyPy3로 풀자 ㅡㅡ
# setrecursionlimit 푸니까 메모리초과 안남

import sys
sys.setrecursionlimit(1000);

n, m, h = map(int, sys.stdin.readline().split());
lines = [[False for i in range(n + 1)] for i in range(h + 1)];
for _ in range(m):
    row, col = map(int, sys.stdin.readline().split());
    lines[row][col] = True;
answer = None;

def play():
    global n, h;
    for col in range(1, n + 1):
        x, y = 1, col;
        while True:
            if lines[x][y]:
                x, y = x + 1, y + 1;
            elif lines[x][y - 1]:
                x, y = x + 1, y - 1;
            else:
                x, y = x + 1, y;
            if x == h + 1: break;
        if y != col:
            return False;
    return True;

def dfs(count, x, y):
    global n, h, lines, answer;

    if play():
        # print(count, '로 찾음');
        if not answer: answer = count;
        else: answer = min(answer, count);
        return;
    else:
        if count >= 3: return;
        elif answer and count >= answer: return;

    for i in range(x, h + 1):
        if i != x: y = 1;
        for j in range(y, n):
            # print(i, j);
            if lines[i][j]: continue;
            if lines[i][j - 1] or lines[i][j + 1]: continue;
            lines[i][j] = True;
            dfs(count + 1, i, j + 2);
            lines[i][j] = False;

dfs(0, 1, 1);
if answer == None:
    print(-1);
else:
    print(answer if answer <= 3 else -1);