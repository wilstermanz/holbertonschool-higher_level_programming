#!/usr/bin/node
let arg1 = 'undefined';
let arg2 = 'undefined';
if (process.argv[2]) {
  arg1 = process.argv[2];
}
if (process.argv[3]) {
  arg2 = process.argv[3];
}
console.log('%s is %s', arg1, arg2);
