import sys

n = int(sys.stdin.readline());
classes = [];

for _ in range(n):
    classes.append(list(map(int, sys.stdin.readline().split())));

classes.sort(key = lambda x: (x[1], x[0]));
currentEnd = None;
answer = 0;

for idx, c in enumerate(classes):
    if idx == 0:
        answer += 1;
        currentEnd = c[1];
    else:
        start, end = c;
        if start < currentEnd: continue;
        else:
            currentEnd = end;
            answer += 1;

print(answer);