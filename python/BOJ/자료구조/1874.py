import sys

n = int(sys.stdin.readline());

stack = [];
nums = [];

for i in range(n):
    nums.append(int(sys.stdin.readline()));

def solution():
    currentIdx = 0;
    answers = [];
    for i in range(1, n + 1):
        stack.append(i);
        answers.append('+');
        while stack and stack[-1] == nums[currentIdx]:
            answers.append('-');
            stack.pop();
            currentIdx += 1;
    if not stack:
        for answer in answers:
            print(answer);
    else:
        print('NO');

solution();

