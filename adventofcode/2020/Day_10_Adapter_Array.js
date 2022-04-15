const fs = require('fs')
let input = fs.readFileSync('day10.txt', 'utf8')
  .split("\n")
  .map((el) => parseInt(el));



let devices_built_in_adapter_voltage = Math.max(...input) + 3;
input.push(0)
input.push(devices_built_in_adapter_voltage)


input.sort((a, b) => a - b);
console.log(input);

let counter = {
  1: 0,
  2: 0,
  3: 0,
};
for (let i = 1; i < input.length; i++) {
  console.log(input[i], input[i - 1], input[i] - input[i - 1]);
  switch (input[i] - input[i - 1]) {
    case 1:
      counter[1] += 1;
      break;
    case 2:
      counter[2] += 1;
      break;
    case 3:
      counter[3] += 1;
      break;
    default:
      console.log(
        "default case",
        input[i],
        input[i - 1],
        input[i] - input[i - 1]
      );
      break;
  }
}

console.log(counter);
