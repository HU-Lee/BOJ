const path = require("path");
const input = require("fs")
  // .readFileSync(path.resolve(__dirname, "example.txt"))
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");

const base = input[0].split(" ");
const n = Number(base[0]);
const category = base[1];
const s = new Set();

for (let i = 1; i <= n; i++) {
  s.add(input[i]);
}

if (category === "Y") {
  console.log(s.size);
} else if (category === "F") {
  console.log(Math.floor(s.size / 2));
} else {
  console.log(Math.floor(s.size / 3));
}
