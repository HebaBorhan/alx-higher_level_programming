#!/usr/bin/node

exports.converter = function (base) {
  function convert (n) {
    if (n < base) {
      return n.toString();
    } else {
      return convert(Math.floor(n / base)) + (n % base).toString();
    }
  }

  return convert;
};
