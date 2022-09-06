#!/usr/bin/node
// script that computes and prints a factorial
const n = parseInt(process.argv[2]);
let f = 1;
for (let i = n; i > 0; i--) {
  f *= i;
}
console.log(f);
