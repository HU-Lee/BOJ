import fs = require("fs");
const path = process.platform == "linux" ? "/dev/stdin" : "1.txt";

function main() {
  const input = Number(fs.readFileSync(path).toString().trim());
  for (let i = 1; i <= 9; i++) {
    console.log(`${input} * ${i} = ${input * i}`);
  }
}

main();