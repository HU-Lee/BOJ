import fs = require("fs");

function main() {
  const input = fs.readFileSync("/dev/stdin").toString().trim();
  console.log(input.length);
}

main();