#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((n, i) => n * i);
console.log(newList);
