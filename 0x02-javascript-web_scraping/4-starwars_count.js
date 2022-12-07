#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/people/18/', function (err, response, content) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(content).films.length);
  }
});
