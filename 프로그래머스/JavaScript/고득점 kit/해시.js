// 완주하지 못한 선수
function solution(participant, completion) {
    participant.sort();
    completion.sort();
    for (let i in participant) {
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }
}

// 위장
function solution(clothes) {
    var answer = 1;
    var comb = {};
    for (var i = 0; i < clothes.length; i++) {
        comb[clothes[i][1]] = (comb[clothes[i][1]] || 1) + 1;
    }
    for (var key in comb) {
        answer *= comb[key];
    }
    return answer - 1;
}

