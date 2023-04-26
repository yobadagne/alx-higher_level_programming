#!/usr/bin/node
// script that computes the number of tasks completed
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err == null) {
    const count = {};
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].completed === true) {
        if (count[obj[i].userId] === undefined) {
          count[obj[i].userId] = 0;
        }
        count[obj[i].userId] += 1;
      }
    }
    console.log(count);
  }
});
