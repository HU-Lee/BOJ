import fs = require("fs");

function main() {
  const input = fs.readFileSync("/dev/stdin").toString().split(" ");
  const y = Number(input[0]);
  console.log((y % 4 === 0 && y % 100 !== 0) || y % 400 === 0 ? 1 : 0);
}

main();