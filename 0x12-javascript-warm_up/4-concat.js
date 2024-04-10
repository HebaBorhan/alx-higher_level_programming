#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined) {
  console.log('undefined');
} else {
  console.log(arg);
}

console.log('is');
