#!/usr/bin/node
const request = require('request');
const j = {};

request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const k = JSON.parse(body);
  for (const task in content) {
    if (!(k[task].userId in j)) {
      j[k[task].userId] = 0;
    }
    if (k[task].completed === true) {
      j[k[task].userId]++;
    }
  }
  console.log(j);
}
);
