#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/', function (err, response, content) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(content).results;
    let numFilms = 0;
    for (const film in results) {
      for (const i in results[film].characters) {
        if (results[film].characters[i].includes('/18/')) {
          numFilms++;
        }
      }
    }
    console.log(numFilms);
  }
}
);
