def solution(s):
    answer = -1

    stack = [];
    for char in s:
        if not stack:
            stack.append(char);
            continue;
        else:
            if stack[-1] == char:
                stack.pop();
            else:
                stack.append(char);

    return 1 if len(stack) == 0 else 0;