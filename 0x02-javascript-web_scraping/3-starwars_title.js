#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (err, response, content) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(content).title);
  }
});
