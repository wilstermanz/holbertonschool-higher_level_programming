#!/usr/bin/node
let secondBiggest = 0;
let biggest = 0;
if (process.argv.length <= 2) {
  console.log(secondBiggest);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > biggest) {
      secondBiggest = biggest;
      biggest = process.argv[i];
    } else if (process.argv[i] > secondBiggest && process.argv[i] !== biggest) {
      secondBiggest = process.argv[i];
    }
  }
  console.log(secondBiggest);
}
