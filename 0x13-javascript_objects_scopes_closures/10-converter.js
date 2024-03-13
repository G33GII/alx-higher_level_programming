#!/usr/bin/node

exports.converter = function(base) {
  if (base < 2 || base > 32) {
    return null
  }
  return function(number) {
    return number.toString(base);
  };
};
