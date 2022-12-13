#!/usr/bin/node
exports.esrever = function (list) {
  let j = 0;
  let k = list.length - 1;
  for (j = 0; j < list.length / 2; j++, k--) {
    [list[j], list[k]] = [list[k], list[j]];
  }
  return list;
};
