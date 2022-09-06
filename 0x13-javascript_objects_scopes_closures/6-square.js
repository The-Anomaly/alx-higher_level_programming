#!/usr/bin/node
const SquarePrev = require('./5-square');

module.exports = class Square extends SquarePrev {
  charPrint (c) {
    let x = 'X';
    if (c) x = c;
    for (let i = this.height; i > 0; i--) {
      console.log(x.repeat(this.width));
    }
  }
};
