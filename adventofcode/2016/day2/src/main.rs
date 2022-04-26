enum KeyboardKind {
    Default,
    Extended,
}

struct Keyboard {
    field: Vec<Vec<char>>,
    kind: KeyboardKind,
}

impl Keyboard {
    fn new(kind: KeyboardKind) -> Keyboard {
        match kind {
            KeyboardKind::Default => Keyboard {
                field: vec![
                    vec!['1', '2', '3'],
                    vec!['4', '5', '6'],
                    vec!['7', '8', '9'],
                ],
                kind,
            },
            KeyboardKind::Extended => Keyboard {
                field: vec![
                    vec![' ', ' ', '1', ' ', ' '],
                    vec![' ', '2', '3', '4', ' '],
                    vec!['5', '6', '7', '8', '9'],
                    vec![' ', 'A', 'B', 'C', ' '],
                    vec![' ', ' ', 'D', ' ', ' '],
                ],
                kind,
            },
        }
        // Keyboard {
        //     field: [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        // }
    }

    fn get_key(&self, x: usize, y: usize) -> char {
        self.field[y][x]
    }
}

struct Code {
    keyboard: Keyboard,
    code: Vec<char>,
    x: usize,
    y: usize,
}

impl Code {
    fn new(kind: KeyboardKind) -> Code {
        match kind {
            KeyboardKind::Default => Code {
                keyboard: Keyboard::new(kind),
                code: vec![],
                y: 1,
                x: 1,
            },
            KeyboardKind::Extended => Code {
                keyboard: Keyboard::new(kind),
                code: vec![],
                x: 0,
                y: 2,
            },
        }
    }
    fn parse_instructions(&mut self, instructions: &str) {
        match self.keyboard.kind {
            KeyboardKind::Default => self.parse_instructions_default(instructions),
            KeyboardKind::Extended => self.parse_instructions_extended(instructions),
        }
    }

    fn parse_instructions_default(&mut self, instructions: &str) {
        for c in instructions.chars() {
            match c {
                'U' => {
                    if self.y > 0 {
                        self.y -= 1;
                    }
                }
                'D' => {
                    if self.y < 2 {
                        self.y += 1;
                    }
                }
                'L' => {
                    if self.x > 0 {
                        self.x -= 1;
                    }
                }
                'R' => {
                    if self.x < 2 {
                        self.x += 1;
                    }
                }
                _ => panic!("Unknown instruction: {}", c),
            }
        }
        self.code.push(self.keyboard.get_key(self.x, self.y));
    }

    fn parse_instructions_extended(&mut self, instructions: &str) {
        for c in instructions.chars() {
            match c {
                'U' => {
                    if self.y > 0 && self.keyboard.get_key(self.x, self.y - 1) != ' ' {
                        self.y -= 1;
                    }
                }
                'D' => {
                    if self.y < 4 && self.keyboard.get_key(self.x, self.y + 1) != ' ' {
                        self.y += 1;
                    }
                }
                'L' => {
                    if self.x > 0 && self.keyboard.get_key(self.x - 1, self.y) != ' ' {
                        self.x -= 1;
                    }
                }
                'R' => {
                    if self.x < 4 && self.keyboard.get_key(self.x + 1, self.y) != ' ' {
                        self.x += 1;
                    }
                }
                _ => panic!("Unknown instruction: {}", c),
            }
        }
        self.code.push(self.keyboard.get_key(self.x, self.y));
    }
}

fn answer_pprint(code: &[char]) -> String {
    code.iter()
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join("")
}

fn part1(input: &str) {
    let mut code = Code::new(KeyboardKind::Default);
    for line in input.trim().lines() {
        code.parse_instructions(line);
    }
    println!("Part 1: {}", answer_pprint(&code.code));
}

fn part2(input: &str) {
    let mut code = Code::new(KeyboardKind::Extended);
    for line in input.trim().lines() {
        code.parse_instructions(line);
    }
    println!("Part 2: {}", answer_pprint(&code.code));
}

fn main() {
    let input = include_str!("../input.txt");
    part1(input);
    part2(input);
}
