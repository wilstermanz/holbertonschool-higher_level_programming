#!/usr/bin/node
const NumArgs = process.argv.length - 2;

if (NumArgs < 1) {
  console.log('No argument');
} else if (NumArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
