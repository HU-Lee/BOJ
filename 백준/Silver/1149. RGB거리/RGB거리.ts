const path = require("path");
const input = require("fs")
  // .readFileSync(path.resolve(__dirname, "example.txt"))
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");

const n = Number(input[0]);

const rgbs: number[][] = [];
for (let i = 1; i <= n; i++) {
  const arr: number[] = input[i].split(" ").map(Number);
  rgbs.push(arr);
}

for (let i = 1; i < n; i++) {
  for (let j = 0; j < 3; j++) {
    rgbs[i][j] += Math.min(rgbs[i - 1][(j + 1) % 3], rgbs[i - 1][(j + 2) % 3]);
  }
}

console.log(Math.min(rgbs[n - 1][0], rgbs[n - 1][1], rgbs[n - 1][2]));
