#!/usr/bin/node
// Requires fs module in which
// readFile function is defined
const fs = require('fs');

// Reads file name from argv[2]
// in utf-8 format
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    // Checks for error and prints if it exists
    console.log(err);
  } else {
    // Prints contents of file if no error
    console.log(data);
  }
});
