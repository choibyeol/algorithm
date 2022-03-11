# k번째 수
def solution(array, commands):
    answer = []
    list = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1];
        idx = commands[i][2] - 1;
        list = array[start:end]
        list.sort()
        answer.append(list[idx])
    return answer

# 가장 큰 수
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer
    """
    틀렸던 답
    def solution(numbers):
        answer = ''
        temp = []
        numbers = sorted(map(str, numbers), reverse=True)
        i = 0
        for num in numbers:
            if '0' in num:
                temp.append(num)
            else:
                answer += num
            if i < len(numbers) - 1:
                if num[0] != numbers[i+1][0]:
                    temp.sort()
                    for num in temp:
                        answer += num
                    temp = []
            if i == len(numbers) - 1:
                temp.sort()
                for num in temp:
                    answer += num
            i += 1
        return answer
    """