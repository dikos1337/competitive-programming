const fs = require('fs')
let input = fs.readFileSync('day9.txt', 'utf8')
  .split("\n")
  .map((el) => parseInt(el));

let preamble_size = 25;
let preamble = input.slice(0, preamble_size);
let data = input.slice(preamble_size, input.length);
console.log(input);
console.log(preamble);
console.log(data);

function sumExist(num, where) {
  let where_slice = where.slice(where.length - preamble_size, where.length);
  for (n of where_slice) {
    for (n2 of where_slice) {
      if (n + n2 == num) {
        return true;
      }
    }
  }
  return false;
}

for (n_to_check of data) {
  if (sumExist(n_to_check, preamble)) {
    preamble.push(n_to_check);
    console.log("n=", n_to_check, true);
  } else {
    console.log("WRONG N", n_to_check);
    break;
  }
}
