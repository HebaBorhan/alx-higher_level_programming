#!/usr/bin/node

const argvLen = process.argv.length;
const integers = process.argv.slice(2).map(arg => parseInt(arg));

if (argvLen === 2 || argvLen === 3) {
  console.log('0');
} else {
  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
