#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const route = process.argv[3];

request(url, (error, response, body) => {
  if (error) throw error;
  const j = body;

  fs.writeFile(route, j, 'utf-8', err => {
    if (err) throw err;
  });
});
