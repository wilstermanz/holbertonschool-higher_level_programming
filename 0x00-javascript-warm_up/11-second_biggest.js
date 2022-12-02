#!/usr/bin/node
let secondBiggest = 0;
let biggest = 0;
if (process.argv.length <= 2) {
  console.log(secondBiggest);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const current = parseInt(process.argv[i]);
    if (current > biggest) {
      secondBiggest = biggest;
      biggest = current;
    } else if (current > secondBiggest && current !== biggest) {
      secondBiggest = current;
    }
  }
  console.log(secondBiggest);
}
