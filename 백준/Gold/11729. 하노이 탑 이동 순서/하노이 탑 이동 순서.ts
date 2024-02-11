import fs = require("fs");

const arr = [];

function get_hanoi_steps(n: number, start: number, end: number, mid: number) {
  if (n == 1) {
    return arr.push([start, end]);
  } else {
    get_hanoi_steps(n - 1, start, mid, end);
    arr.push([start, end]);
    get_hanoi_steps(n - 1, mid, end, start);
  }
}

function get_hanoi_count(n: number): bigint {
  if (n <= 1) return BigInt(1);

  const answer = get_hanoi_count(n - 1) * BigInt(2) + BigInt(1);
  return answer;
}
function main() {
  const input = fs.readFileSync("/dev/stdin").toString().split("\n");

  const n = Number(input[0]);

  console.log(get_hanoi_count(n).toString());
  if (n <= 20) {
    get_hanoi_steps(n, 1, 3, 2);
    console.log(arr.map((x: number[]) => x.join(" ")).join("\n"));
  }
}

main();