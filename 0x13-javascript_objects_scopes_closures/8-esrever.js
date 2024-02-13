#!/usr/bin/node

exports.esrever = function (list) {
  // Define the esrever function and make it accessible outside the module

  // Loop through the array until the midpoint
  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    // Swap the elements at indices i and j using a temporary variable
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
  }
  return list;
};
