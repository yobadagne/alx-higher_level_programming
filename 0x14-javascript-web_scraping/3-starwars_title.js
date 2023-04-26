#!/usr/bin/node
// requesting star wars api
const request = require('request');
let api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(api, (err, res, body)=>{
console.log(JSON.parse(body).title)
});

