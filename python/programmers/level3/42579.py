import heapq


def solution(genres, plays):
    genreMap = {};
    genreCount = {};

    for idx, play in enumerate(plays):
        if genres[idx] not in genreMap:
            genreMap[genres[idx]] = [];
            genreCount[genres[idx]] = 0;
        genreCount[genres[idx]] += play;
        heapq.heappush(genreMap[genres[idx]], (-play, idx));

    genrePQ = [];
    for idx, genre in enumerate(genreCount):
        genrePQ.append([genre, genreCount[genre]]);
    genrePQ.sort(key=lambda x: -x[1]);
    answer = [];
    for val in genrePQ:
        genre = val[0];
        for i in range(2):
            if not genreMap[genre]: break;
            answer.append(heapq.heappop(genreMap[genre])[1]);

    return answer