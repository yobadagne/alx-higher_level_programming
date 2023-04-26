#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request')
request.get(procee.argv[1], function (err, res) {
  if (err) {
    console.error('code:', err);
  } else {
    console.log('code:', res.statusCode);
  }
});
