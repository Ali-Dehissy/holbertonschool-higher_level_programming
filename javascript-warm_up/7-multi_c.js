#!/usr/bin/node
if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing number of occurences');
} else {
  let j;
  for (j = 0; j < process.argv[2]; j++) {
    console.log('C is fun');
  }
}
