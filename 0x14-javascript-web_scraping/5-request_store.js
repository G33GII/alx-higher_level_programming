#!/usr/bin/node

// Import the built-in Node.js 'fs' module
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
