#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let j = 0;
    for (j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
};
