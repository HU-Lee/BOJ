const path = require("path");
const input = require("fs")
  // .readFileSync(path.resolve(__dirname, "example.txt"))
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map(Number);

input.sort((a: number, b: number) => a - b);

console.log(input.join(" "));
