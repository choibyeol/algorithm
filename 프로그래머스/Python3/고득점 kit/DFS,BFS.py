# 타겟 넘버 level 2
# BFS 풀이
def solution(numbers, target):
    answer = 0
    tree = [0]
    for num in numbers:
        temp = []
        for leaf in tree:
            temp.append(leaf + num)
            temp.append(leaf - num)
        tree = temp
    for leaf in tree:
        if leaf == target:
            answer += 1
    return answer

# DFS 풀이
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, depth + 1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth + 1)
        return answer

# 네트워크 level 3
# DFS 풀이
def solution(n, computers):
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(j)
                
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer

# 단어 변환 level 2
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    answers = []
    w = begin
    
    def dfs(w, target, answer, answers):
        if answers != []:
            if answer >= min(answers):
                return
        if w == target:
            answers.append(answer)
            return
        for word in words:
            cnt = 0
            for i in range(len(word)):
                if w[i] == word[i]:
                    cnt += 1
            if cnt == len(word) - 1:
                words.remove(word)
                front_w = w
                w = word
                answer += 1
                dfs(w, target, answer, answers)
                answer -= 1
                w = front_w
                words.append(word)

    dfs(w, target, answer, answers)
    return min(answers)

# 게임 맵 최단거리 level 2
from collections import deque

def solution(maps):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    n, m = len(maps), len(maps[0])
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                
    bfs(0, 0)
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    return answer