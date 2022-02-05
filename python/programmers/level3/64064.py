# dfs로 품
# 쉽게 품

answer = [];


def solution(user_ids, banned_ids):
    visitedMap = {};
    for userId in user_ids:
        visitedMap[userId] = False;
    bannedIdMatchMap = {};
    for idx, bannedId in enumerate(banned_ids):
        bannedIdMatchMap[idx] = getPossibleId(user_ids, bannedId);

    dfs(0, bannedIdMatchMap, visitedMap, []);
    return len(answer);


def dfs(bannedIdx, bannedIdMatchMap, visitedMap, ids):
    global answer;
    if bannedIdx == len(bannedIdMatchMap):
        listToSet = set(ids);
        if not listToSet in answer:
            answer.append(listToSet);
        return;

    possibleIds = bannedIdMatchMap[bannedIdx];
    for possibleId in possibleIds:
        if not visitedMap[possibleId]:
            visitedMap[possibleId] = True;
            dfs(bannedIdx + 1, bannedIdMatchMap, visitedMap, ids + [possibleId]);
            visitedMap[possibleId] = False;


def isPossible(userId, bannedId):
    if len(userId) != len(bannedId): return False;
    for i in range(len(userId)):
        if bannedId[i] != '*' and userId[i] != bannedId[i]:
            return False;
    return True;


def getPossibleId(userIds, bannedId):
    possibleIds = [];
    for userId in userIds:
        if isPossible(userId, bannedId): possibleIds.append(userId);
    return possibleIds;