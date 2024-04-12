#!/usr/bin/node

const Square0 = require('./5-square');

class Square extends Square0 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const row = c.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
