#!/usr/bin/node
const side = parseInt(process.argv[2]);
if (isNaN(side)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < side; i++) {
    let row = '';
    for (let j = 0; j < side; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
