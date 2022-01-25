import sys

n, k = map(int, sys.stdin.readline().split());
areaTypes = [];
for _ in range(n):
    areaTypes.append(list(map(int, sys.stdin.readline().split())));
board = [];
for i in range(n):
    row = [];
    for j in range(n):
        row.append([]);
    board.append(row);
horseInfos = [];
for i in range(1, k + 1):
    x, y, dir = map(int, sys.stdin.readline().split());
    board[x - 1][y - 1].append(i);
    horseInfos.append([x - 1, y - 1, dir]);

dx = [-100, 0, 0, -1, 1];
dy = [-100, 1, -1, 0, 0];

def getReversedDir(dir):
    if dir == 1: return 2;
    elif dir == 2: return 1;
    elif dir == 3: return 4;
    else: return 3;

def run():
    global areaTypes, board, n, k, horseInfos;
    for horseNum, horseInfo in enumerate(horseInfos):
        horseNum += 1;
        x, y, dir = horseInfo;
        currentHorses = board[x][y];
        moveHorses = currentHorses[currentHorses.index(horseNum):];
        restHorses = currentHorses[:currentHorses.index(horseNum)];
        nx, ny = x + dx[dir], y + dy[dir];
        # 파랑
        if not (0 <= nx < n and 0 <= ny < n) or areaTypes[nx][ny] == 2:
            nx, ny = x + dx[getReversedDir(dir)], y + dy[getReversedDir(dir)];
            if not (0 <= nx < n and 0 <= ny < n) or areaTypes[nx][ny] == 2:
                horseInfos[horseNum - 1][2] = getReversedDir(dir);
            elif areaTypes[nx][ny] == 0:
                for movedHorse in moveHorses:
                    horseInfos[movedHorse - 1][0] = nx;
                    horseInfos[movedHorse - 1][1] = ny;
                board[x][y] = restHorses;
                board[nx][ny] = board[nx][ny] + moveHorses;
                if len(board[nx][ny]) >= 4: return True;
                horseInfos[horseNum - 1][2] = getReversedDir(dir);
            elif areaTypes[nx][ny] == 1:
                for movedHorse in moveHorses:
                    horseInfos[movedHorse - 1][0] = nx;
                    horseInfos[movedHorse - 1][1] = ny;
                board[x][y] = restHorses;
                board[nx][ny] = board[nx][ny] + list(reversed(moveHorses));
                if len(board[nx][ny]) >= 4: return True;
                horseInfos[horseNum - 1][2] = getReversedDir(dir);
        # 흰색일 때
        elif areaTypes[nx][ny] == 0:
            for movedHorse in moveHorses:
                horseInfos[movedHorse - 1][0] = nx;
                horseInfos[movedHorse - 1][1] = ny;
            board[x][y] = restHorses;
            board[nx][ny] = board[nx][ny] + moveHorses;
            if len(board[nx][ny]) >= 4: return True;
        # 빨강
        elif areaTypes[nx][ny] == 1:
            for movedHorse in moveHorses:
                horseInfos[movedHorse - 1][0] = nx;
                horseInfos[movedHorse - 1][1] = ny;
            board[x][y] = restHorses;
            board[nx][ny] = board[nx][ny] + list(reversed(moveHorses));
            if len(board[nx][ny]) >= 4: return True;
    return False;

turn = 0;
while True:
    turn += 1;
    if run(): break;
    if turn > 1000:
        print(-1);
        turn = -1;
        break;
if turn != -1: print(turn);

