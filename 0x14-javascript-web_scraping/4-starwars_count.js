#!/usr/bin/node
// looking for actor
const request = require('request');
const api = process.argv[2];
request.get(api, function (res, body) {
  const result = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < JSON.parse(body).count; i++) {
    const found = result[i].characters.find(element => element === 'https://swapi-api.alx-tools.com/api/people/18/');
    if (found) {
      count++;
    }
  }
  console.log(count);
});
