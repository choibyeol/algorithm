# 크레인 인형뽑기 게임 level 1
def solution(board, moves):
    answer = 0
    doll = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                doll.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(doll) >= 2:
            if doll[-1] == doll[-2]:
                doll = doll[0:-2]
                answer += 2
    return answer