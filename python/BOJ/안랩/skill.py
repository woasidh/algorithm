import math

FIGS = ['S', 'D', 'H', 'C'];


def solution(cards):
    global FIGS;
    answer = -1

    figMap = {};
    for figure in FIGS:
        figMap[figure] = [];
    numMap = {};

    for card in cards:
        fig, num = card[0], card[1];
        figMap[fig].append(num);

    answer += getSameFigComb(figMap);

    return answer


def getSameFigComb(figMap):
    comb = 0;
    global FIGS;
    for figure in FIGS:
        for i in range(3, len(figMap[figure]) + 1):
            comb += math.comb(len(figMap[figure]), i);


solution(["S1","D3","S3","S4","H3","H1"]);
