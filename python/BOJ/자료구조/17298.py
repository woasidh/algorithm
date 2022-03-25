import sys

n = int(sys.stdin.readline());
nums = list(map(int, sys.stdin.readline().split()));

stack = [];
answers = [-1 for _ in range(n)];

for idx, num in enumerate(nums):
    if not stack:
        stack.append((num, idx));
    else:
        while stack and stack[-1][0] < num:
            answers[stack[-1][1]] = num;
            stack.pop();
        stack.append((num, idx));

for answer in answers:
    print(answer, end=' ')
