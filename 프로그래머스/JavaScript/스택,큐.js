// 기능개발 level 2
function solution(progresses, speeds) {
  const answer = [];
  let time = 0;
  let cnt = 0;

  while (progresses.length > 0) {
    if (progresses[0] + time * speeds[0] >= 100) {
      progresses.shift();
      speeds.shift();
      cnt += 1;
    } else {
      if (cnt > 0) {
        answer.push(cnt);
        cnt = 0;
      }
      time += 1;
    }
  }
  answer.push(cnt);
  return answer;
}
