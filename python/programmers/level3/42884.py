# 정답 봄
# 정렬하고 log(n)으로 접근하자...!

def solution(routes):
    answer = 1

    routes.sort(key=lambda x: x[1]);
    minR, maxR = routes[0];
    for route in routes:
        start, end = route;
        if start > maxR:
            maxR = end;
            answer += 1;
    return answer