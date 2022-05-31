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