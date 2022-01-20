# 쉬움

import sys
from itertools import combinations, permutations

n = int(sys.stdin.readline());
relations = [];
for _ in range(n):
    relations.append(list(map(int, sys.stdin.readline().split())));

def getOtherTeam(team, n):
    otherTeam = [];
    for i in range(n):
        if not i in team:
            otherTeam.append(i);
    return otherTeam;

vals = []

for team in combinations(list(range(n)), n // 2):
    teamTotal, otherTeamTotal = 0, 0;
    otherTeam = getOtherTeam(team, n);
    for relation in permutations(team, 2):
        teamTotal += relations[relation[0]][relation[1]];
    for relation in permutations(otherTeam, 2):
        otherTeamTotal += relations[relation[0]][relation[1]];
    vals.append(abs(teamTotal - otherTeamTotal));

print(min(vals));
