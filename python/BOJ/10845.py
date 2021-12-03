from collections import deque
import sys

n = int(sys.stdin.readline());
queue = deque([]);

for _ in range(0, n):
    commandArr = sys.stdin.readline().split();

    if len(commandArr) == 1:
        command = commandArr[0];
        if command == 'front':
            output = queue[0] if queue else -1;
            print(output);
        elif command == 'back':
            output = queue[-1] if queue else -1;
            print(output);
        elif command == 'size':
            print(len(queue));
        elif command == 'empty':
            output = 0 if queue else 1;
            print(output);
        elif command == 'pop':
            if len(queue) > 0:
                print(queue.popleft());
            else:
                print(-1);

    # push
    else:
        value = commandArr[1];
        queue.append(value);


