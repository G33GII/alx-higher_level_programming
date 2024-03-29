#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter to keep track of occurrences
  let count = 0;

  // Iterate through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the search element
    if (list[i] === searchElement) {
      // If it is, increment the counter
      count++;
    }
  }

  // Return the count of occurrences
  return count;
};
