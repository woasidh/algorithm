from collections import deque;
import math


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses);

    while progresses:
        progress, speed = progresses[0], speeds[0];
        day = math.ceil((100 - progress) / speed);
        for idx, val in enumerate(progresses):
            progresses[idx] += speeds[idx] * day;
        count = 0;
        while progresses and progresses[0] >= 100:
            progresses.popleft();
            speeds = speeds[1:];
            count += 1;
        answer.append(count);
    return answer