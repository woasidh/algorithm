from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0: return 5 * len(cities);
    cache = [];
    time = 0;
    cities = list(map(lambda x: x.upper(), cities));

    for city in cities:
        if len(cache) < cacheSize:
            if city in cache:
                hitIdx = cache.index(city);
                cache.remove(city);
                cache.append(city);
                time += 1;
            else:
                cache.append(city);
                time += 5;
        else:
            if city in cache:
                hitIdx = cache.index(city);
                cache = cache[:hitIdx] + cache[hitIdx + 1:]
                cache.append(city);
                time += 1;
            else:
                cache = cache[1:];
                cache.append(city);
                time += 5;
    return time