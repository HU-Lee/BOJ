const path = require("path");
var input = require("fs")
  // .readFileSync(path.resolve(__dirname, "example.txt"))
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const sum = Number(input[0]);
const arr = input.slice(1).map(Number);

console.log(sum - arr.reduce((a, b) => a + b, 0));