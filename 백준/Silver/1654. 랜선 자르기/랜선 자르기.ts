const path = require("path");
const input = require("fs")
  // .readFileSync(path.resolve(__dirname, "example.txt"))
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");

const base = input[0].split(" ").map(Number);
const k = base[0];
const n = base[1];

const arr: number[] = [];

for (let i = 1; i <= k; i++) {
  arr.push(Number(input[i]));
}

let min = 1;
let max = Math.pow(2, 31) - 1;

while (min <= max) {
  const mid = Math.floor((min + max) / 2);
  let sum = 0;
  for (let i = 0; i < k; i++) {
    sum += Math.floor(arr[i] / mid);
  }
  if (sum >= n) {
    min = mid + 1;
  } else {
    max = mid - 1;
  }
}

console.log(max);
