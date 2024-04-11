#!/usr/bin/node

const square = process.argv[2];

if (isNaN(square)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < parseInt(square)) {
    let j = 0;
    while (j < parseInt(square)) {
      process.stdout.write('X');
      j++;
    }
    console.log();
    i++;
  }
}
