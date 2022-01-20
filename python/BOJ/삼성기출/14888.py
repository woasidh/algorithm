# 시간 초과나면 PyPy3로 제출하자
# dfs로 풀기

import sys
from itertools import permutations
import copy

opOrder = ['+', '-', '*', '/'];

n = int(sys.stdin.readline());
nums = list(map(int, sys.stdin.readline().split()));
opCounts = map(int, sys.stdin.readline().split());
ops = [];
vals = [];
for idx, opCount in enumerate(opCounts):
    if idx == 0:
        ops += ['+' for i in range(opCount)];
    elif idx == 1:
        ops += ['-' for i in range(opCount)];
    elif idx == 2:
        ops += ['*' for i in range(opCount)];
    else:
        ops += ['/' for i in range(opCount)];

def operate(num1, num2, op):
    if op == '+': return num1 + num2;
    elif op =='-': return num1 - num2;
    elif op == '*': return num1 * num2;
    else:
        if num1 < 0:
            return -((-num1) // num2) ;
        elif num1 == 0: return 0;
        else:
            return num1 // num2;

minNum = None;
maxNum = None;

def calc(nums, ops):
    global minNum, maxNum;
    tmpNums = copy.deepcopy(nums);
    for idx, num in enumerate(tmpNums):
        if idx == len(tmpNums) - 1: break;
        tmpNums[idx + 1] = operate(num, tmpNums[idx + 1], ops[idx]);
    vals.append(tmpNums[-1])


for opOrder in permutations(ops, len(ops)):
    calc(nums, list(opOrder));
print(max(vals));
print(min(vals));

