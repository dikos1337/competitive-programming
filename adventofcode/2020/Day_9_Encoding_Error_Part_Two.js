const fs = require('fs')
let input = fs.readFileSync('day9.txt', 'utf8')
  .split("\n")
  .map((el) => parseInt(el));

let preamble_size = 25;
let preamble = input.slice(0, preamble_size);
let data = input.slice(preamble_size, input.length);

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

let wrong_n = null;
for (n_to_check of data) {
  if (sumExist(n_to_check, preamble)) {
    preamble.push(n_to_check);
  } else {
    console.log("WRONG N", n_to_check);
    wrong_n = n_to_check;
    break;
  }
}

for (let n_slice = 2; n_slice < preamble.length; n_slice++) {

  for (let i = 0; i < preamble.length; i++) {
    let preamble_slice = preamble.slice(i, i + n_slice);
    let preamble_slice_sum = preamble_slice.reduce((a, b) => a + b);
    if (preamble_slice_sum == wrong_n) {
      console.log("preamble_slice_sum", preamble_slice_sum);
      console.log("preamble_slice", preamble_slice);
      console.log("wrong_n", wrong_n);
      let encryption_weakness =
        Math.min(...preamble_slice) + Math.max(...preamble_slice);
      console.log("encryption_weakness", encryption_weakness);
      break;
    }
  }
}
