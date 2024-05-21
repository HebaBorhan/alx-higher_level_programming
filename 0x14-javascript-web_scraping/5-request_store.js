#!/usr/bin/node

const fs = require('node:fs');
const url = process.argv[2];
const filePath = process.argv[3];

fs.writeFile(url, filePath, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
