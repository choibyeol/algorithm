// k번째수
function solution(array, commands) {
    var answer = [];
    for (var i = 0; i < commands.length; i++) {
        var start = commands[i][0] - 1;
        var end = commands[i][1];
        var idx = commands[i][2] - 1;
        var list = array.slice(start, end).sort((a, b) => { return a - b });
        // 오름차순 정렬. 정렬 순서를 정의해주지 않으면 배열의 element들이 문자열로 취급되어 유니코드 값 순서대로 정렬된다.
        answer.push(list[idx]);
    }
    return answer;
}