#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = parseInt(w);
      this.height = parseInt(h);
    }
  }
}

module.exports = Rectangle;
