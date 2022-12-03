#!/usr/bin/node
let prints = 0;
exports.logMe = function (item) {
  console.log('%i: %s', prints, item);
  prints++;
};
