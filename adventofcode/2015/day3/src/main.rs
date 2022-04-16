use std::collections::HashMap;
#[derive(Hash, Eq, PartialEq, Copy, Clone)]
struct SantaPosition {
    x: i32,
    y: i32,
}

impl SantaPosition {
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }

    fn move_santa(&mut self, direction: &char) {
        match direction {
            '^' => self.y += 1,
            'v' => self.y -= 1,
            '>' => self.x += 1,
            '<' => self.x -= 1,
            _ => panic!("Invalid direction"),
        }
    }
}

fn part1(input: &str) {
    let mut houses = HashMap::new();
    let mut santa = SantaPosition::new(0, 0);
    *houses.entry(santa).or_insert(0) += 1;
    for direction in input.chars() {
        santa.move_santa(&direction);
        *houses.entry(santa).or_insert(0) += 1;
    }
    println!("Part 1: {}", houses.len());
}

fn part2(input: &str) {
    let mut houses = HashMap::new();
    let mut santa = SantaPosition::new(0, 0);
    let mut robosanta = SantaPosition::new(0, 0);
    *houses.entry(santa).or_insert(0) += 1;
    for (i, direction) in input.chars().enumerate() {
        if i % 2 == 0 {
            santa.move_santa(&direction);
            *houses.entry(santa).or_insert(0) += 1;
        } else {
            robosanta.move_santa(&direction);
            *houses.entry(robosanta).or_insert(0) += 1;
        }
    }
    println!("Part 2: {}", houses.len());
}

fn main() {
    let input = include_str!("../input.txt");
    part1(input);
    part2(input);
}
