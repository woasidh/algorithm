# 해답 찾아봄...
# 다 맞았는데 범위안에 들어있는 거에서 실수...

def solution(lines):
    answer = 0
    timelines = [];
    for line in lines:
        timelines.append(parseInput(line));
    fits = [];
    for sec, sec2 in timelines:
        fit = 0;
        for start, end in timelines:
            if checkTimeFit(sec, start, end): fit += 1;
        fits.append(fit);
        fit = 0;
        for start, end in timelines:
            if checkTimeFit(sec2, start, end): fit += 1;
        fits.append(fit);
    return max(fits);

def checkTimeFit(sec, start, end):
    return (sec <= start <= sec + 999 or sec <= end <= sec + 999) or (start < sec and end > sec + 999)

def calcToMili(time):
    hour, minute, sec = time.split(':');
    # 1초 - 1000
    # 1분 - 60000
    # 1시간 - 3600000
    total = 0;
    total += 3600000 * int(hour);
    total += 60000 * int(minute);
    total += 1000 * float(sec);
    return int(total);

def parseInput(input):
    _, finished, cost = input.split();
    cost = int(1000 * float(cost[:-1]));
    finished = calcToMili(finished);
    started = finished - cost + 1;
    return (started, finished);