#!/usr/bin/node

const add = (a, b) => {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    return parseInt(a) + parseInt(b);
  }
};

module.exports = {
  add
};
