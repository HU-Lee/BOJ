import fs = require("fs");
const path = process.platform == "linux" ? "/dev/stdin" : "1.txt";

function main() {
  const n = Number(fs.readFileSync(path).toString().trim());
  for (let i = 0; i < n; i++) {
    console.log(" ".repeat(i) + "*".repeat(n - i));
  }
}

main();