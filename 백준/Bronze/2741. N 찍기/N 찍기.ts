import fs = require("fs");
const path = process.platform == "linux" ? "/dev/stdin" : "1.txt";

function main() {
  const input = Number(fs.readFileSync(path).toString().trim());
  console.log(
    new Array<number>(input)
      .fill(0)
      .map((_, idx) => idx + 1)
      .join("\n")
  );
}

main();