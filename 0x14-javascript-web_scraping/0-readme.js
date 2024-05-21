#!/usr/bin/node
const fs = require('node:fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
