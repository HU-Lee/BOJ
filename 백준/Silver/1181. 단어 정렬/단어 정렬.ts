import fs = require("fs");

function main() {
  const input = fs.readFileSync("/dev/stdin").toString().split("\n");

  const n = parseInt(input[0]);

  let arr: string[] = [];
  for (let i = 1; i <= n; i++) {
    arr[i] = input[i];
  }
  arr = Array.from(new Set(arr));
  arr.sort((a, b) => {
    if (a.length != b.length) {
      return a.length - b.length;
    } else {
      return a.localeCompare(b);
    }
  });

  console.log(arr.join("\n"));
}

main();