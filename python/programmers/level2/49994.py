def solution(dirs):
    answer = 0
    currentPosition = (0, 0);
    pathSet = set([]);
    for dir in dirs:
        newPosition = move(dir, currentPosition);
        if newPosition != currentPosition:
            if dir == 'U' or dir == 'R':
                pathSet.add(''.join(list(map(str, currentPosition + newPosition))));
            else:
                pathSet.add(''.join(list(map(str, newPosition + currentPosition))));
            currentPosition = newPosition;
    return len(pathSet);

def move(command, position):
    x, y = position;
    if command == 'U': y += 1;
    elif command == 'D': y -= 1;
    elif command == 'R': x += 1;
    else: x -= 1;
    if not (-5 <= x <= 5 and -5 <= y <= 5): return position;
    else: return (x, y);