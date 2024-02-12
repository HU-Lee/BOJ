import fs = require("fs");
const path = process.platform == "linux" ? "/dev/stdin" : "1.txt";

function main() {
  const input = fs
    .readFileSync(path)
    .toString()
    .split("\n")
    .map((s) => s.trim());
  for (const val of input) {
    if (val === "0 0") break;
    const nums = val.split(" ").map((x) => Number(x));
    console.log(nums[0] + nums[1]);
  }
}

main();