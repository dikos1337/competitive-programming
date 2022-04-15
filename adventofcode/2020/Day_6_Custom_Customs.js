const fs = require('fs')

const sum = (accumulator, currentValue) => accumulator + currentValue;


let input_data = fs.readFileSync('day6.txt', 'utf8');

input_data = input_data.split("\r\n\r\n")
  .map((el) => el.replaceAll("\r\n", ""))
  .map((el) => new Set(el))
  .map((el) => el.size)
  .reduce(sum)
console.log(input_data);
