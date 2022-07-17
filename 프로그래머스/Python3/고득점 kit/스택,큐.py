# 기능개발 level 2
def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)
    return answer

# 프린터 level 2
def solution(priorities, location):
    answer = 0
    arr1 = [c for c in range(len(priorities))]
    arr2 = priorities.copy()
    
    i = 0
    while True:
        if arr2[i] < max(arr2[i+1:]):
            arr1.append(arr1.pop(i))
            arr2.append(arr2.pop(i))
        else:
            i += 1
        if arr2 == sorted(arr2, reverse=True):
            break
        
    answer = arr1.index(location) + 1
    return answer

# 다리를 지나는 트럭 level 2
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while True:
        answer += 1
        bridge.pop(0)
        if len(truck_weights) > 0:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        if len(bridge) == 0:
            break
        
    return answer

# 주식가격 level 2
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    cnt = len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# 같은 숫자는 싫어 level 1
def solution(arr):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        else:
            if answer[-1] == i:
                continue
            else:
                answer.append(i)
    return answer