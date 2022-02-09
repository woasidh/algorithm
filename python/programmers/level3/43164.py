import heapq


def solution(tickets):
    answer = []

    answerPQ = [];
    visited = [False for i in range(len(tickets))];
    dfs('ICN', tickets, visited, ['ICN'], answerPQ);

    return heapq.heappop(answerPQ);


def dfs(current, tickets, visited, path, answerPQ):
    if len(path) == len(tickets) + 1:
        heapq.heappush(answerPQ, path);
        return;

    for idx, ticket in enumerate(tickets):
        start, end = ticket;
        if visited[idx]: continue;
        if start == current:
            visited[idx] = True;
            dfs(end, tickets, visited, path + [end], answerPQ);
            visited[idx] = False;