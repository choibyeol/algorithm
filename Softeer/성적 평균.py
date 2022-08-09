# 성적 평균 level 3
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

scores = list(map(int, input().split()))

for i in range(K):
    i, j = map(int, input().split())
    sum_score = sum(scores[i-1:j])
    average = round(sum_score / (j - i + 1), 2)
    print("%.2f" % average)