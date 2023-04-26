#!/usr/bin/node
// script that reads and prints the content of a file.
const File_path = process.argv[2];
const fs = require('fs');
fs.readFile(File_path, 'utf8', function (error, data) {
if (error) {
console.log(error);
	
 } 
else {
 console.log(File_path);
 }
 });
