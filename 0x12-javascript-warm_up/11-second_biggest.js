#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const list = process.argv;
if (list.length === 2 || list.length === 3) {
  console.log(0);
} else {
  const nums = list.slice(2, list.length).map(n => parseInt(n)).sort((a, b) => b - a);
  console.log(nums[1]);
}
