# 각각 방향이 우 / 하 / 좌 / 상일 때 좌표 변경값
dx = [0, 1, 0, -1];
dy = [1, 0, -1, 0];

def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)];

    dirs = None;
    if clockwise: dirs = [0, 1, 3, 2];
    else: dirs = [1, 2, 0, 3];

    vertexes = [(0, 0, dirs[0]), (0, n - 1, dirs[1]), (n - 1, 0, dirs[2]), (n - 1, n - 1, dirs[3])];

    fillOneCurve((0, 0, dirs[0]), n, clockwise, answer);

    # for vertex in vertexes:
    #     fillOneCurve(vertex, n, clockwise, answer);

    print('fucasdfsdfsk');
    for row in answer:
        print(row);

    return answer

def fillOneCurve(vertex, n, clockwise, answer):
    diff = 1;
    diff2 = 0;
    fillCount = 1;
    x, y, dir = vertex;
    isCenter = False;
    centers = [];
    if n % 2 == 1:
        centers.append([n//2, n//2]);
    else:
        centers = [[n/2 - 1, n/2], [n/2, n/2 - 1], [n/2 -1, n/2 - 1], [n/2, n/2]];

    print(centers);

    while True:
        for i in range(n - diff - diff2):
            if [x, y] in centers:
                answer[x][y] = fillCount;
                isCenter = True;
                break;
            answer[x][y] = fillCount;
            if i != (n - diff - diff2 - 1):
                x, y = x + dx[dir], y + dy[dir];
                fillCount += 1;
            else: break;
            print(x, y, i, n - diff - diff2, fillCount);
        if isCenter: break;
        if clockwise: dir = (dir + 1) % 4;
        else: dir = (dir - 1) % 4;

        diff += 1;
        if diff >= 3: diff2 += 1;

    print('fuck');

solution(7, False);

