#!/usr/bin/node

const Square = require('./5-square');

class Square1 extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const row = 'c'.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(row);
    }
  }
}

module.exports = Square1;
