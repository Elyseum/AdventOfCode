import { readFileSync } from "fs";

function parseColumns(fileName) {
  const column1 = [];
  const column2 = [];

  readFileSync(fileName)
    .toString()
    .split("\n")
    .map((v) => v.split(/\s+/))
    .forEach((v) => {
      column1.push(v[0]);
      column2.push(v[1]);
    });

  return [column1, column2];
}

function part1(fileName) {
  const columns = parseColumns(fileName);
  columns[0].sort();
  columns[1].sort();
  return columns[0]
    .map((v, i) => Math.abs(v - columns[1][i]))
    .reduce((x, y) => x + y, 0);
}

function part2(fileName) {
  const columns = parseColumns(fileName);
  return columns[0]
    .map((v) => v * columns[1].filter((y) => y == v).length)
    .reduce((x, y) => x + y, 0);
}

function solve(fileName, solver) {
  console.log(fileName + ": " + solver(fileName));
}

solve("data/01.example.txt", part1);
solve("data/01.txt", part1);
solve("data/01.example.txt", part2);
solve("data/01.txt", part2);
