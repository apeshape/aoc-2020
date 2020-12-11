const print = console.log;
const fs = require("fs");

const input = fs
  .readFileSync("./testdata1", "utf-8")
  .split("\n")
  .map((n) => parseInt(n, 10));
input.push(0);
input.push(Math.max(...input) + 3);
const data = input.sort((a, b) => a - b);

const visited = [];
let acc = 1;

const checkMutations = (num, arr) => {};

const getTree = (rest) => {
  if (rest.length == 0) {
    return rest;
  }
  const start = rest[0];
  const childrenOfStart = rest.filter((el) => el <= start + 3 && el !== start);
  const newRest = rest.filter(
    (el) => !childrenOfStart.includes(el) && el != start
  );

  if (
    childrenOfStart.length > 1 &&
    !visited.includes(childrenOfStart.join("-"))
  ) {
    // print("children", start, childrenOfStart);
    visited.push(childrenOfStart.join("-"));
    if (childrenOfStart.length > 2) {
      print("long children", start, childrenOfStart);
      const muts = checkMutations(start, childrenOfStart);
      acc *= 4;
    } else {
      acc *= childrenOfStart.length;
    }
  }
  return getTree(newRest);
};

print(data);
getTree(data);
data.forEach((el) => {
  const arr = data.filter((i) => i > el);
  getTree(arr);
});

print(acc);
