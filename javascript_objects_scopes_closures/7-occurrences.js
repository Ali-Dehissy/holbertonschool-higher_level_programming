#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let j = 0;
  let counter = 0;
  for (j = 0; j < list.length; j++) {
    if (list[j] === searchElement) {
      counter++;
    }
  }
  return counter;
};
