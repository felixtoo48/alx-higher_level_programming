#!/usr/bin/node
// A script that writes a string to a file

let filename = process.argv[2];
let text = process.argv[3];
const fs = require('fs');
fs.writeFile(filename, text, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
