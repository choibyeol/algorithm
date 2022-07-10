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