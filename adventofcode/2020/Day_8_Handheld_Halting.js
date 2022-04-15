const fs = require('fs')
let input = fs.readFileSync('day8.txt', 'utf8').split("\n");

function parseInstruction(instruction) {
  let result = instruction.split(" ");
  return {
    operation: result[0],
    value: parseInt(result[1]),
    wasRun: false,
  };
}

let instructions = input.map((el) => parseInstruction(el));
let accumulator = 0;

console.log(instructions);

let pointer = 0;
let op = instructions[pointer];
while (!op.wasRun) {
  switch (op.operation) {
    case "nop":
      pointer += 1;
      op.wasRun = true;
      console.log("pointer=", pointer);
      break;
    case "jmp":
      pointer += op.value;
      op.wasRun = true;
      console.log("pointer=", pointer);
      break;
    case "acc":
      accumulator += op.value;
      pointer += 1;
      op.wasRun = true;
      console.log("pointer=", pointer, "accumulator=", accumulator);
      break;
  }
  // new instruction
  op = instructions[pointer];
}
console.log("ANSWER accumulator=", accumulator);
