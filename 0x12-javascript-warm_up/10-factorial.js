#!/usr/bin/node
// script that computes and prints a factorial
const n = parseInt(process.argv[2]);

function factorial (n) {
  if (n <= 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(n));
