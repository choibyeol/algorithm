# 더 맵게 level 2
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        sco1 = heapq.heappop(scoville)
        sco2 = heapq.heappop(scoville)
        newsco = sco1 + sco2 * 2
        heapq.heappush(scoville, newsco)
        answer += 1
    return answer