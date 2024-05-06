const path = require("path");
const input = require("fs")
  // .readFileSync(path.resolve(__dirname, "example.txt"))
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");

const arr = input[0].split(" ").map(Number);
const n = arr[0];
const k = arr[1];

const direction = {};

for (let i = 0; i < n; i++) {
  direction[i] = Number(input[i + 1]);
}

let count = 0;
const visited = new Array(n).fill(false);

let cur = 0;
while (visited[cur] === false) {
  visited[cur] = true;
  count++;
  cur = direction[cur];
  if (cur === k) {
    break;
  }
}
if (cur === k) {
  console.log(count);
} else {
  console.log(-1);
}
