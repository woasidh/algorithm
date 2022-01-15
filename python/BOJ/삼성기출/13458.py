import sys
import math

n = int(sys.stdin.readline());
students = list(map(int, sys.stdin.readline().split()));
b, c = map(int, sys.stdin.readline().split());

answer = 0;

# if c >= b:
#     for studentNum in students:
#         answer += math.ceil(studentNum / c);
#     print(answer);
# else:
for studentNum in students:
    # 감독관
    studentNum -= b;
    answer += 1;
    if studentNum > 0:
        answer += math.ceil(studentNum /c);
print(answer);