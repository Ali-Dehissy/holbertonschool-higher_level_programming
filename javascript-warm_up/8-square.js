#!/usr/bin/node
if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing size');
} else {
  let j;
  for (j = 0; j < process.argv[2]; j++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
