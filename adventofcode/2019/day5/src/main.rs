#[derive(Debug)]
enum ParameterMode {
    Position,
    Immediate,
}
impl ParameterMode {
    fn match_mode(mode: usize) -> ParameterMode {
        match mode {
            0 => ParameterMode::Position,
            1 => ParameterMode::Immediate,
            _ => panic!("Invalid parameter mode"),
        }
    }
}

#[derive(Debug)]
enum OpCode {
    Sum,
    Mul,
    Input,
    Output,
    JpmTrue,
    JpmFalse,
    LessThan,
    Equals,
}

impl OpCode {
    fn match_code(mode: usize) -> OpCode {
        match mode {
            1 => OpCode::Sum,
            2 => OpCode::Mul,
            3 => OpCode::Input,
            4 => OpCode::Output,
            5 => OpCode::JpmTrue,
            6 => OpCode::JpmFalse,
            7 => OpCode::LessThan,
            8 => OpCode::Equals,
            _ => panic!("Invalid opcode: {}", mode),
        }
    }
}

struct IntCode {
    memory: Vec<i64>,
    ip: usize, // Instruction Pointer
    user_input: Option<usize>,
}

impl IntCode {
    fn from(memory: Vec<i64>) -> Self {
        IntCode {
            memory,
            ip: 0,
            user_input: None,
        }
    }

    fn set_user_input(&mut self, input: usize) {
        self.user_input = Some(input);
    }

    fn run(&mut self) {
        while self.memory[self.ip] != 99 {
            let op = self.memory[self.ip];
            self.execute_op(op as usize);
        }
    }

    fn get_parameter(&self, offset: usize, mode: ParameterMode) -> usize {
        match mode {
            ParameterMode::Position => self.memory[self.ip + offset] as usize,
            ParameterMode::Immediate => self.ip + offset,
        }
    }

    fn execute_op(&mut self, op: usize) {
        let code = OpCode::match_code(op % 10);
        let mode_1st = ParameterMode::match_mode(op / 100 % 10);
        let mode_2nd = ParameterMode::match_mode(op / 1000 % 10);
        let mode_3rd = ParameterMode::match_mode(op / 10000 % 10);

        match code {
            OpCode::Sum => {
                let a = self.get_parameter(1, mode_1st);
                let b = self.get_parameter(2, mode_2nd);
                let c = self.get_parameter(3, mode_3rd);
                let sum = self.memory[a] + self.memory[b];
                self.memory[c] = sum;
                self.ip += 4;
            }
            OpCode::Mul => {
                let a = self.get_parameter(1, mode_1st);
                let b = self.get_parameter(2, mode_2nd);
                let c = self.get_parameter(3, mode_3rd);
                let mul = self.memory[a] * self.memory[b];
                self.memory[c] = mul;
                self.ip += 4;
            }
            OpCode::Input => match self.user_input {
                Some(input) => {
                    let a = self.get_parameter(1, mode_1st);
                    self.memory[a] = input as i64;
                    self.ip += 2;
                    self.user_input = None;
                }
                None => {
                    let a = self.get_parameter(1, mode_1st);
                    self.memory[a] = a as i64;
                    self.ip += 2;
                }
            },
            OpCode::Output => {
                let a = self.get_parameter(1, mode_1st);
                println!("Output: {}", self.memory[a]);
                self.ip += 2;
            }
            OpCode::JpmTrue => {
                let a = self.get_parameter(1, mode_1st);
                let b = self.get_parameter(2, mode_2nd);
                if self.memory[a] != 0 {
                    self.ip = self.memory[b] as usize;
                } else {
                    self.ip += 3;
                }
            }
            OpCode::JpmFalse => {
                let a = self.get_parameter(1, mode_1st);
                let b = self.get_parameter(2, mode_2nd);
                if self.memory[a] == 0 {
                    self.ip = self.memory[b] as usize;
                } else {
                    self.ip += 3;
                }
            }
            OpCode::LessThan => {
                let a = self.get_parameter(1, mode_1st);
                let b = self.get_parameter(2, mode_2nd);
                let c = self.get_parameter(3, mode_3rd);
                if self.memory[a] < self.memory[b] {
                    self.memory[c] = 1;
                } else {
                    self.memory[c] = 0;
                }
                self.ip += 4;
            }
            OpCode::Equals => {
                let a = self.get_parameter(1, mode_1st);
                let b = self.get_parameter(2, mode_2nd);
                let c = self.get_parameter(3, mode_3rd);
                if self.memory[a] == self.memory[b] {
                    self.memory[c] = 1;
                } else {
                    self.memory[c] = 0;
                }
                self.ip += 4;
            }
        }
    }
}

fn part1(memory: Vec<i64>) {
    let mut intcode = IntCode::from(memory);
    intcode.set_user_input(1);
    intcode.run();
}

fn part2(memory: Vec<i64>) {
    let mut intcode = IntCode::from(memory);
    intcode.set_user_input(5);
    intcode.run();
}
fn main() {
    let input = include_str!("../input.txt");

    let memory = input
        .trim()
        .split(',')
        .map(|s| s.parse::<i64>().unwrap())
        .collect::<Vec<_>>();

    println!("Part 1:");
    part1(memory.clone());

    println!("Part 2:");
    part2(memory);
}
