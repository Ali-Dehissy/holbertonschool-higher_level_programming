#!/usr/bin/node
const parentSquare = require('./5-square');
module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let j = 0;
      for (j = 0; j < this.height; j++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
