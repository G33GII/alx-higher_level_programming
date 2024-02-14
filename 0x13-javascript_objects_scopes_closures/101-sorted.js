#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrencesDict = {};

// Loop through each user id in the original dictionary
for (const userId in dict) {
  // Get the number of occurrences for the current user id
  const occurrences = dict[userId];

  // If the occurrences is not a key in the occurrencesDict, initialize it as an empty array
  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }

  // Push the user id to the array corresponding to its number of occurrences
  occurrencesDict[occurrences].push(userId);
}

console.log(occurrencesDict);
