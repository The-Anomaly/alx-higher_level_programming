#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]]) {
    const r = newDict[dict[key]];
    r.push(key);
    newDict[dict[key]] = r;
  } else {
    newDict[dict[key]] = [key];
  }
}
console.log(newDict);
