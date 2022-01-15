# 시간만 있으면 충분한 문제

def solution(str1, str2):
    # str1, str2마다 dictionary 형태로 저장
    # set에 모든 원소 저장
    hashMapA, hashMapB, setAB = {}, {}, set();
    intersection, union = 0, 0
    str1, str2 = str1.upper(), str2.upper();
    iterateString(str1, hashMapA, setAB);
    iterateString(str2, hashMapB, setAB);
    # 교집합 구하기
    for string in setAB:
        countA, countB = countFromMap(hashMapA, string), countFromMap(hashMapB, string);
        minCount, maxCount = min(countA, countB), max(countA, countB);
        intersection += minCount;
        union += maxCount;
    if union == 0 and intersection == 0: return 65536;
    return int((intersection / union) * 65536);


# string 파싱해서 hashmap, set 업데이트
def iterateString(string, hashmap, hashset):
    for idx in range(0, len(string) - 1):
        partialStr = string[idx:idx + 2]
        if not partialStr.isalpha(): continue;
        updateMap(hashmap, partialStr);
        hashset.add(partialStr);


# 문자열이랑 hashmap주고 있으면 1 추가, 없으면 1로 초기화
def updateMap(hashmap, string):
    if string in hashmap:
        hashmap[string] += 1;
    else:
        hashmap[string] = 1;


def countFromMap(hashMap, val):
    return hashMap[val] if val in hashMap else 0;