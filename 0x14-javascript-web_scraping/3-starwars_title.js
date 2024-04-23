#!/usr/bin / node

// Import the 'request' module.
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
