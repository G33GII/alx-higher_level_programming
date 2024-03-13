#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 5) {
  console.log('Usage: ./concat_files.js source_file1 source_file2 destination_file');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the contents of sourceFile1
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error('Error reading source file 1:', err);
    process.exit(1);
  }

  // Read the contents of sourceFile2
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error('Error reading source file 2:', err);
      process.exit(1);
    }

    // Concatenate the contents of both files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        process.exit(1);
      }
    });
  });
});
