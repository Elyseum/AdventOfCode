import { readFileSync } from "fs";

function readLine(fileName) {
  return readFileSync(fileName).toString();
}

function parseMulInstructions(line) {
  return line.match(/mul\(\d{1,3}\,\d{1,3}\)/g);
}

function execMul(mul) {
  const numbers = mul
    .substring(4, mul.length - 1)
    .split(",")
    .map((x) => parseInt(x));
  return numbers[0] * numbers[1];
}

function part1(fileName) {
  const line = readLine(fileName);
  return parseMulInstructions(line)
    .flat()
    .map(execMul)
    .reduce((x, y) => x + y, 0);
}

function part2(fileName) {
  const line = readLine(fileName);
  const parts = line.split(/do\(\)|don\'t\(\)/g);
  let cursor = 0;
  const enabledInstructions = [];
  const lineIterable = "do()" + line;
  parts.forEach((p, i) => {
    if (lineIterable.substring(cursor).startsWith("do()")) {
      enabledInstructions.push(...parseMulInstructions(p));
      cursor += "do()".length + p.length;
    } else {
      cursor += "don't()".length + p.length;
    }
  });
  return enabledInstructions.map(execMul).reduce((x, y) => x + y);
}

function solve(fileName, solver) {
  console.log(fileName + ": " + solver(fileName));
}

solve("data/03.example.txt", part1);
solve("data/03.txt", part1);
solve("data/03.example2.txt", part2);
solve("data/03.txt", part2);
