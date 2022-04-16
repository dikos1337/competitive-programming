enum Instruction {
    TurnOn,
    TurnOff,
    Toggle,
}

fn parse_instruction(s: &str) -> Instruction {
    match s {
        "turn on" => Instruction::TurnOn,
        "turn off" => Instruction::TurnOff,
        "toggle" => Instruction::Toggle,
        _ => panic!("Unknown instruction: {}", s),
    }
}

fn parse_instruction_args(s: &str) -> (Instruction, usize, usize, usize, usize) {
    let mut instruction = "_";

    for ins in ["turn on", "turn off", "toggle"] {
        if s.starts_with(ins) {
            instruction = ins;
        }
    }

    let args: Vec<&str> = s[instruction.len() + 1..].split(" through ").collect();
    let start_x = args[0].split(',').collect::<Vec<&str>>()[0]
        .parse::<usize>()
        .unwrap();
    let start_y = args[0].split(',').collect::<Vec<&str>>()[1]
        .parse::<usize>()
        .unwrap();
    let end_x = args[1].split(',').collect::<Vec<&str>>()[0]
        .parse::<usize>()
        .unwrap();
    let end_y = args[1].split(',').collect::<Vec<&str>>()[1]
        .parse::<usize>()
        .unwrap();

    (
        parse_instruction(instruction),
        start_x,
        start_y,
        end_x,
        end_y,
    )
}

fn part1(input: &str) {
    let mut grid = vec![vec![false; 1000]; 1000];

    for line in input.lines() {
        let (instruction, x1, y1, x2, y2) = parse_instruction_args(line);
        for x in x1..=x2 {
            for y in y1..=y2 {
                match instruction {
                    Instruction::TurnOn => grid[x][y] = true,
                    Instruction::TurnOff => grid[x][y] = false,
                    Instruction::Toggle => grid[x][y] = !grid[x][y],
                }
            }
        }
    }

    let lights_on = grid
        .iter()
        .map(|x| x.iter().filter(|&x| *x).count())
        .sum::<usize>();

    println!("Part 1: {}", lights_on);
}

fn part2(input: &str) {
    let mut grid = vec![vec![0; 1000]; 1000];

    for line in input.lines() {
        let (instruction, x1, y1, x2, y2) = parse_instruction_args(line);
        for x in x1..=x2 {
            for y in y1..=y2 {
                match instruction {
                    Instruction::TurnOn => grid[x][y] += 1,
                    Instruction::TurnOff => match grid[x][y] {
                        0 => (),
                        _ => grid[x][y] -= 1,
                    },
                    Instruction::Toggle => grid[x][y] += 2,
                }
            }
        }
    }

    let total_brightness = grid.iter().map(|x| x.iter().sum::<i32>()).sum::<i32>();

    println!("Part 2: {}", total_brightness);
}

fn main() {
    let input = include_str!("../input.txt");
    part1(input);
    part2(input);
}
