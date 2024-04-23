#!/usr/bin/node

const request = require('request');
// Import the 'request' module.

request.get(process.argv[2])
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
