# 못품

def solution(land):
    answer = 0

    for row in range(1, len(land)):
        for col in range(4):
            land[row][col] += max(land[row - 1][:col] + land[row - 1][col + 1:]);
    return max(land[-1]);