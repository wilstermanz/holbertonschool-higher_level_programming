#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      occurrences++;
    }
  }
  return occurrences;
};
