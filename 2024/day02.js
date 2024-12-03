import { readFileSync } from "fs";

function parseLines(fileName) {
  return readFileSync(fileName)
    .toString()
    .split("\r\n")
    .map((v) => v.split(/\s+/));
}

function isSafeAscending(report, maxViolations) {
  if (maxViolations < 0) return false;
  let violations = 0;
  let prev = report[0] - 1; // Start with a marker that is always valid.
  let valid = true;
  report.forEach((v, i) => {
    if (valid) {
      if ([1, 2, 3].indexOf(v - prev) > -1) {
        // Valid ascend. Move marker forward to check next ascend.
        prev = v;
      } else {
        // Invalid ascend. Don't move marker (so we skip the next value).
        violations += 1;
        if (violations > maxViolations) {
          // If not tolerated, break the loop.
          valid = false;
        }
      }
    }
  });
  return valid;
}

function isSafeDescending(report, maxViolations) {
  return isSafeAscending(
    report.map((x) => x * -1),
    maxViolations
  );
}

function isSafe(report, maxViolations) {
  if (maxViolations === 0) {
    return (
      isSafeAscending(report, maxViolations) ||
      isSafeDescending(report, maxViolations)
    );
  }

  // Our checker validates from left to right. This means that if violations are tolerated, our
  // checker always ignores the next value (and not the current value).
  // E.g. if we check that [a,b] in [a,b,c] is not valid, we skip b and check [a,c].
  // This works if b is the problem (and should be omitted), but it does not work if a is the
  // problem (and should be omitted).
  // To ignore the current value, we need to check from right to left. This is the same as checking
  // descending reversed order. 
  return (
    isSafeAscending(report, maxViolations) ||
    isSafeDescending(report, maxViolations) ||
    isSafeDescending(report.toReversed(), maxViolations) ||
    isSafeAscending(report.toReversed(), maxViolations)
  );
}

function part1(fileName) {
  const reports = parseLines(fileName);
  let safe = 0;
  reports.forEach((r) => {
    if (isSafe(r, 0)) {
      safe += 1;
    }
  });
  return safe;
}

function part2(fileName) {
  const reports = parseLines(fileName);
  let safe = 0;
  reports.forEach((r) => {
    if (isSafe(r, 1)) {
      safe += 1;
    }
  });
  return safe;
}

function solve(fileName, solver) {
  console.log(fileName + ": " + solver(fileName));
}

solve("data/02.example.txt", part1);
solve("data/02.txt", part1);
solve("data/02.example.txt", part2);
solve("data/02.txt", part2);
