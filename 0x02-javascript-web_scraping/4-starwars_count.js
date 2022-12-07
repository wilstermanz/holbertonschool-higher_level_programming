#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, content) {
  if (err) {
    console.log(err);
  } else {
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
