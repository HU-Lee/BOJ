import fs = require("fs");
const path = process.platform == "linux" ? "/dev/stdin" : "1.txt";

function main() {
  const n = Number(fs.readFileSync(path).toString().trim());
  for (let i = 1; i <= n - 1; i++) {
    console.log("*".repeat(i) + " ".repeat(2 * (n - i)) + "*".repeat(i));
  }
  for (let i = n; i > 0; i--) {
    console.log("*".repeat(i) + " ".repeat(2 * (n - i)) + "*".repeat(i));
  }
}

main();
