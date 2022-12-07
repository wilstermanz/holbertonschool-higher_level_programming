#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (err, response, content) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], content, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
