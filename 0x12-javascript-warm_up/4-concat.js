#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No Arguments');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
