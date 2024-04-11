#!/usr/bin/node

const a = process.argv[2];
const b = process.argv[3];

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  function add (a, b) {
    return a + b;
  }
  const result = add(parseInt(a), parseInt(b));
  console.log(result);
}
