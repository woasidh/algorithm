n = int(input())

def isVPS(str):

    stack = [];

    for char in str:
        if char == '(':
            stack.append(char);
        else:
            if len(stack) == 0:
                return 'NO';
            if stack[-1] == '(':
                stack.pop();
            else:
                return 'NO';

    return 'YES' if len(stack) == 0 else 'NO';


for _ in range(0, n):
    print(isVPS(input()));
